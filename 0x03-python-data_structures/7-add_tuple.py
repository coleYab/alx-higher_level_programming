#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	a = 0
	for i in range(2):
		if i + 1 > len(tuple_a):
			a = tuple_a[i]
			