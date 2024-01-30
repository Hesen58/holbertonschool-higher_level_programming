#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    zor = [[]]
    for i in range(0, len(matrix)):
        for j in range(0, matrix[i]):
            zor[i][j] = matrix[i][j] ** 2
    return zor
