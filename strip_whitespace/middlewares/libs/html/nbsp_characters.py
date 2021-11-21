import re
from django.conf import settings

STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER: str = getattr(
    settings, "STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER", "'অ'"
)


def mangle_nbsp(html: str) -> str:
    # Using a foreign character so there's 0 chance of messing up the translation.
    html = html.replace("&nbsp;", STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER)
    return html


def unmangle_nbsp(html: str) -> str:
    # Using a foreign character so there's 0 chance of messing up the translation.
    html = html.replace(STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER, "&nbsp;")
    return html
