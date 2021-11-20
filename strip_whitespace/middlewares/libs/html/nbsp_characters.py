import re


def mangle_nbsp(html: str) -> str:
    return re.sub("&nbsp;", "mangled_nbsp", html)


def unmangle_nbsp(html: str) -> str:
    return re.sub("mangled_nbsp", "&nbsp;", html)
