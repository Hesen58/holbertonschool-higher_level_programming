#!/usr/bin/python3
'''Something useful'''
import json


def save_to_json_file(my_obj, filename):
    '''Something more useful'''
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
