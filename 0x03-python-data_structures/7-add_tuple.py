#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, c, d = 0, 0, 0, 0
    if (len(tuple_a) >= 2):
        a, b = tuple_a
    else if (len(tuple_a) == 1):
        a = tuple_a[0]
    if (len(tuple_b) >= 0):
        c, d = tuple_b
    else if (len(tuple_b) == 1):
        c = tuple_b[0]

    return (a + c, b + d)
