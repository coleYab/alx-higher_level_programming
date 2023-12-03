#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print('')
    list_size = len(my_list) - 1
    for i in range(list_size, -1, -1):
        print("{:d}".format(my_list[i]))
