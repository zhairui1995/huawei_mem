KDIR ?= /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)
LINUX_ARTIFACT_DIR ?= artifacts/linux-$(shell uname -r)-$(shell uname -m)

obj-m += v8_page_access.o

.PHONY: all user module linux-artifact save-linux clean

all: user module

user: page_access_collect

page_access_collect: page_access_collect.c page_access_uapi.h
	$(CC) -Wall -Wextra -std=c11 -O2 -o $@ page_access_collect.c

module: v8_page_access.c page_access_uapi.h
	$(MAKE) -C $(KDIR) M=$(PWD) modules

linux-artifact:
	$(MAKE) clean
	$(MAKE) all
	$(MAKE) save-linux

save-linux: page_access_collect v8_page_access.ko
	mkdir -p $(LINUX_ARTIFACT_DIR)
	cp -f page_access_collect v8_page_access.ko page_access_uapi.h run_page_access_workflow.sh user_operation.sh draw_page_access.py $(LINUX_ARTIFACT_DIR)/
	printf '%s\n' \
		'KDIR=$(KDIR)' \
		'ARCH=$(shell uname -m)' \
		'CC=$(CC)' \
		> $(LINUX_ARTIFACT_DIR)/build-info.txt

clean:
	rm -f page_access_collect
	rm -f *.o *.ko *.mod *.mod.c *.mod.o *.symvers *.order .*.cmd .*.d
	rm -rf .tmp_versions __pycache__
