#!/usr/bin/python3
"""Module for FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of objects optionally filtered by class."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes JSON file to objects."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method to deserialize JSON file to objects."""
        self.reload()

