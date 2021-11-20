from django.conf import settings

#  Variables from settings.py.
#  Default Value of Everything is true.
#  Variables are copied from the source code.
#  https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs

STRIP_WHITESPACE_DO_NOT_MINIFY_DOCTYPE: bool = getattr(
    settings, "STRIP_WHITESPACE_DO_NOT_MINIFY_DOCTYPE", True
)

STRIP_WHITESPACE_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES: bool = getattr(
    settings, "STRIP_WHITESPACE_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES", True
)

STRIP_WHITESPACE_KEEP_CLOSING_TAGS: bool = getattr(
    settings, "STRIP_WHITESPACE_KEEP_CLOSING_TAGS", True
)


STRIP_WHITESPACE_KEEP_COMMENTS: bool = getattr(
    settings, "STRIP_WHITESPACE_KEEP_COMMENTS", True
)

STRIP_WHITESPACE_KEEP_HTML_AND_HEAD_OPENING_TAGS: bool = getattr(
    settings, "STRIP_WHITESPACE_KEEP_HTML_AND_HEAD_OPENING_TAGS", True
)

STRIP_WHITESPACE_KEEP_SPACES_BETWEEN_ATTRIBUTES: bool = getattr(
    settings, "STRIP_WHITESPACE_KEEP_SPACES_BETWEEN_ATTRIBUTES", True
)

STRIP_WHITESPACE_MINIFY_CSS: bool = getattr(
    settings, "STRIP_WHITESPACE_MINIFY_CSS", True
)

STRIP_WHITESPACE_MINIFY_JS: bool = getattr(settings, "STRIP_WHITESPACE_MINIFY_JS", True)

STRIP_WHITESPACE_REMOVE_BANGS: bool = getattr(
    settings, "STRIP_WHITESPACE_REMOVE_BANGS", True
)

STRIP_WHITESPACE_REMOVE_PROCESSING_INSTRUCTIONS: bool = getattr(
    settings, "STRIP_WHITESPACE_REMOVE_PROCESSING_INSTRUCTIONS", True
)
