import json
import os

class File:
    def __init__(self, file_dict, path = None):
        self.file_dict = file_dict
        self.path = path
        self.index_map = {i: key for i, key in enumerate(file_dict.keys())}

    def __getitem__(self, index):
        key = self.index_map.get(index)
        if key is not None:
            return self.file_dict.get(key)
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        key = self.index_map.get(index)
        if key is not None:
            self.file_dict[key] = value
        else:
            raise IndexError("Index out of range")

    @staticmethod
    def dict_save(path, file_dict):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(file_dict, file, indent=4)

    @staticmethod
    def dict_load(path, file_dict):
        if not os.path.exists(path):
            File.dict_save(path, file_dict)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    file_dict = json.load(file)
                return File(file_dict, path)
            except Exception as e:
                return e
        else:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    file_dict = json.load(file)
                return File(file_dict, path)
            except Exception as e:
                return e
