#!/bin/python3
def best_score(a_dictionary):
    maximum = -1213412
    for i, value in a_dictionary.items():
        if maximum < value:
            maximum = value
    return maximum
