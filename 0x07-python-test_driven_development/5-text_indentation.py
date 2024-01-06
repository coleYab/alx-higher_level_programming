#!/usr/bin/python3

def text_indentation(text):
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
            