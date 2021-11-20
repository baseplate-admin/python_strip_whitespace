import re

NEW_LINE_REPLACE_PATTERN = re.compile(r"(?!^)(?<![{,])\n(?!^\s\S*$)")
