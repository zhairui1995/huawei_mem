#ifndef V8_PAGE_ACCESS_UAPI_H
#define V8_PAGE_ACCESS_UAPI_H

#include <linux/ioctl.h>
#include <linux/types.h>

#define V8_PAGE_ACCESS_DEVICE "/dev/v8_page_access"
#define V8_PAGE_ACCESS_IOC_MAGIC 'Y'

#define V8_PAGE_ABSENT     0
#define V8_PAGE_IDLE       1
#define V8_PAGE_REFERENCED 2
#define V8_PAGE_ERROR      3

struct v8_page_access_range {
    __s32 pid;
    __u32 reserved;
    __u64 start;
    __u64 end;
};

struct v8_page_access_info {
    __u64 vaddr;
    __u8 state;
    __u8 reserved[7];
};

struct v8_page_access_query {
    __s32 pid;
    __u32 page_count;
    __u64 start;
    __u64 end;
    __u64 pages_ptr;
};

#define V8_PAGE_ACCESS_CLEAR _IOW(V8_PAGE_ACCESS_IOC_MAGIC, 1, struct v8_page_access_range)
#define V8_PAGE_ACCESS_QUERY _IOWR(V8_PAGE_ACCESS_IOC_MAGIC, 2, struct v8_page_access_query)

#endif
