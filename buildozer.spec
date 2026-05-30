[app]

title = 心电预警系统
package.name = ai_ecg_alert
package.domain = org.ecg

source.include_exts = py,png,jpg,kv,ttf,json

requirements = python3,kivy,numpy,pyserial

entrypoint = main.py

orientation = portrait

android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.use_androidx = True

presplash.filename =

[buildozer]

log_level = 2
