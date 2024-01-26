#!/usr/bin/python3
def uppercase(strzor):
    for i in strzor:
        if ord(i) > 96 and ord(i) < 123:
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print()
