


#!/usr/bin/python3
"""
Module to Divide a Matrix
"""
def matrix_divided(matrix, div):
    matrix_new = [row[:] for row in matrix]  # Create a new matrix with the same values as the original

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in range(len(matrix_new)):
        if not isinstance(matrix_new[row], list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        if len(matrix_new[row]) != len(matrix_new[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for colmun in range(len(matrix_new[row])):  # Fix the loop variable and iterate over the columns
            if (not isinstance(matrix_new[row][colmun], int)) and (not isinstance(matrix_new[row][colmun], float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            matrix_new[row][colmun] = matrix_new[row][colmun] / div

    return matrix_new



if __name__ == '__main__':
    try:
        print(matrix_divided([[12, 12, 21], [12, 12, 12]], 2))
    except Exception as E:
        print(E)
