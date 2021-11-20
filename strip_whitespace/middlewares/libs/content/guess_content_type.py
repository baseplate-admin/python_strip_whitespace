from typing import Union


def guess(buffer: bytes) -> Union[str("BR"), str("GZ"), str("PLAIN")]:
    """ """
    try:
        if buffer[0:3] == b"\x1f\x8b\x08":
            return "GZ"
        elif buffer[0:3] == b"\x1b\xf5\x01":
            return "BR"
        else:
            return "PLAIN"
            # raise ValueError("Encoding not Gzip or Brotli")

    except Exception as e:
        raise e
