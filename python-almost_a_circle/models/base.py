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
            zorjson = [zor.to_dictionary() for zor in list_objs]
        with open("{}.json".format(zorname), "w") as f:
            f.write(cls.to_json_string(zorjson))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        zorname = cls.__name__
        if zorname == "Square":
            zordummy = cls(31)
        elif zorname == "Rectangle":
            zordummy = cls(31, 32)
        zordummy.update(**dictionary)
        return zordummy

    @classmethod
    def load_from_file(cls):
        zorfile = "{}.json".format(cls.__name__)
        try:
            with open(zorfile, "r") as f:
                zordict = cls.from_json_string(f.read())
            zorlist = [cls.create(**zor) for zor in zordict]
            return zorlist
