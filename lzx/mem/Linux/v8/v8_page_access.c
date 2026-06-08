#include <linux/capability.h>
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/mm.h>
#include <linux/miscdevice.h>
#include <linux/module.h>
#include <linux/pid.h>
#include <linux/pgtable.h>
#include <linux/sched/mm.h>
#include <linux/slab.h>
#include <linux/spinlock.h>
#include <linux/uaccess.h>
#include <linux/vmalloc.h>

#include "page_access_uapi.h"


#define V8_MAX_QUERY_PAGES (1024U * 1024U)//最大查询页数限制，防止用户空间请求过大导致内核内存耗尽


//根据pid获取mm_struct(描述进程地址空间的核心结构)
static struct mm_struct *v8_get_mm(pid_t pid)
{
    struct pid *pid_struct;
    struct task_struct *task;
    struct mm_struct *mm;

    pid_struct = find_get_pid(pid);
    if (!pid_struct)
        return NULL;

    task = get_pid_task(pid_struct, PIDTYPE_PID);
    put_pid(pid_struct);
    if (!task)
        return NULL;

    /**
    //这个函数会增加 mm_struct 的引用计数。
    // 这样即使目标进程正在退出，只要你拿到了 mm，它也不会立刻被释放
    // 用完必须mmput(mm)
     */
    mm = get_task_mm(task);
    put_task_struct(task);
    return mm;
}


//根据虚拟地址 addr 找到对应的 PTE，并加锁。
static pte_t *v8_get_pte_locked(struct mm_struct *mm, unsigned long addr, spinlock_t **ptl)
{
    pgd_t *pgd;
    p4d_t *p4d;
    pud_t *pud;
    pmd_t *pmd;
    pte_t *pte;

    pgd = pgd_offset(mm, addr);//找到该虚拟地址对应的 PGD 项。
    if (pgd_none(*pgd) || pgd_bad(*pgd))
        return NULL;

    p4d = p4d_offset(pgd, addr);
    if (p4d_none(*p4d) || p4d_bad(*p4d))
        return NULL;

    pud = pud_offset(p4d, addr);
    if (pud_none(*pud) || pud_bad(*pud))
        return NULL;

    pmd = pmd_offset(pud, addr);
    if (pmd_none(*pmd) || pmd_leaf(*pmd) || pmd_bad(*pmd))//如果 PMD 是 leaf，说明它可能是一个大页映射，例如 THP 透明大页。
        return NULL;//遇到大页直接返回，不在这里处理，这个函数只处理PTE级别的访问。

    pte = pte_offset_kernel(pmd, addr);
    if (!pte)
        return NULL;

    *ptl = pte_lockptr(mm, pmd);
    spin_lock(*ptl);
    return pte;
}

//lzx --查找大页级别的映射
//这个地址不是走到 PTE，而是在 PMD 层就完成映射
static pmd_t *v8_get_leaf_pmd_locked(struct mm_struct *mm, unsigned long addr, spinlock_t **ptl)
{
    pgd_t *pgd;
    p4d_t *p4d;
    pud_t *pud;
    pmd_t *pmd;

    pgd = pgd_offset(mm, addr);
    if (pgd_none(*pgd) || pgd_bad(*pgd))
        return NULL;

    p4d = p4d_offset(pgd, addr);
    if (p4d_none(*p4d) || p4d_bad(*p4d))
        return NULL;

    pud = pud_offset(p4d, addr);
    if (pud_none(*pud) || pud_bad(*pud))
        return NULL;

    pmd = pmd_offset(pud, addr);
    if (pmd_none(*pmd) || !pmd_leaf(*pmd))
        return NULL;
    if (pmd_bad(*pmd))
        return NULL;

    *ptl = pmd_lock(mm, pmd);
    return pmd;
}


//清除一个页面的 accessed bit
//这个函数负责对一个虚拟地址对应的页执行：young/accessed bit 清零
static void v8_clear_one(struct mm_struct *mm, unsigned long addr)
{
    spinlock_t *ptl;
    pmd_t *pmd;
    pte_t *pte;

    //先尝试大页映射
    pmd = v8_get_leaf_pmd_locked(mm, addr, &ptl);

    //如果这个大页present，并且 young=1，就把他改成old，也就是young=0
    if (pmd) {
        pmd_t old = *pmd;
        if (pmd_present(old) && pmd_young(old))
            set_pmd_at(mm, addr, pmd, pmd_mkold(old));
        spin_unlock(ptl);
        return;
    }

    //如果没有pmd大页，就走普通pte
    pte = v8_get_pte_locked(mm, addr, &ptl);
    if (pte) {
        pte_t old = ptep_get(pte);
        if (pte_present(old) && pte_young(old))
            set_pte_at(mm, addr, pte, pte_mkold(old));
        spin_unlock(ptl);
    }
}

//查询一个页面是否被访问过
static u8 v8_query_one(struct mm_struct *mm, unsigned long addr)
{
    spinlock_t *ptl;
    pmd_t *pmd;
    pte_t *pte;
    u8 state = V8_PAGE_ABSENT;

    //查询pmd大页，
    pmd = v8_get_leaf_pmd_locked(mm, addr, &ptl);
    /**
    如果 present且young=1 -> referenced
    如果 present且young=0 -> idle
    如果 not present -> absent
     */
    if (pmd) {
        pmd_t val = *pmd;
        if (pmd_present(val))
            state = pmd_young(val) ? V8_PAGE_REFERENCED : V8_PAGE_IDLE;
        spin_unlock(ptl);
        return state;
    }

    //查询普通pte
    pte = v8_get_pte_locked(mm, addr, &ptl);
    if (pte) {
        pte_t val = ptep_get(pte);
        if (pte_present(val))
            state = pte_young(val) ? V8_PAGE_REFERENCED : V8_PAGE_IDLE;
        spin_unlock(ptl);
    }
    return state;
}

//清除一段地址范围
static long v8_ioctl_clear(struct v8_page_access_range __user *argp)
{
    struct v8_page_access_range req;
    struct mm_struct *mm;
    unsigned long start;
    unsigned long end;
    unsigned long addr;

    if (copy_from_user(&req, argp, sizeof(req)))
        return -EFAULT;
    if (req.pid <= 0 || req.end <= req.start)
        return -EINVAL;

    start = req.start & PAGE_MASK;
    end = PAGE_ALIGN(req.end);
    mm = v8_get_mm(req.pid);
    if (!mm)
        return -ESRCH;

    mmap_read_lock(mm);
    for (addr = start; addr < end; addr += PAGE_SIZE)
        v8_clear_one(mm, addr);
    mmap_read_unlock(mm);
    mmput(mm);
    return 0;
}

//查询一段地址范围
static long v8_ioctl_query(struct v8_page_access_query __user *argp)
{
    struct v8_page_access_query req;
    struct v8_page_access_info *pages;
    struct mm_struct *mm;
    unsigned long start;
    unsigned long end;
    unsigned long addr;
    unsigned int expected;
    unsigned int index = 0;

    if (copy_from_user(&req, argp, sizeof(req)))
        return -EFAULT;
    if (req.pid <= 0 || req.end <= req.start || req.pages_ptr == 0)
        return -EINVAL;

    start = req.start & PAGE_MASK;
    end = PAGE_ALIGN(req.end);
    expected = (unsigned int)((end - start) >> PAGE_SHIFT);
    if (expected == 0 || expected > V8_MAX_QUERY_PAGES || req.page_count != expected)
        return -E2BIG;

    pages = kvcalloc(expected, sizeof(*pages), GFP_KERNEL);
    if (!pages)
        return -ENOMEM;

    mm = v8_get_mm(req.pid);
    if (!mm) {
        kvfree(pages);
        return -ESRCH;
    }

    mmap_read_lock(mm);
    for (addr = start; addr < end; addr += PAGE_SIZE) {
        pages[index].vaddr = addr;
        pages[index].state = v8_query_one(mm, addr);
        index++;
    }
    mmap_read_unlock(mm);
    mmput(mm);

    //拷贝结果回用户态
    if (copy_to_user((void __user *)(uintptr_t)req.pages_ptr, pages, expected * sizeof(*pages))) {
        kvfree(pages);
        return -EFAULT;
    }

    kvfree(pages);
    return 0;
}

//ioctl 分发函数，所有用户态 ioctl 都会进入这里
static long v8_page_access_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    if (!capable(CAP_SYS_ADMIN))
        return -EPERM;

    switch (cmd) {
    case V8_PAGE_ACCESS_CLEAR://清除指定范围页表项的 young bit
        return v8_ioctl_clear((struct v8_page_access_range __user *)arg);
    case V8_PAGE_ACCESS_QUERY://查询指定范围页表项的 young bit
        return v8_ioctl_query((struct v8_page_access_query __user *)arg);
    default:
        return -ENOTTY;
    }
}


//注册 misc 设备
static const struct file_operations v8_page_access_fops = {
    .owner = THIS_MODULE,
    .unlocked_ioctl = v8_page_access_ioctl,
#ifdef CONFIG_COMPAT
    .compat_ioctl = v8_page_access_ioctl,
#endif
};

//注册 misc device，这会创建/dev/v8_page_access，权限是0600，只有 root 可以读写
static struct miscdevice v8_page_access_dev = {
    .minor = MISC_DYNAMIC_MINOR,
    .name = "v8_page_access",
    .fops = &v8_page_access_fops,
    .mode = 0600,
};

//模块加载
static int __init v8_page_access_init(void)
{
    return misc_register(&v8_page_access_dev);
}

//模块卸载
static void __exit v8_page_access_exit(void)
{
    misc_deregister(&v8_page_access_dev);
}

//声明入口和出口
module_init(v8_page_access_init);
module_exit(v8_page_access_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("513test v8");
MODULE_DESCRIPTION("Clear and query PTE/PMD young(accessed) bits for selected process virtual ranges");
