"""
This module adds line break to html_files

"""
from ..functions.regex import replace_regex
from ..functions.regex_patterns import *


def add_line_break(html: str) -> str:
    html = replace_regex(X_INIT_PATTERN, html)
    html = replace_regex(X_EFFECT_PATTERN, html)

    # Mouse Click Pattern
    html = replace_regex(CLICK_PATTERN, html)
    html = replace_regex(CLICK_PREVENT_PATTERN, html)
    html = replace_regex(CLICK_STOP_PATTERN, html)
    html = replace_regex(CLICK_OUTSIDE_PATTERN, html)
    html = replace_regex(CLICK_WINDOW_PATTERN, html)
    html = replace_regex(CLICK_ONCE_PATTERN, html)
    html = replace_regex(CLICK_DEBOUNCE_PATTERN, html)
    html = replace_regex(CLICK_THROTTLE_PATTERN, html)
    html = replace_regex(CLICK_SELF_PATTERN, html)
    html = replace_regex(CLICK_CAMEL_PATTERN, html)
    html = replace_regex(CLICK_DOT_PATTERN, html)
    html = replace_regex(CLICK_PASSIVE_PATTERN, html)

    # Mouse movement Pattern
    html = replace_regex(MOUSE_ENTER_PATTERN, html)
    html = replace_regex(MOUSE_LEAVE_PATTERN, html)
    html = replace_regex(MOUSE_OUT_PATTERN, html)
    html = replace_regex(MOUSE_OVER_PATTERN, html)
    html = replace_regex(MOUSE_UP_PATTERN, html)
    html = replace_regex(MOUSE_MOVE_PATTERN, html)
    return html
