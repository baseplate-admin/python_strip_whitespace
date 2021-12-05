import typing as t
from re import compile


ANIMEJS_REGEX_PATTERN: t.Pattern = compile("anime[(]{[\w\W]*}[)]")
