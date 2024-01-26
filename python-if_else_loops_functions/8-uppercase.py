#!/usr/bin/python3
def uppercase(strzor):
    zor = ""
    for i in strzor:
        if ord(i) > 96 and ord(i) < 123:
            zor += chr(ord(i) - 32)
        else:
            zor += i
    print("{}".format(zor))
