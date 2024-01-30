#!/usr/bin/python3
def search_replace(my_list, search, replace):
    zor = []
    for i in my_list:
        if (i == search):
            zor.append(replace)
        else:
            zor.append(i)
    return zor
