#!/usr/bin/python3
"""FileStorage Module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """FileStorage Class Implementation"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            objs_to_write = {}
            for obj_key in self.__objects.keys():
                objs_to_write[obj_key] = self.__objects[obj_key].to_dict()
            file.write(json.dumps(objs_to_write))

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                objects = json.loads(file.read())
                if not len(objects):
                    return
                for key in objects.keys():
                    attribs = objects[key].copy()
                    cls = attribs.pop("__class__", None)
                    self.new(eval(cls)(**attribs))
        except FileNotFoundError:
            return
