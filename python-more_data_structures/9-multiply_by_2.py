#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    zor = {}
    for i in a_dictionary:
        zor.update({i[0]: (int(i[1]) ** 2)})
    return zor
