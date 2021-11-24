from typing import Optional


def mangle_nbsp(
    html: str,
    STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER: Optional[str],
) -> str:
    html = html.replace("&nbsp;", STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER)
 
    return html


def unmangle_nbsp(
    html: str,
    STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER: Optional[str],
) -> str:
    html = html.replace(STRIP_WHITESPACE_NBSP_MANGLE_CHARACTER, "&nbsp;")
    
    return html
