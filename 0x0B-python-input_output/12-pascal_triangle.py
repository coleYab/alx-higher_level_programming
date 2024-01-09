#!/usr/bin/python3
"""Pascal triangle printing"""


def pascal_triangle(n):
    lists = []

    def factorial(num):
        return 1 if num == 0 else num * factorial(num - 1)

    if n <= 0:
        return lists
    for i in range(n):
        val = [int(factorial(i) / (factorial(j) * factorial(i - j))) for j in range(i + 1)]
        lists.append(val[:])

    return lists    
