#!/usr/bin/python3
'''Something useful'''


def pascal_triangle(n):
    '''Something more useful'''
    zor = []
    if n <= 0:
        return zor
    zor.append([1])
    zor.append([1, 1])
    for i in range(2, n):
        zor.append([])
        zor[i].append(1)
        for j in range(i - 1):
            zor[i].append(zor[i - 1][j] + zor[i - 1][j + 1])
        zor[i].append(1)
