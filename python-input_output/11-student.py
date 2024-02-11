#!/usr/bin/python3
'''Something useful'''


class Student:
    '''Something more useful'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        zor = {}
        zorkeys = list(self.__dict__.keys())
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            for i in attrs:
                for j in zorkeys:
                    if i == j:
                        zor[i] = self.__dict__[j]
            return zor
        else:
            return self.__dict__

    def reload_from_json(self, json):
        try:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
        except KeyError:
            pass
