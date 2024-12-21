import json
import os


class File:
    def __init__(self, file_dict, path=None):
        """
        初始化 File 类的实例。

        参数:
        - file_dict (dict): 存储文件数据的字典。
        - path (str): 文件路径，用于保存或加载文件，默认为 None。
        """
        self.file_dict = file_dict
        self.path = path
        self.index_map = {i: key for i, key in enumerate(file_dict.keys())}

    def __getitem__(self, index):
        """
        重载 [] 操作符，用于根据索引号获取字典的值。

        参数:
        - index (int): 索引号。

        返回:
        - 对应索引号的字典值。

        异常:
        - IndexError: 当索引超出范围时抛出。
        """
        key = self.index_map.get(index)
        if key is not None:
            return self.file_dict.get(key)
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        """
        重载 [] 操作符，用于根据索引号设置字典的值。

        参数:
        - index (int): 索引号。
        - value: 要设置的新值。

        异常:
        - IndexError: 当索引超出范围时抛出。
        """
        key = self.index_map.get(index)
        if key is not None:
            self.file_dict[key] = value
        else:
            raise IndexError("Index out of range")

    @staticmethod
    def dict_save(path, file_dict):
        """
        静态方法：将字典保存到指定路径的 JSON 文件中。

        参数:
        - path (str): 保存文件的路径。
        - file_dict (dict): 要保存的字典数据。
        """
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(file_dict, file, indent=4)

    @staticmethod
    def dict_load(path, file_dict):
        """
        静态方法：从指定路径加载字典文件。如果文件不存在，则创建一个新的文件并保存默认字典。

        参数:
        - path (str): 加载文件的路径。
        - file_dict (dict): 默认的字典数据，当文件不存在时用于初始化。

        返回:
        - File 类的实例，包含加载后的数据。
        - 如果出现错误，返回异常对象。
        """
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
