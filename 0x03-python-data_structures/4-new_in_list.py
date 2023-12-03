#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = []
    length = len(my_list)
    if (idx >= length):
        return my_list
    else:
        for i in range(len(my_list)):
            if i != idx or idx < 0:
                list_new.append(my_list[i])
            else:
                my_list[idx] = element
    return my_list
