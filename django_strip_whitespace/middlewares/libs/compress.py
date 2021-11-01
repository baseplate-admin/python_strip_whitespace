from minify_html import minify as rs_minifier
from ._html_minifier import html_minify as py_minifier
from ._decompress_gzip import decompress as gz_decompress
from ._decompress_brotli import decompress as br_decompress
from ._compress_brotli import compress as br_compress
from ._compress_gzip import compress as gz_compress
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

    first_iter = py_minifier(decompressed_buffer.decode(), comments=False)
    second_iter = rs_minifier(
        first_iter,
        minify_js=True,
        minify_css=True,
        # do_not_minify_doctype=True,
        # keep_html_and_head_opening_tags=True,
        # keep_closing_tags=True,
        remove_processing_instructions=True,
    )
    second_iter = second_iter.encode()

    if buffer_type == "gz":
        return_buffer = gz_compress(second_iter)
    elif buffer_type == "br":
        return_buffer = br_compress(second_iter)
    elif buffer_type == "plain":
        return_buffer = second_iter

    return return_buffer
