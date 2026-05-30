[app]

# (str) Application title (应用名称)
title = ECG Warning App

# (str) Package name (包名)
package.name = ecgmonitor

# (str) Package domain (needed for android packaging) (域名)
package.domain = org.yangying

# (str) Source code directory where main.py resides (源码目录)
source.dir = .

# (list) Source files to include (包含的文件类型，确保包含 simhei.ttf 和 seguiemj.ttf 字体)
source.include_exts = py,png,jpg,kv,atlas,ttf,csv

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# 注意：你的代码导入了 numpy, serial, jnius。
# android 是 jnius 正常运行所必需的依赖，pyapi 需要 pyserial 支撑。
requirements = python3,kivy==2.3.0,numpy==v1.26.4,pyserial,pyjnius

# (list) Supported orientations (屏幕朝向：因为有比较宽的心电图，推荐竖屏或跟随系统)
orientation = portrait

# ---------------------------------------------
# Android 专有详细配置
# ---------------------------------------------

# (list) Permissions (关键！你的代码调用了蓝牙和文件存储，必须在此处显式请求底层权限)
# 1. 经典蓝牙权限（配对和通讯）
# 2. Android 12+ 细分蓝牙权限 (BLUETOOTH_SCAN, BLUETOOTH_CONNECT)
# 3. 定位权限（蓝牙搜索周边设备的前提）
# 4. 读写手机存储权限（导出 CSV 所需）
android.permissions = android.permission.BLUETOOTH, android.permission.BLUETOOTH_ADMIN, android.permission.BLUETOOTH_CONNECT, android.permission.BLUETOOTH_SCAN, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE

# (int) Target Android API (目标运行 API，保持 33 / 34)
android.api = 33

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use (Buildozer 推荐对应 25b/25c 以兼容 numpy 编译)
android.ndk = 25b

# (list) The Android architectures to build for (支持 32位 和 64位 真机)
android.archs = arm64-v8a

# (bool) Enable Android logcat (调试日志输出)
android.logcat = True

# (str) Android entry point (你的入口文件如果是 demo4.py，在此处将它定义为入口启动文件名)
# 🚨 注意：Buildozer 原生要求入口必须叫 main.py。建议将你的 demo4.py 在仓库里重命名为 main.py！
# 如果已重命名为 main.py，下面这行可以保持默认；如果是 demo4.py，请将这里的值改为 demo4
android.entrypoint = main

# ---------------------------------------------
# 构建选项
# ---------------------------------------------
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and error)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
