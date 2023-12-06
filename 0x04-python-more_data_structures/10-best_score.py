#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    maximum = -1213412
    for i, value in a_dictionary.items():
        if maximum < value:
            maximum = value
    return i
