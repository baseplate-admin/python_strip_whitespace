try:
    import brotli
except ImportError:
    raise ImportError(
        """
        Did you install this module using:
            python -m pip install django_strip_whitespace[brotli]

        
        If not then please use these commands to uninstall and reinstall:
            python -m pip uninstall django_strip_whitespace
            python -m pip install django_strip_whitespace[brotli]


        Or just install ZSTD module:
            CPython:
                python -m pip install brotli
            PyPy:
                python -m pip install brotlipy
        """
    )


def decompress(buffer: bytes) -> str:
    try:
        return brotli.decompress(buffer)
    except Exception as e:
        raise e
