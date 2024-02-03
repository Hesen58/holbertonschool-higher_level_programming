#!/usr/bin/pyhton3
def safe_print_list(my_list=[], x=0):
    zor = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            zor += 1
        except IndexError:
            break
    print()
    return zor
