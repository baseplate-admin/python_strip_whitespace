import re

NEW_LINE_REPLACE_PATTERN = re.compile(
    r"(?!^)(?<![\s{,\"\`;])\n(?!^(\s\S*($|[\"\`)$]|)}))(?![\w\s]*[\)])"
)
