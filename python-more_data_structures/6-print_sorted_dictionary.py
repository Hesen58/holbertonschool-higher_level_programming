#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    zor = sorted(a_dictionary.items())
    for i in zor:
        print("{}: {}".format(i[0], i[1]))
