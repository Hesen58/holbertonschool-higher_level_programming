#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    zor = []
    for i in range(0, len(matrix)):
        zor.append([])
        for j in range(0, len(matrix[i])):
            zor[i].append(matrix[i][j] ** 2)
    return zor
