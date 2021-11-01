from .html import html_minify as py_minifier
from minify_html import minify as rs_minifier

# Compressors
from .compressors import *

# Decompressors
from .decompressors import *

from ._guess_content_type import guess


def minify(buffer: bytes) -> str:
    buffer_type: str = guess(buffer).lower()
    decompressed_buffer: str = ""
    return_buffer: bytes = b""

    if buffer_type == "gz":
        decompressed_buffer = gz_decompress(buffer)
    elif buffer_type == "br":
        decompressed_buffer = br_decompress(buffer)
    elif buffer_type == "plain":
        decompressed_buffer = buffer

    first_iter = rs_minifier(
        decompressed_buffer.decode(),
        minify_js=True,
        minify_css=True,
        # do_not_minify_doctype=True,
        # keep_html_and_head_opening_tags=True,
        # keep_closing_tags=True,
        remove_processing_instructions=True,
    )
    last_iter = py_minifier(first_iter, comments=False)

    last_iter = last_iter.encode()

    if buffer_type == "gz":
        return_buffer = gz_compress(last_iter)
    elif buffer_type == "br":
        return_buffer = br_compress(last_iter)
    elif buffer_type == "plain":
        return_buffer = last_iter

    return return_buffer
