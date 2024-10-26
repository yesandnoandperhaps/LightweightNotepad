import re
import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk

from LightweightNotepad.function import JsonFile
from LightweightNotepad.function.ProjectFunctions import window_init, window_closes
from LightweightNotepad.function.variables.ProjectPathVariables import XLR_DATA_PATH, XLR_JSON


class RandomNumbersWindow:
    def __init__(self,main_window):

       self.main_window = main_window

       window = ttk.Toplevel(str(main_window))
       window_init(window, main_window, "随机数范围")
       window.resizable(False, False)

       text0 = ttk.Label(window, text="始范围")
       text1 = ttk.Label(window, text="末范围")
       entry0 = ttk.Entry(window)
       entry1 = ttk.Entry(window)

       entry0.insert(tk.END, str([XLR_JSON[11]][0]))
       entry1.insert(tk.END, str([XLR_JSON[12]][0]))

       text0.grid(column=0, row=0, padx=5, pady=5)
       text1.grid(column=2, row=0, padx=5, pady=5)
       entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
       entry1.grid(column=3, row=0, padx=5, pady=5, ipadx=20)
       entry0.focus_set()

       # 绑定 Shift 键事件
       entry0.bind('<Shift_R>', lambda event: self.judge(entry0.get(), entry1.get(), window))
       entry1.bind('<Shift_R>', lambda event: self.judge(entry0.get(), entry1.get(), window))
       entry0.bind('<Return>', lambda event: entry1.focus_set())
       entry1.bind('<Return>', lambda event: entry0.focus_set())

    def judge(self,input_string,input_string_2,window):
        judge_of_bool = bool(re.match(r"^\d+(\.\d+)?$", input_string))
        judge_of_bool_2 = bool(re.match(r"^\d+(\.\d+)?$", input_string_2))
        if judge_of_bool and judge_of_bool_2:
            XLR_JSON[11] = float(input_string)
            XLR_JSON[12] = float(input_string_2)
            JsonFile.File.dict_save(XLR_DATA_PATH, XLR_JSON.file_dict)
            window_closes(window, self.main_window)
        else:
            messagebox.showerror("错误",
                                 message="请按以下格式输入：\n例1：\n始范围：1\n例2：\n末范围：9",
                                 parent=window)

