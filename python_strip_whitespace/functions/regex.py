import typing as t
from re import findall
from jsbeautifier import beautify

from .regex_patterns import NEW_LINE_REPLACE_PATTERN

JS_RESERVED_WORDS = [
    "try",
    "break",
    "finally",
    "switch",
    "typeof",
    "while",
]

JS_LINE_END_CHARACTER = [
    "})",  # For cases like this ({})
]


def replace_regex(RE_PATTERN: t.Pattern, html: str) -> str:
    regex_occurances: t.List = findall(RE_PATTERN, html)
    replaced_regex_occurances: t.List = []

    for i in JS_RESERVED_WORDS:
        html = html.replace(i, f";{i}")
        JS_RESERVED_WORDS.remove(i)

    for i in JS_LINE_END_CHARACTER:
        html = html.replace(i, f"{i};")

    for i in regex_occurances:
        minified_js = beautify(i)
        replaced_regex_occurances.append(minified_js)

    for i in replaced_regex_occurances:
        index = replaced_regex_occurances.index(i)
        previous_content = regex_occurances[index]

        html = html.replace(previous_content, i)

    return html
