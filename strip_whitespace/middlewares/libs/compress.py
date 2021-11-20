# Minifiers
from minify_html import minify as rust_minifier

from .html import (
    html_minify as python_minifier,
    mangle_nbsp,
    unmangle_nbsp,
)


# Guess the file content
from .functions import guess

# Import bindings
from .functions.rust_variables import *

# Import helper functions
from .html import add_line_break


def minify(buffer: bytes) -> str:
    buffer_type: str = guess(buffer).lower()
    decompressed_buffer: str = ""
    return_buffer: bytes = b""

    if buffer_type == "gz":
        from .functions.decompressors import gz_decompress

        decompressed_buffer = gz_decompress(buffer)

    elif buffer_type == "br":
        from .functions.decompressors import br_decompress

        decompressed_buffer = br_decompress(buffer)

    elif buffer_type == "zstd":
        from .functions.decompressors import zstd_decompress

        decompressed_buffer = zstd_decompress(buffer)

    elif buffer_type == "plain":
        decompressed_buffer = buffer

    first_iter = mangle_nbsp(decompressed_buffer.decode())

    second_iter = rust_minifier(
        first_iter,
        do_not_minify_doctype=STRIP_WHITESPACE_DO_NOT_MINIFY_DOCTYPE,
        ensure_spec_compliant_unquoted_attribute_values=STRIP_WHITESPACE_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES,
        keep_closing_tags=STRIP_WHITESPACE_KEEP_CLOSING_TAGS,
        keep_comments=STRIP_WHITESPACE_KEEP_COMMENTS,
        keep_html_and_head_opening_tags=STRIP_WHITESPACE_KEEP_HTML_AND_HEAD_OPENING_TAGS,
        keep_spaces_between_attributes=STRIP_WHITESPACE_KEEP_SPACES_BETWEEN_ATTRIBUTES,
        minify_css=STRIP_WHITESPACE_MINIFY_CSS,
        minify_js=STRIP_WHITESPACE_MINIFY_JS,
        remove_bangs=STRIP_WHITESPACE_REMOVE_BANGS,
        remove_processing_instructions=STRIP_WHITESPACE_REMOVE_PROCESSING_INSTRUCTIONS,
    )

    third_iter = add_line_break(second_iter)
    fourth_iter = python_minifier(third_iter)

    last_iter = unmangle_nbsp(fourth_iter)
    last_iter = last_iter.encode()

    # Decompress
    if buffer_type == "gz":
        from .functions.compressors import gz_compress

        return_buffer = gz_compress(last_iter)

    elif buffer_type == "br":
        from .functions.compressors import br_compress

        return_buffer = br_compress(last_iter)

    elif buffer_type == "zstd":
        from .functions.compressors import zstd_compress

        return_buffer = zstd_compress(last_iter)

    elif buffer_type == "plain":
        return_buffer = last_iter

    return return_buffer
