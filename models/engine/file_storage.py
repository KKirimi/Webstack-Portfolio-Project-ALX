#!/usr/bin/python3
<<<<<<< HEAD
import json
import os
import self
import models


class FileStorage:
    """Serializes instances to a JSOn file
    and deserializes Json file to instances
    """


__file_path = "file.json"
__objects = {}


def all():
    """Returns the dictionary_objects"""
    return self.__objects


def new(obj):
    """Sets in __objects the obj with key <obj class name>.id
    :rtype: object
    """


key = "{}.{}".format(obj.__class__.__name__, obj.id)
self.__objects[key] = __objects


def save():
    """Serializes __objects to the JSON file (path: __file_path)."""


serialized_objects = {}
for key, obj in self.__objects.items():
    serialized_objects[key] = obj.to_dict()
    with open(self.__file_path, 'w') as file:
        json.dump(serialized_objects, file)


def reload():
    """Deserializes the JSON file to __objects
    (only if the JSON file (__file_path) exists;
      otherwise, do nothing. If the file does not exist,
      no exception should be raised).
      """
    if os.path.exists(self.__file_path):
        with open(self.__file_path, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
            module = __import__('models')
            class_ = getattr(module, class_name)
            instance = class_(**value)
            self.__objects[key] = instance
=======

"""
Defines the FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in obj with key."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file path."""
        save_dict = {}
        for key, obj in self.__objects.items():
            save_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(save_dict, file)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to __objects.
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(cls.__file_path, "r", encoding="utf-8") as file:
                dict_to_obj = json.load(file)
                for key, value in dict_to_obj.items():
                    class_name = value['__class__']
                    cls_to_ins = classes.get(class_name)
                    if cls_to_ins:
                        obj = cls_to_ins(**value)
                        cls.__objects[key] = obj
        except FileNotFoundError:
            pass
>>>>>>> ccc0d1c6b2deb7c2cff24f19deddd62a4bd5e1ff
