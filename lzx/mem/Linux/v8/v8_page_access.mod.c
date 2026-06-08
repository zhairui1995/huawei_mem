#include <linux/module.h>
#include <linux/export-internal.h>
#include <linux/compiler.h>

MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x848a0d8d, "get_pid_task" },
	{ 0x920e864e, "put_pid" },
	{ 0xbf2c538b, "get_task_mm" },
	{ 0x1cf09ab5, "__put_task_struct_rcu_cb" },
	{ 0xb9fcd065, "call_rcu" },
	{ 0x2520ea93, "refcount_warn_saturate" },
	{ 0xb1ad3f2f, "boot_cpu_data" },
	{ 0xf296206e, "ptrs_per_p4d" },
	{ 0x6f8082dd, "pv_ops" },
	{ 0xd272d446, "BUG_func" },
	{ 0x095159b2, "physical_mask" },
	{ 0xbd03ed67, "page_offset_base" },
	{ 0xf296206e, "pgdir_shift" },
	{ 0x1bdf2bc8, "sme_me_mask" },
	{ 0xbd03ed67, "vmemmap_base" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xbd03ed67, "phys_base" },
	{ 0x82fd7238, "__ubsan_handle_shift_out_of_bounds" },
	{ 0xbd03ed67, "__ref_stack_chk_guard" },
	{ 0x0c161ddc, "capable" },
	{ 0x092a35a2, "_copy_from_user" },
	{ 0xf52f8b44, "__kvmalloc_node_noprof" },
	{ 0x73c05ac1, "__tracepoint_mmap_lock_start_locking" },
	{ 0xa59da3c0, "down_read" },
	{ 0x73c05ac1, "__tracepoint_mmap_lock_acquire_returned" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x2287b539, "__mmap_lock_do_trace_released" },
	{ 0xa59da3c0, "up_read" },
	{ 0xcf46e6bd, "mmput" },
	{ 0x73c05ac1, "__tracepoint_mmap_lock_released" },
	{ 0x546c19d9, "validate_usercopy_range" },
	{ 0xa61fd7aa, "__check_object_size" },
	{ 0x092a35a2, "_copy_to_user" },
	{ 0xf1de9e85, "kvfree" },
	{ 0xaedbc175, "__mmap_lock_do_trace_acquire_returned" },
	{ 0x2287b539, "__mmap_lock_do_trace_start_locking" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0xd272d446, "__fentry__" },
	{ 0xaca12394, "misc_register" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0xd5ad82a1, "misc_deregister" },
	{ 0xb0e4fe1f, "find_get_pid" },
	{ 0xbebe66ff, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x848a0d8d,
	0x920e864e,
	0xbf2c538b,
	0x1cf09ab5,
	0xb9fcd065,
	0x2520ea93,
	0xb1ad3f2f,
	0xf296206e,
	0x6f8082dd,
	0xd272d446,
	0x095159b2,
	0xbd03ed67,
	0xf296206e,
	0x1bdf2bc8,
	0xbd03ed67,
	0xde338d9a,
	0xbd03ed67,
	0x82fd7238,
	0xbd03ed67,
	0x0c161ddc,
	0x092a35a2,
	0xf52f8b44,
	0x73c05ac1,
	0xa59da3c0,
	0x73c05ac1,
	0xde338d9a,
	0x2287b539,
	0xa59da3c0,
	0xcf46e6bd,
	0x73c05ac1,
	0x546c19d9,
	0xa61fd7aa,
	0x092a35a2,
	0xf1de9e85,
	0xaedbc175,
	0x2287b539,
	0xd272d446,
	0xd272d446,
	0xaca12394,
	0xd272d446,
	0xd5ad82a1,
	0xb0e4fe1f,
	0xbebe66ff,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"get_pid_task\0"
	"put_pid\0"
	"get_task_mm\0"
	"__put_task_struct_rcu_cb\0"
	"call_rcu\0"
	"refcount_warn_saturate\0"
	"boot_cpu_data\0"
	"ptrs_per_p4d\0"
	"pv_ops\0"
	"BUG_func\0"
	"physical_mask\0"
	"page_offset_base\0"
	"pgdir_shift\0"
	"sme_me_mask\0"
	"vmemmap_base\0"
	"_raw_spin_lock\0"
	"phys_base\0"
	"__ubsan_handle_shift_out_of_bounds\0"
	"__ref_stack_chk_guard\0"
	"capable\0"
	"_copy_from_user\0"
	"__kvmalloc_node_noprof\0"
	"__tracepoint_mmap_lock_start_locking\0"
	"down_read\0"
	"__tracepoint_mmap_lock_acquire_returned\0"
	"_raw_spin_unlock\0"
	"__mmap_lock_do_trace_released\0"
	"up_read\0"
	"mmput\0"
	"__tracepoint_mmap_lock_released\0"
	"validate_usercopy_range\0"
	"__check_object_size\0"
	"_copy_to_user\0"
	"kvfree\0"
	"__mmap_lock_do_trace_acquire_returned\0"
	"__mmap_lock_do_trace_start_locking\0"
	"__stack_chk_fail\0"
	"__fentry__\0"
	"misc_register\0"
	"__x86_return_thunk\0"
	"misc_deregister\0"
	"find_get_pid\0"
	"module_layout\0"
;

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "07D0FA5F9342D7C1ED4210C");
