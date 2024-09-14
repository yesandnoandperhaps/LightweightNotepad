import os
from tkinter import messagebox
import ttkbootstrap as ttk

from function.ProjectVariables import DATA_FILE_PATH,ICON_PATH


class NewX:
    def __init__(self,root_main):
        self.w_4_1_path = os.path.join(DATA_FILE_PATH, "w_4_1_path")
        window = ttk.Toplevel(root_main)
        window.title("小六壬-起卦")
        window.iconbitmap(ICON_PATH)


    @staticmethod
    def down_box_save_1(w_4_1_path,down_box):
        with open(w_4_1_path, 'w', encoding='utf-8') as file:
            file.write(str(down_box.get()))

    @staticmethod
    def w_4_3_load(w_4_1_path):
        try:
            with open(w_4_1_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            pass
        except Exception as e:
            messagebox.showerror("错误", f"发生错误: {e}")