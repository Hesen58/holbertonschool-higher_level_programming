#!/usr/bin/python3
'''Something useful'''
import json


def load_from_json_file(filename):
    '''Something more useful'''
    with open(filename, "r") as f:
        zor = json.load(filename)
    return zor
