#!/usr/bin/env python3
"""Apply or verify fixed-size vendor paths in the MiOne graphics/thermal blobs."""

import argparse
import hashlib
from pathlib import Path

# Only paths whose targets are installed in vendor are changed. Keep Android's
# software GL libraries and tools such as /system/bin/ip on their platform paths.
# The known hashes include the existing Adreno renderer compatibility patch.
PATCHES = {'bin/thermald': ('fd9309a05c947e2781b819b0c6a29dd3ff369345a07ad56d1afc484b84687590',
                  '6f180df0120086f4f174162f40b29a4453f597869b01ce7b5323104fda187295',
                  (('/system/etc/thermald.conf', '/vendor/etc/thermald.conf'),)),
 'lib/libOpenCL.so': ('9200ca38982bc7f89fc295709018a56cf6529fee7a80796a6f45d14c02291039',
                      '7b19086edd42f7488c847274ea9358fb0593232e5b9e4b0a77bdb7d3553e0fd7',
                      (('/system/lib/egl/libGLESv2_adreno200.so',
                        '/vendor/lib/egl/libGLESv2_adreno200.so'),
                       ('/system/lib/libOpenCL.so', '/vendor/lib/libOpenCL.so'))),
 'lib/egl/libEGL_adreno200.so': ('0f8db880397671c978a6534dc778de1809d0821e3ba3392b52d531796ca75d2f',
                                 '8f96763d1ac2a29324350966bf833f70235ff0156059f015db53ec487001165d',
                                 (('/system/lib/egl/eglsubAndroid.so',
                                   '/vendor/lib/egl/eglsubAndroid.so'),
                                  ('/system/lib/egl/libGLESv1_CM_adreno200.so',
                                   '/vendor/lib/egl/libGLESv1_CM_adreno200.so'),
                                  ('/system/lib/egl/libGLESv2_adreno200.so',
                                   '/vendor/lib/egl/libGLESv2_adreno200.so'),
                                  ('/system/lib/egl/libq3dtools_adreno200.so',
                                   '/vendor/lib/egl/libq3dtools_adreno200.so'),
                                  ('/system/lib/libOpenVG.so', '/vendor/lib/libOpenVG.so'))),
 'lib/egl/libq3dtools_adreno200.so': ('eaf666602e92ee35b15644744ddef13633820d79e0123dd5c00dbb13cfc08e6f',
                                      'ab14f534e2e0de689c7fb904a8a63f6eab53f2bb1228e865390399c58cf64950',
                                      (('/system/lib/egl/libEGL_adreno200.so',
                                        '/vendor/lib/egl/libEGL_adreno200.so'),
                                       ('/system/lib/egl/libGLESv2S3D_adreno200.so',
                                        '/vendor/lib/egl/libGLESv2S3D_adreno200.so'),
                                       ('/system/lib/egl/libGLESv2_adreno200.so',
                                        '/vendor/lib/egl/libGLESv2_adreno200.so'),
                                       ('/system/lib/egl/libq3dtools_adreno200.so',
                                        '/vendor/lib/egl/libq3dtools_adreno200.so'))),
 'lib/egl/libGLESv1_CM_adreno200.so': ('3481b374a5fd587772b39612af20e002213cfe44460a9f914aa86be850127e4f',
                                       '0ceb03d18c8bec208effa2b98a628276b705fce2c35844d7dcee9c66bcef6d5b',
                                       (('/system/lib/egl/libGLESv2_adreno200.so',
                                         '/vendor/lib/egl/libGLESv2_adreno200.so'),)),
 'lib/egl/libGLESv2_adreno200.so': ('ba77721895ce566e52022736aedd5d48dc2a378a4fdecae7ecec66ccc3ef9ae7',
                                    'a78ffe93559ea697d9034c85727e148907f8e2bfb192162becb3baa8a495c28b',
                                    (('/system/lib/egl/libGLESv2S3D_adreno200.so',
                                      '/vendor/lib/egl/libGLESv2S3D_adreno200.so'),
                                     ('/system/lib/egl/libq3dtools_adreno200.so',
                                      '/vendor/lib/egl/libq3dtools_adreno200.so'),
                                     ('/system/lib/libsc-a2xx.so', '/vendor/lib/libsc-a2xx.so'))),
 'lib/egl/libGLESv2S3D_adreno200.so': ('6dc06825f81a6645aa7c94673b44042828523e84100d9db8e43ea94252b98e2d',
                                       'c194ee84394f32a565cc560733742ecd27b7f6b57193428546dc673f786b6be4',
                                       (('/system/lib/egl/libGLESv2_adreno200.so',
                                         '/vendor/lib/egl/libGLESv2_adreno200.so'),)),
 'lib/egl/eglsubAndroid.so': ('4a557367cfac0b7905df23c70f60fdf95a1cceb93afa6d79ef51fe3c8d08e763',
                              'b19aa8f31ed31dfbce21c4712b3285d654adc260fc28d304886d0127ff2cff96',
                              (('/system/lib/egl/libGLESv2S3D_adreno200.so',
                                '/vendor/lib/egl/libGLESv2S3D_adreno200.so'),))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base', nargs='?', type=Path, default=
                        Path(__file__).resolve().parent.parent / 'proprietary')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    pending = []
    for relative, (original, expected, paths) in PATCHES.items():
        blob = args.base / "vendor" / relative
        data = blob.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest == expected:
            print(relative + ': vendor paths verified')
            continue
        if digest != original:
            parser.error(relative + ': unknown binary SHA256 ' + digest)
        if args.check:
            parser.error(relative + ': vendor path patch is missing')
        patched = data
        for old, new in paths:
            old = old.encode('ascii') + b'\0'
            new = new.encode('ascii') + b'\0'
            if len(old) != len(new) or patched.count(old) != 1:
                parser.error(relative + ': unexpected path length or occurrence count')
            patched = patched.replace(old, new)
        if len(data) != len(patched) or hashlib.sha256(patched).hexdigest() != expected:
            parser.error(relative + ': unexpected patch result')
        pending.append((blob, patched))
    for blob, data in pending:
        blob.write_bytes(data)
        print(str(blob.relative_to(args.base)) + ': vendor paths applied')


if __name__ == '__main__':
    main()
