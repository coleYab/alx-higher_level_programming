#!/usr/bin/python3
def best_score(a_dictionary):
    if None or a_dictionary == {}:
        return None
    maximum = -1213412
    key = ''
    for i, value in a_dictionary.items():
        if maximum < value:
            maximum = value
            key = i
    return key
