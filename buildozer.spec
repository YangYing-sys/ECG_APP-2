[app]

# 应用基本信息
title = 心电预警系统
package.name = ai_ecg_alert
package.domain = org.yourname

# 代码资源设置
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json

# 依赖库（加入了 cython）
requirements = python3,kivy,numpy,pyserial,cython

# 入口脚本
entrypoint = demo4.py

# 版本
version = 1.0.0

# 屏幕方向
orientation = portrait

# Android 权限
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android SDK/NDK 版本设置
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.use_androidx = True

# 指定支持的CPU架构（32位和64位）
android.arch = armeabi-v7a, arm64-v8a

# 预启动画面
presplash.filename =

[buildozer]
log_level = 2
