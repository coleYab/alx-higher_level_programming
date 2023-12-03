#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = []
    length = len(my_list)
    if (idx < 0 or idx >= length):
        return my_list
    for i in range(len(my_list)):
        if i != idx:
            list_new.append(my_list[i])
        else:
            my_list[idx] = element
    return my_list
