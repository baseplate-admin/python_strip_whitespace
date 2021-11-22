import gzip


def compress(string: bytes) -> bytes:
    try:
        return gzip.compress(string)
    except Exception as e:
        raise e
