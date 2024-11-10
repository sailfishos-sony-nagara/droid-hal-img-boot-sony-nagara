%define device pdx224

%{please_check_boot_parameters_and_remove_this_line_when_ready}

%define mkbootimg_cmd mkbootimg --cmdline 'androidboot.selinux=permissive audit=0' --header_version 4 --os_version 14.0.0 --os_patch_level 2024-09 --kernel %{kernel} --ramdisk %{initrd} --output

%define vendor_boot_mkbootimg_cmd mkbootimg --header_version 4 --pagesize 0x00001000 --base 0x00000000 --kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --tags_offset 0x00000100 --dtb_offset 0x0000000001f00000 --vendor_cmdline 'androidboot.selinux=permissive coherent_pool=8M printk.devkmsg=on androidboot.fstab_suffix=pdx224 bootconfig' --board '' --dtb %{dtb} --vendor_ramdisk %{initrd} --vendor_boot

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/panel0-backlight/brightness
%define display_brightness 1024

%define lvm_root_size 5000

%define initrd_use_lz4 1

# missing dependency
BuildRequires: python3-base

%include initrd/droid-hal-device-img-boot.inc
