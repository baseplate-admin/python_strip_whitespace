"""
This module adds line break to html_files

"""
from ..functions.regex import replace_regex
from ..functions.regex_patterns import (
    X_INIT_PATTERN,
    X_EFFECT_PATTERN,
    CLICK_PATTERN,
    MOUSE_ENTER_PATTERN,
    MOUSE_LEAVE_PATTERN,
    CLICK_PREVENT_PATTERN,
)


def add_line_break(html: str) -> str:
    html = replace_regex(X_INIT_PATTERN, html)
    html = replace_regex(X_EFFECT_PATTERN, html)
    html = replace_regex(CLICK_PATTERN, html)
    html = replace_regex(MOUSE_ENTER_PATTERN, html)
    html = replace_regex(MOUSE_LEAVE_PATTERN, html)
    html = replace_regex(CLICK_PREVENT_PATTERN, html)

    return html
