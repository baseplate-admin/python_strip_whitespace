import re

# X Pattern
X_INIT_PATTERN = re.compile(r"(?<=x-init=[\"\`])([^[\"\`\]]+)")
X_EFFECT_PATTERN = re.compile(r"(?<=x-effect=[\"\`])([^[\"\`\]]+)")

# Click Related Pattern.
# Mapped from => https://alpinejs.dev/directives/on#window
CLICK_PATTERN = re.compile(r"(?<=click=[\"\`])([^[\"\`\]]+)")
CLICK_PREVENT_PATTERN = re.compile(r"(?<=[click.prevent]=[\"\`])([^[\"\`\]]+)")
CLICK_STOP_PATTERN = re.compile(r"(?<=[click.stop]=[\"\`])([^[\"\`\]]+)")
CLICK_OUTSIDE_PATTERN = re.compile(r"(?<=[click.outside]=[\"\`])([^[\"\`\]]+)")
CLICK_WINDOW_PATTERN = re.compile(r"(?<=[click.window]=[\"\`])([^[\"\`\]]+)")
CLICK_ONCE_PATTERN = re.compile(r"(?<=[click.document]=[\"\`])([^[\"\`\]]+)")
CLICK_DEBOUNCE_PATTERN = re.compile(r"(?<=[click.debounce]=[\"\`])([^[\"\`\]]+)")
CLICK_THROTTLE_PATTERN = re.compile(r"(?<=[click.throttle]=[\"\`])([^[\"\`\]]+)")
CLICK_SELF_PATTERN = re.compile(r"(?<=[click.self]=[\"\`])([^[\"\`\]]+)")
CLICK_CAMEL_PATTERN = re.compile(r"(?<=[click.camel]=[\"\`])([^[\"\`\]]+)")
CLICK_DOT_PATTERN = re.compile(r"(?<=[click.dot]=[\"\`])([^[\"\`\]]+)")
CLICK_PASSIVE_PATTERN = re.compile(r"(?<=[click.passive]=[\"\`])([^[\"\`\]]+)")


# Mouse movement Pattern
# Mapped from => https://www.w3schools.com/jsref/obj_mouseevent.asp
MOUSE_ENTER_PATTERN = re.compile(r"(?<=mouseenter=[\"\`])([^[\"\`\]]+)")
MOUSE_LEAVE_PATTERN = re.compile(r"(?<=mouseleave=[\"\`])([^[\"\`\]]+)")
# MOUSE_CONTEXT_MENU_PATTERN = re.compile(r"(?<=mousecontextmenu=[\"\`])([^[\"\`\]]+)")
MOUSE_OUT_PATTERN = re.compile(r"(?<=mouseout=[\"\`])([^[\"\`\]]+)")
MOUSE_OVER_PATTERN = re.compile(r"(?<=mouseover=[\"\`])([^[\"\`\]]+)")
MOUSE_UP_PATTERN = re.compile(r"(?<=mouseup=[\"\`])([^[\"\`\]]+)")
MOUSE_MOVE_PATTERN = re.compile(r"(?<=mousemove=[\"\`])([^[\"\`\]]+)")
