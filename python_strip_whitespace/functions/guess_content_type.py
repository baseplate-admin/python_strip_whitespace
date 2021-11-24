def guess(buffer: bytes) -> str:
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

    except Exception as e:
        raise e
