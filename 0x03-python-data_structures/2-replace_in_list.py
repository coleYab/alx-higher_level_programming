#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	list_size = len(mylist)
	if list_size <= idx or idx < 0:
		return my_list
	else:
		my_list[idx] = element
	return my_list
