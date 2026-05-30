[app]

# (str) Title of your application
title = AI辅助心电预警系统

# (str) Package name
package.name = ai_ecg_alert

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourname

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,ttf,json,csv

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,numpy,pyserial,cython

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
entrypoint = demo4.py

# (list) Supported orientations
# Valid options are: portrait, landscape, sensorLandscape, reverseLandscape
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,MANIFEST.PERMISSION.BLUETOOTH_CONNECT,MANIFEST.PERMISSION.BLUETOOTH_SCAN

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK build tools version
android.build_tools_version = 33.0.2

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid network timeouts or cross-version flaws
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# 注意：这里改成了复数的 android.archs 以解决你截图里的报错警告
android.archs = armeabi-v7a, arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) Use androidx dependencies
android.use_androidx = True

# Presplash of the application
presplash.filename =

# Icon of the application
icon.filename = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
