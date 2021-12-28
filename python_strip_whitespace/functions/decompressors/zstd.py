try:
    import zstd
except ImportError:
    raise ImportError(
        """
        Did you install this module using:
            python -m pip install python_strip_whitespace[zstd]

        
        If not then please use these commands to uninstall and reinstall:
            python -m pip uninstall python_strip_whitespace
            python -m pip install python_strip_whitespace[zstd]


        Or just install ZSTD module:
            python -m pip install zstd
        """
    )


def decompress(buffer: bytes) -> str:
    return zstd.decompress(buffer)
