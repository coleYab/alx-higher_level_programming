#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    index = len(my_string)
    for i in range(index):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += my_string[i]

    return new_str
