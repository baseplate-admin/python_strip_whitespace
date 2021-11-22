import builtins
from typing import Union


def guess(buffer: bytes) -> Union[str("BR"), str("GZ"), str("ZSTD"), str("PLAIN")]:
    """ """
    try:
        if buffer[0:3] == b"\x1f\x8b\x08":
            return "GZIP"
        elif buffer[0:3] == b"\x1b\xf5\x01":
            return "BR"
        elif buffer[0:3] == b"\x28\xb5\x2f":
            return "ZSTD"
        else:
            return "PLAIN"
            # raise ValueError("Encoding not Gzip or Brotli")

    except Exception as e:
        raise e
