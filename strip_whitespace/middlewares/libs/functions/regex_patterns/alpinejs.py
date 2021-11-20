import re

# X Pattern
X_INIT_PATTERN = re.compile(r"(?<=x-init=[\"\`])([^[\"\`\]]+)")
X_EFFECT_PATTERN = re.compile(r"(?<=x-effect=[\"\`])([^[\"\`\]]+)")

# Click Related Pattern
CLICK_PATTERN = re.compile(r"(?<=@click=[\"\`])([^[\"\`\]]+)")
CLICK_PREVENT_PATTERN = re.compile(r"(?<=[@click.prevent]=[\"\`])([^[\"\`\]]+)")

# Mouse movement Pattern
MOUSE_ENTER_PATTERN = re.compile(r"(?<=@mouseenter=[\"\`])([^[\"\`\]]+)")
MOUSE_LEAVE_PATTERN = re.compile(r"(?<=@mouseleave=[\"\`])([^[\"\`\]]+)")
