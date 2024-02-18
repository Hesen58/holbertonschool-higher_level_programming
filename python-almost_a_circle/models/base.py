#!/usr/bin/python3
'''Something useful'''
import json


class Base:
    '''Something more useful'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        zorname = cls.__name__
        if list_objs is None:
            zorjson = []
        else:
            zorjson = [obj.to_dictionary() for zor in list_objs]
        with open("{}.json".format(zorname), "w") as f:
            f.write(cls.to_json_string(zorjson))
