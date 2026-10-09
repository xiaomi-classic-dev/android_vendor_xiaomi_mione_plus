# Copyright (C) 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0

LOCAL_PATH := $(call my-dir)

ifeq ($(TARGET_DEVICE),mione_plus)

include $(CLEAR_VARS)
LOCAL_MODULE := libaudioalsa
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libaudioalsa.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libacdbloader
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libacdbloader.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
# The old ARM blob imports libcrt symbols hidden from the public libc stub.
# Check against the implementation, which exports these as LIBC_PRIVATE.
LOCAL_SHARED_LIBRARIES := libcutils libutils liblog libaudcal libc.bootstrap libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libacdbmapper
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libacdbmapper.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libcutils libutils liblog libaudioalsa libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libstlport
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libstlport.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libc libm libstdc++
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libnv
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libnv.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := liboncrpc libdiag libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := liboncrpc
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/liboncrpc.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libcutils libutils libdsm libqueue libdiag liblog libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libaudcal
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libaudcal.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libutils liblog libdiag libacdbmapper libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libdiag
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libdiag.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
# The old ARM blob imports libcrt symbols hidden from the public libc stub.
# Check against the implementation, which exports these as LIBC_PRIVATE.
LOCAL_SHARED_LIBRARIES := libc.bootstrap libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libdsm
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libdsm.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
# The old ARM blob imports libcrt symbols hidden from the public libc stub.
# Check against the implementation, which exports these as LIBC_PRIVATE.
LOCAL_SHARED_LIBRARIES := libqueue libdiag libc.bootstrap libstdc++ libm
include $(BUILD_PREBUILT)

include $(CLEAR_VARS)
LOCAL_MODULE := libqueue
LOCAL_MODULE_OWNER := xiaomi
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_CLASS := SHARED_LIBRARIES
LOCAL_MODULE_SUFFIX := .so
LOCAL_SRC_FILES := proprietary/vendor/lib/libqueue.so
LOCAL_VENDOR_MODULE := true
LOCAL_STRIP_MODULE := false
LOCAL_CXX_STL := none
LOCAL_SHARED_LIBRARIES := libc libstdc++ libm
include $(BUILD_PREBUILT)

include $(LOCAL_PATH)/prebuilt/webview/Android.mk

endif
