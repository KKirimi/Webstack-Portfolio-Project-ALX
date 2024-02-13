#!/usr/bin/python3
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
