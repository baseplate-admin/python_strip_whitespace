# Minifiers
import typing as t

# 3rd party
from minify_html import minify as rust_minifier

from .html import (
    html_minify as python_minifier,
    mangle_nbsp,
    unmangle_nbsp,
)

# Guess the file content
from .functions import guess

# Import helper functions
from .html import add_line_break


def minify(
    buffer: bytes,
    # Rust
    STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES: t.Optional[
        bool
    ] = True,
    STRIP_WHITESPACE_RUST_KEEP_CLOSING_TAGS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_KEEP_COMMENTS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_KEEP_HTML_AND_HEAD_OPENING_TAGS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_KEEP_SPACES_BETWEEN_ATTRIBUTES: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_MINIFY_CSS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_MINIFY_JS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_REMOVE_BANGS: t.Optional[bool] = True,
    STRIP_WHITESPACE_RUST_REMOVE_PROCESSING_INSTRUCTIONS: t.Optional[bool] = True,
    # Python
    STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS: t.Optional[bool] = False,
    STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML: t.Optional[bool] = True,
    STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML: t.Optional[bool] = True,
    STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS: t.Optional[bool] = True,
    STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE: t.Optional[bool] = True,
    STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES: t.Optional[bool] = True,
    # NBSP character setting
    STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER: t.Optional[str] = "'অ'",
    # Compression Settings
    STRIP_WHITESPACE_COMPRESSION_TYPE: t.Optional[str] = str(
        "decompressed"  # Lets default to decompressed bytes
    ),
    STRIP_WHITESPACE_REGEX_FLAVOR: t.Optional[t.List] = [
        # str("alpinejs")  # Lets default it to alpinejs.
        "animejs",
        "alpinejs",
    ],
) -> bytes:
    #   Errors ⚠️
    #   Checked here ✔️ | ❌

    #   ❌ STRIP_WHITESPACE_COMPRESSION_TYPE is neither 'decompressed' nor 'compressed
    if str(STRIP_WHITESPACE_COMPRESSION_TYPE) not in [
        str("compressed"),
        str("decompressed"),
    ]:
        raise ValueError(
            f"""Error in python_strip_whitespace.compress

                    STRIP_WHITESPACE_COMPRESSION_TYPE is neither 'decompressed' nor 'compressed.
                    Please change the value when calling minify function.

                        Current Value : { str(STRIP_WHITESPACE_COMPRESSION_TYPE) }
                        It must be one of these :
                            |> str('compressed')
                            |> str('decompressed')"""
        )
    # ❌ STRIP_WHITESPACE_REGEX_FLAVOR is not defined in module
    # if str(STRIP_WHITESPACE_REGEX_FLAVOR) not in [
    #     str("plain"),
    #     str("alpinejs"),
    #     str("petitevue"),
    # ]:
    #     raise ValueError(
    #         f"""Error in python_strip_whitespace.compress

    #             STRIP_WHITESPACE_REGEX_FLAVOR is not defined.
    #             Please change the value when calling minify function.

    #                 Current Value : { str(STRIP_WHITESPACE_REGEX_FLAVOR) }
    #                 It must be one of these :
    #                     |>  str("plain")
    #                     |>  str("alpinejs")
    #                     |>  str("petitevue")"""
    #     )

    # Declare some variables here
    decompressed_buffer: bytes = b""
    return_buffer: bytes = b""

    # We check if the HTML that the server sent us is compressed or decompressed.
    # If the string is decompressed then just set buffer type to plain
    if STRIP_WHITESPACE_COMPRESSION_TYPE == str("compressed"):
        buffer_type: str = guess(buffer).lower()
    elif STRIP_WHITESPACE_COMPRESSION_TYPE == str("decompressed"):
        buffer_type: str = "plain"

    # If the buffer is not plain text, check for compression type.
    # But if the buffer is just plain text, don't do unnecessary checks.
    if buffer_type == "plain":
        decompressed_buffer = buffer

    elif buffer_type == "gzip":
        from .functions.decompressors.gzip import decompress as gz_decompress

        decompressed_buffer = gz_decompress(buffer)
    elif buffer_type == "br":
        from .functions.decompressors.brotli import decompress as br_decompress

        decompressed_buffer = br_decompress(buffer)
    elif buffer_type == "zstd":
        from .functions.decompressors.zstd import decompress as zstd_decompress

        decompressed_buffer = zstd_decompress(buffer)

    #   First change the &nbsp; into a special character so the other compressors cant mangle with that.
    first_iter: str = mangle_nbsp(
        decompressed_buffer.decode(),
        STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER,
    )

    #   Rust based minifier. The most powerful one in here. 💪
    second_iter: str = rust_minifier(
        first_iter,
        do_not_minify_doctype=STRIP_WHITESPACE_RUST_DO_NOT_MINIFY_DOCTYPE,
        ensure_spec_compliant_unquoted_attribute_values=STRIP_WHITESPACE_RUST_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES,
        keep_closing_tags=STRIP_WHITESPACE_RUST_KEEP_CLOSING_TAGS,
        keep_comments=STRIP_WHITESPACE_RUST_KEEP_COMMENTS,
        keep_html_and_head_opening_tags=STRIP_WHITESPACE_RUST_KEEP_HTML_AND_HEAD_OPENING_TAGS,
        keep_spaces_between_attributes=STRIP_WHITESPACE_RUST_KEEP_SPACES_BETWEEN_ATTRIBUTES,
        minify_css=STRIP_WHITESPACE_RUST_MINIFY_CSS,
        minify_js=STRIP_WHITESPACE_RUST_MINIFY_JS,
        remove_bangs=STRIP_WHITESPACE_RUST_REMOVE_BANGS,
        remove_processing_instructions=STRIP_WHITESPACE_RUST_REMOVE_PROCESSING_INSTRUCTIONS,
    )

    #   Rust minifier comes first to migrate some of the issues I faced.😛
    #   Specially the python module picks '\n in class=""
    #   So first remove all unnecessary whitespace before adding line_break
    third_iter: str = add_line_break(second_iter, STRIP_WHITESPACE_REGEX_FLAVOR)

    #   Finally the python iterator.
    #   I don't know how this works.🤷
    #   So adding it at last
    fourth_iter: str = python_minifier(
        third_iter,
        STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS,
        STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML,
        STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML,
        STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS,
        STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE,
        STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES,
    )

    #   Replace special character with &nbsp;
    last_iter: bytes = unmangle_nbsp(
        fourth_iter,
        STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER,
    ).encode()

    # Compress the buffer
    if buffer_type == "plain":
        return_buffer = last_iter

    elif buffer_type == "gzip":
        from .functions.compressors.gzip import compress as gz_compress

        return_buffer = gz_compress(last_iter)

    elif buffer_type == "br":
        from .functions.compressors.brotli import compress as br_compress

        return_buffer = br_compress(last_iter)

    elif buffer_type == "zstd":
        from .functions.compressors.zstd import compress as zstd_compress

        return_buffer = zstd_compress(last_iter)

    return return_buffer
