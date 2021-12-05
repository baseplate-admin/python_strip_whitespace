from re import compile
from typing import Pattern

# X Pattern

X_INIT_PATTERN: Pattern = compile(r"(?<=x-init=[\"\`])([^[\"\`\]]+)")
X_EFFECT_PATTERN: Pattern = compile(r"(?<=x-effect=[\"\`])([^[\"\`\]]+)")

# Click Related Pattern.
# Mapped from => https://alpinejs.dev/directives/on#window

CLICK_PATTERN: Pattern = compile(r"(?<=click=[\"\`])([^[\"\`\]]+)")
CLICK_PREVENT_PATTERN: Pattern = compile(r"(?<=@click.prevent=[\"\`])([^[\"\`\]]+)")
CLICK_STOP_PATTERN: Pattern = compile(r"(?<=@click.stop=[\"\`])([^[\"\`\]]+)")
CLICK_OUTSIDE_PATTERN: Pattern = compile(r"(?<=@click.outside=[\"\`])([^[\"\`\]]+)")
CLICK_WINDOW_PATTERN: Pattern = compile(r"(?<=@click.window=[\"\`])([^[\"\`\]]+)")
CLICK_ONCE_PATTERN: Pattern = compile(r"(?<=@click.document=[\"\`])([^[\"\`\]]+)")
CLICK_DEBOUNCE_PATTERN: Pattern = compile(r"(?<=@click.debounce=[\"\`])([^[\"\`\]]+)")
CLICK_THROTTLE_PATTERN: Pattern = compile(r"(?<=@click.throttle=[\"\`])([^[\"\`\]]+)")
CLICK_SELF_PATTERN: Pattern = compile(r"(?<=@click.self=[\"\`])([^[\"\`\]]+)")
CLICK_CAMEL_PATTERN: Pattern = compile(r"(?<=@click.camel=[\"\`])([^[\"\`\]]+)")
CLICK_DOT_PATTERN: Pattern = compile(r"(?<=@click.dot=[\"\`])([^[\"\`\]]+)")
CLICK_PASSIVE_PATTERN: Pattern = compile(r"(?<=@click.passive=[\"\`])([^[\"\`\]]+)")


# Mouse movement Pattern
# Mapped from => https://www.w3schools.com/jsref/obj_mouseevent.asp

MOUSE_ENTER_PATTERN: Pattern = compile(r"(?<=mouseenter=[\"\`])([^[\"\`\]]+)")
MOUSE_LEAVE_PATTERN: Pattern = compile(r"(?<=mouseleave=[\"\`])([^[\"\`\]]+)")
# MOUSE_CONTEXT_MENU_PATTERN: Pattern = compile(r"(?<=mousecontextmenu=[\"\`])([^[\"\`\]]+)")
MOUSE_OUT_PATTERN: Pattern = compile(r"(?<=mouseout=[\"\`])([^[\"\`\]]+)")
MOUSE_OVER_PATTERN: Pattern = compile(r"(?<=mouseover=[\"\`])([^[\"\`\]]+)")
MOUSE_UP_PATTERN: Pattern = compile(r"(?<=mouseup=[\"\`])([^[\"\`\]]+)")
MOUSE_MOVE_PATTERN: Pattern = compile(r"(?<=mousemove=[\"\`])([^[\"\`\]]+)")
