#!/usr/bin/python3
def uniq_add(my_list=[]):
    zor = 0
    zorset = set(my_list)
    for i in zorset:
        zor += i
    return zor
