#!/usr/bin/python3
"""Pascal triangle printing"""


def pascal_triangle(n):
    """Prints the pascal triangle"""
    lists = []

    def fact(num):
        """Calculates the fact of nums"""
        return 1 if num == 0 else num * fact(num - 1)

    if n <= 0:
        return lists
    for i in range(n):
        val = [
            int(fact(i) / (fact(j) * fact(i - j))) for j in range(i + 1)
        ]
        lists.append(val[:])

    return lists
