import gzip


def decompress(buffer: bytes) -> str:
    return gzip.decompress(buffer)
