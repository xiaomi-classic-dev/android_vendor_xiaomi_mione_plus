#!/usr/bin/env python3
"""Apply or verify the MiOne ISP PP-loop pollfd initialization repair."""

import argparse
import hashlib
from pathlib import Path
import struct

ORIGINAL = 'f98785d3bb410ec826f94044458d943039833374a48e69e80c81875ad914a18f'
PATCHED = '07ea8520490a011059e70f42b362e9ea30bbd61c0326b59e216446a27efb5345'

# Thumb branch from 0x446b8 to unused file padding at 0x9ae14. The repair
# clears the four revents halfwords at sp+74/82/90/98, executes the displaced
# add.w ip,r4,#65536, then branches back to 0x446bc. No call or stack change.
ENTRY = bytes.fromhex('56f0acbb')
REPAIR = bytes.fromhex('0023adf84a30adf85230adf85a30adf8623004f5803ca9f747bc')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('blob', nargs='?', type=Path, default=
                        Path(__file__).resolve().parent.parent /
                        'proprietary/vendor/lib/liboemcamera.so')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = args.blob.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest == PATCHED:
        print('ISP poll repair verified: ' + digest)
        return
    if digest != ORIGINAL:
        parser.error('unknown ISP binary; refusing to patch SHA256 ' + digest)
    if args.check:
        parser.error('the original ISP binary still needs the poll repair')
    patched = bytearray(data)
    patched[0x446b8:0x446bc] = ENTRY
    patched[0x9ae14:0x9ae14 + len(REPAIR)] = REPAIR
    # Extend the first executable LOAD over 26 bytes of existing zero padding.
    # All sections, symbols, relocations, later offsets and file size stay put.
    for offset in (0x64, 0x68):
        struct.pack_into('<I', patched, offset, 0x9ae14 + len(REPAIR))
    if len(patched) != len(data) or hashlib.sha256(patched).hexdigest() != PATCHED:
        parser.error('repair output did not match the validated binary')
    args.blob.write_bytes(patched)
    print('ISP poll repair applied: ' + PATCHED)


if __name__ == '__main__':
    main()
