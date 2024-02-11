#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    """ the FileStorage class of the AirBnB Clone Project"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User}
    def __init__(self):
        """initiates file_storage class"""
        pass

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """A Public instance method that sets in the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        serialized_dict = {}
        for key, obj in FileStorage.__objects.items():
            serialized_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    obj = FileStorage.class_dict[obj_dict["__class__"]](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
