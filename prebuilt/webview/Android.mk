# Copyright (C) 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

LOCAL_PATH := $(call my-dir)

ifeq ($(TARGET_DEVICE),mione_plus)
include $(CLEAR_VARS)
LOCAL_MODULE := mione_webview
LOCAL_MODULE_STEM := webview.apk
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_PRODUCT_MODULE := true
LOCAL_CERTIFICATE := $(DEFAULT_SYSTEM_DEV_CERTIFICATE)
LOCAL_SRC_FILES := webview.apk
LOCAL_MODULE_TARGET_ARCH := arm
LOCAL_PREBUILT_JNI_LIBS_arm := @lib/armeabi-v7a/libwebviewchromium.so
LOCAL_REQUIRED_MODULES := libwebviewchromium_loader libwebviewchromium_plat_support
LOCAL_OVERRIDES_PACKAGES := webview
include $(BUILD_PREBUILT)
endif
