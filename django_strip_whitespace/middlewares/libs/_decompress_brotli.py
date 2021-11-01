import brotli


def decompress(buffer: bytes) -> str:
    try:
        return brotli.decompress(buffer)
    except Exception as e:
        raise e
