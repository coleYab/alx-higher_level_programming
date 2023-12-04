#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = []
    length = len(my_list)
    for i in range(len(my_list)):
        if i != idx or idx < 0 or idx >= length:
            list_new.append(my_list[i])
        else:
            list_new.append(element)
    return list_new
