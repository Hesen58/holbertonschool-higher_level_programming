#!/usr/bin/python3
'''Something useful'''


class MyList(list):
    '''Something more useful'''
    def print_sorted(self):
        zor = self[:]
        print(zor.sort())
