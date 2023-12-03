#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('\n', end='')
    for i in range(len(matrix)):
        token = ' '
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                token = '\n'
            else:
                token = ' '
            print("{:d}".format(matrix[i][j]), end=token)
