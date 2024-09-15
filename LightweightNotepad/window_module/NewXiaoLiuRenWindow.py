import os
from tkinter import messagebox
import ttkbootstrap as ttk
from function.JsonFile import File
from function.ProjectPathVariables import DATA_FILE_PATH,ICON_PATH
from function.ProjectDictionaryVariables import XLR_DATA


class NewX:
    def __init__(self,root_main):
        self.xlr_data_path = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
        xlr_json = File.dict_load(self.xlr_data_path, XLR_DATA)
        window = ttk.Toplevel(root_main)
        window.title("小六壬-起卦")
        window.iconbitmap(ICON_PATH)