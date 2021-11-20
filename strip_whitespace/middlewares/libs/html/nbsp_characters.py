import re


def mangle_nbsp(html: str) -> str:
    # Using a foreign character so there's 0 chance of messing up the translation.
    html = html.replace("&nbsp;", "অ")
    return html


def unmangle_nbsp(html: str) -> str:
    # Using a foreign character so there's 0 chance of messing up the translation.
    html = html.replace("অ", "&nbsp;")
    return html
