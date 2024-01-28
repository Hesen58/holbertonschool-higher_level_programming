#!/usr/bin/python3
def no_c(my_string):
    zor = ""
    for i in my_string:
        if i != "c" and i != "C":
            zor += i
    return zor
