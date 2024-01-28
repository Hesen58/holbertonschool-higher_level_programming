#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    zor = my_list[0]
    for i in my_list:
        if i > zor:
            zor = i
    return zor
