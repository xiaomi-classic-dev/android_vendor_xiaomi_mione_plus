#!/usr/bin/env python3
"""Select MiOne's dedicated interpreter without changing fixed-address code."""
import hashlib
import json
import pathlib
import struct
import sys

NAMES = ("bridgemgrd", "cnd", "gpsone_daemon", "netmgrd", "port-bridge",
         "qmiproxy", "qmuxd", "rmt_storage", "usbhub", "usbhub_init")
OLD = b"/system/bin/linker\0"
NEW = b"/system/bin/mld\0"


def patch(path):
    original = path.read_bytes()
    data = bytearray(original)
    if data[:7] != b"\x7fELF\x01\x01\x01":
        raise ValueError("{} is not a little-endian ELF32 file".format(path))
    if struct.unpack_from("<HH", data, 16) != (2, 40):
        raise ValueError("{} is not an ARM ET_EXEC executable".format(path))
    phoff = struct.unpack_from("<I", data, 28)[0]
    phentsize, phnum = struct.unpack_from("<HH", data, 42)
    if phentsize != 32:
        raise ValueError("Unexpected ELF program header size")
    matches = []
    for i in range(phnum):
        fields = struct.unpack_from("<8I", data, phoff + i * phentsize)
        if fields[0] == 3:
            matches.append((fields[1], fields[4]))
    if len(matches) != 1:
        raise ValueError("Expected exactly one PT_INTERP")
    offset, size = matches[0]
    old = bytes(data[offset:offset + size]).split(b"\0", 1)[0] + b"\0"
    if old not in (OLD, NEW) or size < len(NEW):
        raise ValueError("Unexpected interpreter in {}".format(path))
    data[offset:offset + size] = NEW.ljust(size, b"\0")
    if data != original:
        path.write_bytes(data)
    return {"file": "vendor/bin/" + path.name,
            "before_sha256": hashlib.sha256(original).hexdigest(),
            "after_sha256": hashlib.sha256(data).hexdigest(),
            "interp_offset": offset, "interp_size": size}


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    print(json.dumps([patch(root / "vendor/bin" / name) for name in NAMES], indent=2))
