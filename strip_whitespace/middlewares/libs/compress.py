# Minifiers
from minify_html import minify as rust_minifier
from .html import html_minify as python_minifier

# Compressors
from .compressors import *

# Decompressors
from .decompressors import *

# Guess the file content
from .content import guess

# Import bindings
from .variables import *


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

    first_iter = rust_minifier(
        decompressed_buffer.decode(),
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
    last_iter = python_minifier(first_iter)
    last_iter = last_iter.encode()

    if buffer_type == "gz":
        return_buffer = gz_compress(last_iter)
    elif buffer_type == "br":
        return_buffer = br_compress(last_iter)
    elif buffer_type == "plain":
        return_buffer = last_iter

    return return_buffer
