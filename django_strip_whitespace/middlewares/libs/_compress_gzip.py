import gzip


def compress(string: str) -> bytes:
    try:
        return gzip.compress(string)
    except Exception as e:
        raise e
