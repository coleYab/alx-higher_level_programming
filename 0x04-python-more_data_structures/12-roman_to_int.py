#!/usr/bin/python3
def roman_to_int(string):
    integer = 0
    index = len(string)
    string = string.lower()
    roman_val = {'i': [1, 0], 'm': [1000, 0], 'd': [500, 0],
                 'l': [50, 0], 'x': [10, 0], 'v': [5, 0], 'c': [100, 0]}
    rep_3 = 'ixcm'
    if (len(string) == 0):
        return 0
    if string[len(string) - 2:] == 'iv':
        integer += 4
        index -= 2
        roman_val['i'][1] += 1
        roman_val['v'][1] += 1
    elif string[len(string) - 2:] == 'ix':
        integer += 9
        index -= 2
        roman_val['i'][1] += 1
        roman_val['x'][1] += 1
    for i in range(index):
        if string[i] in roman_val.keys():
            integer += roman_val[string[i]][0]
            roman_val[string[i]][1] += 1
        else:
            return 0
    for i, v in roman_val.items():
        if i in rep_3:
            if v[1] > 3:
                return 0
        else:
            if v[1] > 1:
                return 0
    return integer if integer >= 1 and integer <= 3999 else 0
