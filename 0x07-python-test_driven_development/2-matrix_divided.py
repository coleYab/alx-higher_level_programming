#!/usr/bin/python3

def matrix_divided(matrix, div):
    matrix_new = []
    
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for row in range(len(matrix)):
        n_row = []
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(matrix[row], list):
            raise TypeError(msg)
        for colmun in range(len(matrix[row])):
            if (not isinstance(matrix[row][colmun], int)) and (not isinstance(matrix[row][colmun], float)):
                raise TypeError(msg)
            n_row.append(round(matrix[row][colmun] / div, 2))
            
        matrix_new.append(n_row[:])
        
        
    return (matrix_new)