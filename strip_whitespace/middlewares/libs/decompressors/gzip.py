import gzip

def decompress(buffer: bytes) -> str:
    try:
        return gzip.decompress(buffer)
    except Exception as e:
        raise e
