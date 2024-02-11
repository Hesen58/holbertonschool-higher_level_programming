#!/usr/bin/python3
'''Something useful'''


def read_file(filename=""):
    '''Something more useful'''
    with open(filename) as f:
        zor = f.read()
    print(zor, end="")
