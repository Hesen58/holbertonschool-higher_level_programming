#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    zor = []
    for i in range(len(my_list)):
        zor.append(my_list[i])
    zor[idx] = element
    return zor
