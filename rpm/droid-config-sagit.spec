# These and other macros are documented in ../droid-configs-device/droid-configs.inc

%define device sagit
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Mi 6

%define community_adaptation 1

%define android_version_major 13

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer
Obsoletes: ofono-configs-binder

# Device-specific usb-moded configuration
Provides: usb-moded-configs
Obsoletes: usb-moded-defaults

%define pixel_ratio 1.75

Requires: libgbinder-tools

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-sagit.inc
%include patterns/patterns-sailfish-device-configuration-sagit.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

