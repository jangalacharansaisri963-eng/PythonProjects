[app]

# (string) Title of your application
title = Cryptographic Vault

# (string) Package name
package.name = cryptovault

# (string) Package domain (needed for android packaging)
package.domain = org.example

# (string) Source code directory
source.dir = .

# (list) Source files to include (letting Kivy read your design profiles)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application version
version = 1.0

# (list) Application requirements
# hostpython3 guarantees the cloud compilation tools match perfectly
requirements = hostpython3,python3,kivy==2.3.0

# (str) Supported orientations
orientation = portrait

# (int) Fullscreen mode
fullscreen = 1

# ==========================================
# Android Specific Configurations
# ==========================================

# (list) Permissions required by your file explorer engine
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (list) Target architectures (arm64-v8a covers almost all modern devices)
android.archs = arm64-v8a

# (bool) Automatically accept SDK license agreements during CI runs
android.accept_sdk_license = True

# NOTE: Hardcoded android.api, android.sdk, and android.ndk lines 
# are left commented out intentionally. This allows Buildozer to 
# pull down the absolute best matched pairing from the cloud.

# ==========================================
# Buildozer Settings
# ==========================================

[buildozer]

# (int) Log level (2 = standard details, 1 = error only)
log_level = 2

# (int) Warn if buildozer is run as root
warn_on_root = 1
