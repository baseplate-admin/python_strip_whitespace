"""
    HTML Minifier functions for CSS-HTML-JS-Minify.
        Source : https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py
        License : https://github.com/juancarlospaco/css-html-js-minify/blob/master/LICENSE.gpl.txt
            Rewritten By : Baseplate-Admin (https://github.com/baseplate-admin/)
"""
import re
import typing as t


def condense_html_whitespace(html: str) -> str:
    """Condense HTML, but be safe first if it have textareas or pre tags.

    >>> condense_html_whitespace('<i>  <b>    <a> test </a>    </b> </i><br>')
    '<i><b><a> test </a></b></i><br>'
    """  # first space between tags, then empty new lines and in-between.
    tagsStack: t.List = []

    split: t.List = re.split(
        "(<\\s*pre.*>|<\\s*/\\s*pre\\s*>|<\\s*textarea.*>|<\\s*/\\s*textarea\\s*>)",
        html,
        flags=re.IGNORECASE,
    )

    for i in range(0, len(split)):
        # if we are on a tag
        if (i + 1) % 2 == 0:
            tag: str = rawtag(split[i])

            if tag.startswith("/"):
                if not tagsStack or "/" + tagsStack.pop() != tag:
                    raise Exception("Some tag is not closed properly")

            else:
                tagsStack.append(tag)

            continue

        # else check if we are outside any nested <pre>/<textarea> tag
        if not tagsStack:

            temp: str = re.sub(r">\s+<", "> <", split[i])
            split[i] = re.sub(r"\s{2,}|[\r\n]", " ", temp)

    return "".join(split)


def rawtag(string: str) -> str:
    if re.match("<\\s*pre.*>", string, flags=re.IGNORECASE):
        return "pre"

    if re.match("<\\s*textarea.*>", string, flags=re.IGNORECASE):
        return "txt"

    if re.match("<\\s*/\\s*pre\\s*>", string, flags=re.IGNORECASE):
        return "/pre"

    if re.match("<\\s*/\\s*textarea\\s*>", string, flags=re.IGNORECASE):
        return "/txt"


def condense_style(html: str) -> str:
    """Condense style html tags.

    >>> condense_style('<style type="text/css">*{border:0}</style><p>a b c')
    '<style>*{border:0}</style><p>a b c'
    """  # May look silly but Emmet does this and is wrong.
    return (
        html.replace('<style type="text/css">', "<style>")
        .replace("<style type='text/css'>", "<style>")
        .replace("<style type=text/css>", "<style>")
    )


def condense_script(html: str) -> str:
    """Condense script html tags.

    >>> condense_script('<script type="text/javascript"> </script><p>a b c')
    '<script> </script><p>a b c'
    """  # May look silly but Emmet does this and is wrong.
    return (
        html.replace('<script type="text/javascript">', "<script>")
        .replace("<style type='text/javascript'>", "<script>")
        .replace("<style type=text/javascript>", "<script>")
    )


def clean_unneeded_html_tags(html: str) -> str:
    """Clean unneeded t.Optional html tags."""
    tags_to_remove: t.List = [
        "</area>",
        "</base>",
        "</col>",
        "</colgroup>",
        "</img>",
        "</input>",
        "</link>",
        "</meta>",
    ]

    for i in tags_to_remove:
        html = html.replace(i, "")

    return html


def remove_html_comments(html: str) -> str:
    """Remove all HTML comments, Keep all for Grunt, Grymt and IE.

    >>> _="<!-- build:dev -->a<!-- endbuild -->b<!--[if IE 7]>c<![endif]--> "
    >>> _+= "<!-- kill me please -->keep" ; remove_html_comments(_)
    '<!-- build:dev -->a<!-- endbuild -->b<!--[if IE 7]>c<![endif]--> keep'
    """  # Grunt uses comments to as build arguments, bad practice but still.
    return re.compile(r"<!-- .*? -->", re.I).sub("", html)


def unquote_html_attributes(html: str) -> str:
    """Remove all HTML quotes on attibutes if possible.

    >>> unquote_html_attributes('<img   width="9" height="5" data-foo="0"  >')
    '<img width=9 height=5 data-foo=0 >'
    """  # data-foo=0> might cause errors on IE, we leave 1 space data-foo=0 >
    # cache all regular expressions on variables before we enter the for loop.
    any_tag: re.Pattern = re.compile(r"<\w.*?>", re.I | re.MULTILINE | re.DOTALL)
    space: re.Pattern = re.compile(r" \s+|\s +", re.MULTILINE)
    space1: re.Pattern = re.compile(r"\w\s+\w", re.MULTILINE)
    space2: re.Pattern = re.compile(r'"\s+>', re.MULTILINE)
    space3: re.Pattern = re.compile(r"'\s+>", re.MULTILINE)
    space4: re.Pattern = re.compile(
        "\"\s\s+\w+=\"|'\s\s+\w+='|\"\s\s+\w+=|'\s\s+\w+=", re.MULTILINE
    )
    space6: re.Pattern = re.compile(r"\d\s+>", re.MULTILINE)
    quotes_in_tag: re.Pattern = re.compile('([a-zA-Z]+)="([a-zA-Z0-9-_\.]+)"')

    # iterate on a for loop cleaning stuff up on the html markup.
    for tag in iter(any_tag.findall(html)):
        # exceptions of comments and closing tags
        if tag.startswith("<!") or tag.find("</") > -1:
            continue
        original = tag

        # remove white space inside the tag itself
        tag = space2.sub('" >', tag)  # preserve 1 white space is safer
        tag = space3.sub("' >", tag)

        for each in space1.findall(tag) + space6.findall(tag):
            tag = tag.replace(each, space.sub(" ", each))
        for each in space4.findall(tag):
            tag = tag.replace(each, each[0] + " " + each[1:].lstrip())

        # remove quotes on some attributes
        tag = quotes_in_tag.sub(r"\1=\2 ", tag)  # See Bug #28

        if original != tag:  # has the tag been improved ?
            html = html.replace(original, tag)

    return html.strip()


def html_minify(
    html: str,
    STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS: t.Optional[bool],
    STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML: t.Optional[bool],
    STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML: t.Optional[bool],
    STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS: t.Optional[bool],
    STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE: t.Optional[bool],
    STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES: t.Optional[bool],
) -> str:
    """Minify HTML main function.

    >>> html_minify(' <p  width="9" height="5"  > <!-- a --> b </p> c <br> ')
    '<p width=9 height=5 > b c <br>'
    """
    if STRIP_WHITESPACE_PYTHON_REMOVE_COMMENTS:
        html = remove_html_comments(html)

    if STRIP_WHITESPACE_PYTHON_CONDENSE_STYLE_FROM_HTML:
        html = condense_style(html)

    if STRIP_WHITESPACE_PYTHON_CONDENSE_SCRIPT_FROM_HTML:
        html = condense_script(html)

    if STRIP_WHITESPACE_PYTHON_CLEAN_UNNEEDED_HTML_TAGS:
        html = clean_unneeded_html_tags(html)

    if STRIP_WHITESPACE_PYTHON_CONDENSE_HTML_WHITESPACE:
        html = condense_html_whitespace(html)

    if STRIP_WHITESPACE_PYTHON_UNQUOTE_HTML_ATTRIBUTES:
        html = unquote_html_attributes(html)

    return html.strip()
