[app]

# App name shown on Android
title = Advanced Calculator

# Internal package name (no spaces)
package.name = advancedcalculator

# Package domain
package.domain = org.example


# Main folder containing main.py
source.dir = .


# Files to include
source.include_exts = py,png,jpg,kv


# Python + Kivy dependencies
requirements = python3,kivy


# App orientation
orientation = portrait


# Don't run fullscreen
fullscreen = 0



[buildozer]

# Build log detail
log_level = 2



[android]

# Modern Android architecture
android.archs = arm64-v8a


# Minimum Android version
android.minapi = 21


# Target Android version
android.api = 35


# Use AndroidX
android.enable_androidx = True
