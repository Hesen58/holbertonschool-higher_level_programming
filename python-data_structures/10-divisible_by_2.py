#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    zor = []
    for i in my_list:
        if i % 2 == 0:
            zor.append(True)
        else:
            zor.append(False)
    return zor
