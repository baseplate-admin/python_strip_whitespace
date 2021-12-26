import typing as t
from re import findall
import minify_html


JS_RESERVED_WORDS_BEFORE: t.List = [
    "try",
    "break",
    "finally",
    "switch",
    "typeof",
    "while",
    "await",
    "continue",
    "anime({",
]

JS_RESERVED_WORDS_AFTER: t.List = [
    "})",
]


def replace_regex(RE_PATTERN: t.Pattern, html: str) -> str:
    regex_occurances: t.List = findall(RE_PATTERN, html)
    replaced_regex_occurances: t.List = []

    for i in JS_RESERVED_WORDS_BEFORE:
        JS_RESERVED_WORDS_BEFORE.remove(i)
        html = html.replace(i, f";{i}")

    for i in JS_RESERVED_WORDS_AFTER:
        JS_RESERVED_WORDS_AFTER.remove(i)
        html = html.replace(i, f"{i};")

    for i in regex_occurances:
        minified_js = minify_html.minify(
            i,
            minify_js=True,
        )
        replaced_regex_occurances.append(minified_js)

    for i in regex_occurances:
        regex_index = regex_occurances.index(i)
        replaced_regex_content = replaced_regex_occurances[regex_index]

        html = html.replace(i, replaced_regex_content)

    return html
