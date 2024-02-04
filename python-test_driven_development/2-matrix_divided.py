#!/usr/bin/python3
'''Something useful'''

def matrix_divided(matrix, div):
    '''Something useful

    Args:
    matrix: Something more useful
    div: Something more useful
    '''
    zor = []
    zori = 0
    oldrow = matrxi[0]
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
            if not (len(oldrow) == len(row)):
                raise TypeError("Each row of the matrix must have the same size")
        zor.append([])
        for node in row:
            oldrow = row
            if not (isinstance(node, int) or isinstance(node, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            zor[zori].append(round(node / div, 2))
            zori += 1
    return zor
