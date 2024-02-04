#!/usr/bin/python3
'''Something useful'''

def add_integer(a, b=98):
    '''Something more useful

    Args:
    a: Something much more useful
    b: Something much more useful
    '''
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
