#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    zor = list(a_dictionary.values())[0]
    for i in a_dictionary:
        if a_dictionary[i] > zor:
            zor = a_dictionary[i]
    return zor
