#!/usr/bin/python3
'''Something useful'''
import sys, json
savejson = __import__('5-save_to_json_file').save_to_json_file
loadjson = __import__('6-load_from_json_file').load_from_json_file


zor = loadjson("add_item.json")
if not zor:
    zor == []
savejson(zor + sys.argv[1:], "add_item.json")
