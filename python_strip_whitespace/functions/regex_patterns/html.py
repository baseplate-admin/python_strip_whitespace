import re
from typing import Pattern

NEW_LINE_REPLACE_PATTERN: Pattern = re.compile(
    r"(?!^)(?<![\s{,\"\`;])\n(?!^(\s\S*($|[\"\`)$]|)}))(?![\w\s]*[\)])"
)
