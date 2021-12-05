import minify_html
import typing as t
from re import findall

from .regex_patterns import NEW_LINE_REPLACE_PATTERN


def replace_regex(RE_PATTERN: t.Pattern, html: str) -> str:
    regex_occurances: t.List = findall(RE_PATTERN, html)
    replaced_regex_occurances: t.List = []

    for i in regex_occurances:
        minified_js = minify_html.minify(
            i,
            minify_js=True,
        )
        replaced_regex_occurances.append(minified_js)

    for i in replaced_regex_occurances:
        index = replaced_regex_occurances.index(i)
        previous_content = regex_occurances[index]

        html = html.replace(previous_content, i)

    return html
