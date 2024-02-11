#!/usr/bin/python3
'''Something useful'''


def write_file(filename="", text=""):
    '''Something more useful'''
    with open(filename, "w") as f:
        zor = f.write(text)
    return zor
