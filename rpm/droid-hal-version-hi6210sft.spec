# rpm_device is the name of the ported device
%define rpm_device hi6210sft
# rpm_vendor is used in the rpm space
%define rpm_vendor huawei
# Manufacturer and device name to be shown in UI
%define vendor_pretty Huawei
%define device_pretty P8Lite
# See ../droid-hal-version/droid-hal-device.inc
%define have_vibrator 1
# %define have_ffmemless 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
