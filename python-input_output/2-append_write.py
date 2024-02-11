#!/usr/bin/python3
'''Something useful'''


def append_write(filename="", text=""):
    '''Something more useful'''
    with open(filename, "a") as f:
        zor = f.write(text)
    return zor
