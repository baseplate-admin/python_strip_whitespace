import brotli


def compress(string: str) -> bytes:
    try:
        return brotli.compress(string)
    except Exception as e:
        raise e
