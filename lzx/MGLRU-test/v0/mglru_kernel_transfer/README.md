# MGLRU Page Control Kernel Transfer Kit

This package contains the patched Ubuntu HWE 6.17 kernel source and the config
used for `6.17.13-mglru`.

On the target machine:

```bash
tar -xf linux-hwe-6.17.0-mglru-source.tar.zst
cd mglru_kernel_transfer
./build_on_target.sh "$PWD/linux-hwe-6.17-6.17.0" "$PWD/linux-hwe-6.17-mglru-build"
```

Install after a successful build:

```bash
cd linux-hwe-6.17-6.17.0
sudo make O="$PWD/../linux-hwe-6.17-mglru-build" LOCALVERSION=-mglru modules_install
sudo make O="$PWD/../linux-hwe-6.17-mglru-build" LOCALVERSION=-mglru install
sudo update-grub
```

After reboot:

```bash
uname -r
ls /sys/kernel/debug/lru_gen_pages
```

Expected release: `6.17.13-mglru`.
