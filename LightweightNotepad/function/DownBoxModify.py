from function import JsonFile
class DownBoxModify:
    def __init__(self,json,json_path,down_dox_values_group,down_dox_group):
        self.json = json
        self.json_path = json_path
        self.num = len(down_dox_values_group)
        self.down_dox_values_group = down_dox_values_group
        self.down_box_group = down_dox_group

    def for_modify(self):
        for i in range(self.num):
            self.json[i] = self.down_dox_values_group[i].index(self.down_box_group[i].get())

        JsonFile.File.dict_save(self.json_path, self.json.file_dict)

    def for_set(self):
        for i in range(self.num):
            self.down_box_group[i].set(self.down_dox_values_group[i][self.json[i]])