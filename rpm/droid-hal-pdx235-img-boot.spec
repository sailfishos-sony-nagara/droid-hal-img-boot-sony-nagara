%define device pdx235

%define mkbootimg_cmd mkbootimg --cmdline 'androidboot.selinux=permissive audit=0' --header_version 3 --os_version 14.0.0 --os_patch_level 2024-05 --kernel %{kernel} --ramdisk %{initrd} --output

%define vendor_boot_mkbootimg_cmd mkbootimg --header_version 3 --pagesize 0x00001000 --base 0x00000000 --kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --tags_offset 0x00000100 --dtb_offset 0x0000000001f00000 --vendor_cmdline 'androidboot.bootdevice=4804000.ufshc swiotlb=2048 service_locator.enable=1 console=null androidboot.selinux=permissive androidboot.memcg=1 coherent_pool=8M printk.devkmsg=on androidboot.hardware=pdx235 androidboot.fstab_suffix=pdx235' --board '' --dtb %{dtb} --vendor_ramdisk %{initrd} --vendor_boot

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/panel0-backlight/brightness
%define display_brightness 1024

%define lvm_root_size 5000

%define initrd_use_lz4 1

%include initrd/droid-hal-device-img-boot.inc
