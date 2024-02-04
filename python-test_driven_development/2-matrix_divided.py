#!/usr/bin/python3
'''Something useful'''

def matrix_divided(matrix, div):
    '''Something useful

    Args:
    matrix: Something more useful
    div: Something more useful
    '''
    zor = []
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        if not (len(matrix[i]) == len(matrix[i + 1])):
            raise TypeError("Each row of the matrix must have the same size")
        zor.append([])
        for node in matrix[i]:
            if not (isinstance(node, int) or isinstance(node, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            zor[i].append(round(node / div), 2)
    return zor
