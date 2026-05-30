[app]

# 应用名称
title = ECG Warning App

# 包名
package.name = ecgmonitor

# 包域名
package.domain = org.yangying

# 源码目录
source.dir = .

# 包含的文件类型
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,csv

# 版本号
version = 1.0.0

# Python 依赖
# 重点：
# 1. numpy 不要写 v1.26.4，要写 1.26.4
# 2. 你的代码用了 android.permissions，所以必须加 android
# 3. 你的代码顶部用了 serial，所以必须有 pyserial
# 4. 你的代码用了 jnius，所以必须有 pyjnius
requirements = python3,kivy,numpy==1.26.4,pyserial,pyjnius,android

# 屏幕方向
orientation = portrait

# ---------------------------------------------
# Android 配置
# ---------------------------------------------

# Android 权限
# 建议用短权限名，Buildozer 会自动生成完整 android.permission.xxx
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_CONNECT, BLUETOOTH_SCAN, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# 目标 Android API
android.api = 33

# 自动接受 SDK license
android.accept_sdk_license = True

# 最低 API
android.minapi = 24

# NDK 版本
android.ndk = 25b

# 架构，华为 MatePad Pro 11 用 arm64-v8a 没问题
android.archs = arm64-v8a

# 开启 logcat
android.logcat = True

# 不要写 android.entrypoint
# Buildozer 默认寻找 main.py
# 所以请确保你的入口文件叫 main.py
# android.entrypoint = main

# ---------------------------------------------
# Buildozer 配置
# ---------------------------------------------

[buildozer]

log_level = 2

warn_on_root = 1
