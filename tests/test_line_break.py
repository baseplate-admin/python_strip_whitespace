from python_strip_whitespace.functions.regex_patterns import NEW_LINE_REPLACE_PATTERN
from re import sub

JS = """
() => {
    switch (button_turned) {
        case true : {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 0,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 1 ,
                scale: 1
            })
            break
        }
        case false: {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 40 * 2,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 0,
                scale: 0.2
            })
            break
        }
    }
}
"""
EXPECTED_JS = '''
() => {
    switch (button_turned) {
        case true : {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 0,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 1 ,
                scale: 1            });            break;        };        case false: {
            anime({
                targets: '.animejs__facebook__button',
                translateX: 40 * 2,
                easing: 'easeOutSine',
                duration: 150,
                opacity: 0,
                scale: 0.2            });            break;        };    };};
'''
def func() -> str:
    return sub(NEW_LINE_REPLACE_PATTERN,';', JS)


def test_line_break():
    assert func() == EXPECTED_JS
    
