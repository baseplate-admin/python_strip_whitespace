import re
from typing import List
from .regex_patterns import NEW_LINE_REPLACE_PATTERN


def replace_regex(RE_PATTERN: re.Pattern, html: str) -> str:
    regex_occurances: List = re.findall(RE_PATTERN, html)
    replaced_regex_occurances: List = []

    for i in regex_occurances:
        substituated_regex = re.sub(NEW_LINE_REPLACE_PATTERN, r";", i)
        replaced_regex_occurances.append(substituated_regex)

    for i in regex_occurances:
        regex_index = regex_occurances.index(i)
        replaced_regex_content = replaced_regex_occurances[regex_index]

        html = html.replace(i, replaced_regex_content)

    return html
