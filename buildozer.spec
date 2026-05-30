[app] 

# (str) Application title (应用名称) 
title = ECG Warning App

# (str) Package name (包名) 
package.name = ecgmonitor

# (str) Package domain (needed for android packaging) (域名) 
package.domain = org.yangying

# (str) Source code directory where main.py resides (源码目录) 
source.dir = . 

# (list) Source files to include (包含的文件类型，确保包含字体和 csv 等) 
source.include_exts = py,png,jpg,kv,atlas,ttf,csv

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# 固定 numpy 为稳定的 v1.26.4 避开底层 C++ 报错
requirements = python3,kivy,numpy==v1.26.4,pyserial,pyjnius

# (list) Supported orientations (屏幕朝向：推荐竖屏) 
orientation = portrait

# --------------------------------------------- 
# Android 专有详细配置
# --------------------------------------------- 

# (list) Permissions (显式请求底层权限：蓝牙、定位、读写手机存储) 
android.permissions = android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.BLUETOOTH_CONNECT, android.permission.BLUETOOTH_SCAN, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE

# (int) Target Android API (目标运行 API，保持 33) 
android.api = 33

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (int) Minimum API your APK will support. 
android.minapi = 24

# (str) Android NDK version to use 
android.ndk = 25b

# (list) The Android architectures to build for (支持 64位 真机) 
android.archs = arm64-v8a

# (bool) Enable Android logcat (调试日志输出) 
android.logcat = True

# 注释掉自定义 entrypoint，让系统默认寻找 main.py (最稳妥的做法)
# android.entrypoint = main 

# --------------------------------------------- 
# 构建选项
# --------------------------------------------- 
[buildozer] 

# (int) Log level (0 = error only, 1 = info, 2 = debug and error) 
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true) 
warn_on_root = 1
