#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    zorkey = list(a_dictionary.keys())
    zorval = list(a_dictionary.values())[0]
    hoqqa = zorkey[0]
    for i in a_dictionary:
        if a_dictionary[i] > zorval:
            zorval = a_dictionary[i]
            hoqqa = i
    return hoqqa
