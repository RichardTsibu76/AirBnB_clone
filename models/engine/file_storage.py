#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage():
    """ """
    def __init__(self):
        """initiates file_storage class

       Attributes:
       __filepath: private instance attribute
       __objects: private instance attribute
       """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """A Public instance method that sets in the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        serialized_dict = {}
        for key, obj in self.__objects.items():
            serialized_dict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
