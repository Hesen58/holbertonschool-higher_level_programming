#!/usr/bin/python3
'''Something useful'''


class Mylist(list):
    '''Something more useful'''
    def print_sorted(self):
        zor = self[:]
        print(zor.sort())
