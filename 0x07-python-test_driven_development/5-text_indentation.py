#!/usr/bin/python3
"""# text indentation
a module to indent a text by the signs
"""


def text_indentation(text):
    """# text indetation
    This is the function that is its thing"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text2 = ''
    for i in text:
        if i not in ".?:":
            text2 += i
        else:
            text2 += i
            print(text2.strip(), end="\n\n")
            text2 = ''

    if text2 != '':
        print(text2.strip(), end='')
