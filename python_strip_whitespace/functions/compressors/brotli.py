try:
    import brotli
except ImportError:
    raise ImportError(
        """
        Did you install this module using:
            python -m pip install python_strip_whitespace[brotli]

        
        If not then please use these commands to uninstall and reinstall:
            python -m pip uninstall python_strip_whitespace
            python -m pip install python_strip_whitespace[brotli]


        Or just install Brotli Module module:
            CPython:
                python -m pip install brotli
            PyPy:
                python -m pip install brotlipy
        """
    )


def compress(string: bytes) -> bytes:
    try:
        return brotli.compress(string)
    except Exception as e:
        raise e
