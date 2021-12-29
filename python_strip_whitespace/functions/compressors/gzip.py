import gzip


def compress(string: bytes) -> bytes:
    return gzip.compress(string)
