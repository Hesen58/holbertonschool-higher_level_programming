#!/usr/bin/python3
'''Something useful'''


def inherits_from(obj, a_class):
    '''Something more useful'''
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
