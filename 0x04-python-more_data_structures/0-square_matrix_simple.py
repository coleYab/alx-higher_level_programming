#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
	new_matrix = []
	for i in range(len(matrix)):
		new_matrix_new = []
		for j in range(len(matrix[i])):
			new_matrix_new.append(matrix[i][j] ** 2)
		new_matrix.append(new_matrix_new)
	return new_matrix
