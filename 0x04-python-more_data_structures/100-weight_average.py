#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    items = 0
    for i in my_list:
        sum += i[0] * i[1]
        items += i[1]
    return sum / items if len(my_list) != 0 else 0
