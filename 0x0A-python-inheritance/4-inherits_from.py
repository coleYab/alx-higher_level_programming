#!/usr/bin/python3

def inherits_from(obj, a_class):
    temp = a_class()


    return (isinstance(obj, a_class) and  type(obj) != type(temp))

if __name__ == '__main__':
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

