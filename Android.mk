# Copyright (C) 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := libaudioalsa
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/lib/libaudioalsa.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libacdbloader
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/lib/libacdbloader.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libacdbmapper
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/lib/libacdbmapper.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
include $(BUILD_PREBUILT)

# Android 8 removed STLport; retain the CM14 source-built ABI for old blobs.
include $(CLEAR_VARS)
LOCAL_MODULE := libstlport
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/lib/libstlport.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
include $(BUILD_PREBUILT)
