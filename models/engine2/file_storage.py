#!/usr/bin/env python3
"""Serialization and deserialize """

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        key = f"{obj.__class__.__name__}.{obj.id}"

    def save(self):
        new_dict = {}

        for k, v in FileStorage.__objects.items():
            new_dict[k] = v

            with open(FileStorage.__file_path, "w") as x:
                json.dump(new_dict, x)

    def reload(self):
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as x:
                json_data = json.load(x)
                for k, v in json_data.items():
                    obj[k] = BaseModel(**v)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
