#!/usr/bin/python3
'''Something useful'''
import sys
import json
savejson = __import__('5-save_to_json_file').save_to_json_file
loadjson = __import__('6-load_from_json_file').load_from_json_file

try:
    zor = loadjson("add_item.json")
except Exception:
    zor = []
savejson(zor + sys.argv[1:], "add_item.json")
