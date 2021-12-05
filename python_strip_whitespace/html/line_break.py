"""
This module adds line break to html_files
"""

import typing as t


def add_line_break(html: str, flavor: t.List) -> str:
    if "alpinejs" in flavor:
        from ..functions.regex import replace_regex
        from ..functions.regex_patterns.alpinejs import (
            # X pattern
            X_INIT_PATTERN,
            X_EFFECT_PATTERN,
            # Mouse Click Pattern
            CLICK_PATTERN,
            CLICK_PREVENT_PATTERN,
            CLICK_STOP_PATTERN,
            CLICK_OUTSIDE_PATTERN,
            CLICK_WINDOW_PATTERN,
            CLICK_ONCE_PATTERN,
            CLICK_DEBOUNCE_PATTERN,
            CLICK_THROTTLE_PATTERN,
            CLICK_SELF_PATTERN,
            CLICK_CAMEL_PATTERN,
            CLICK_DOT_PATTERN,
            CLICK_PASSIVE_PATTERN,
            # Mouse movement Pattern
            MOUSE_ENTER_PATTERN,
            MOUSE_LEAVE_PATTERN,
            MOUSE_OUT_PATTERN,
            MOUSE_OVER_PATTERN,
            MOUSE_UP_PATTERN,
            MOUSE_MOVE_PATTERN,
        )

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

    if "petitevue" in flavor:
        # We'll implement it later.
        pass

    # else:
    #     raise ValueError(
    #         f"""Error in python_strip_whitespace.html.line_break.
    #                 Current Flavor : { flavor }
    #                 It must be one of these :
    #                     |>  str("plain")
    #                     |>  str("alpinejs")
    #                     |>  str("petitevue")

    #                 Please change the value when calling add_line_break()"""
    #     )
    return html
