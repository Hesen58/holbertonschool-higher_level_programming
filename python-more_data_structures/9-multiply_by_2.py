#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    zor = {}
    for i in a_dictionary:
        zor.update({i: (a_dictionary[i] * 2)})
    return zor
