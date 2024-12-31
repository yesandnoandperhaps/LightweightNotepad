import re
import tkinter as tk
from tkinter import messagebox
import random
import ttkbootstrap as ttk

from function import JsonFile
from function.ProjectFunctions import window_init, window_closes
from function.variables.ProjectPathVariables import XLR_DATA_PATH, XLR_JSON


class RandomNumbersWindow:
    def __init__(self,main_window,num1=None,num2=None,p_time=None):

       self.result_num = None
       self.main_window = main_window
       self.p_time = p_time

       if num1 is None and num2 is None:
           self.num1 = 11
           self.num2 = 12
       else:
           self.num1 = num1
           self.num2 = num2

       self.window = ttk.Toplevel(str(main_window))
       window_init(self.window, main_window, "随机数范围")
       self.window.resizable(False, False)

       self.text0 = ttk.Label(self.window, text="始范围:")
       self.text1 = ttk.Label(self.window, text="末范围:")
       self.entry0 = ttk.Entry(self.window)
       self.entry1 = ttk.Entry(self.window)

       self.entry0.insert(tk.END, str([XLR_JSON[self.num1]][0]))
       self.entry1.insert(tk.END, str([XLR_JSON[self.num2]][0]))

       self.text0.grid(column=0, row=0, padx=5, pady=5)
       self.text1.grid(column=2, row=0, padx=5, pady=5)
       self.entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
       self.entry1.grid(column=3, row=0, padx=5, pady=5, ipadx=20)
       self.entry0.focus_set()

    def event0(self,num=None):
        self.entry0.bind('<Control_R>', lambda event: self.judge(self.entry0.get(), self.entry1.get(), self.window,num,self.p_time))
        self.entry1.bind('<Control_R>', lambda event: self.judge(self.entry0.get(), self.entry1.get(), self.window,num,self.p_time))
        self.entry0.bind('<KeyRelease>',
                         lambda event: self.judge(self.entry0.get(), self.entry1.get(), self.window, num, self.p_time))
        self.entry1.bind('<KeyRelease>',
                         lambda event: self.judge(self.entry0.get(), self.entry1.get(), self.window, num, self.p_time))
        self.entry0.bind('<Return>', lambda event: self.entry1.focus_set())
        self.entry1.bind('<Return>', lambda event: self.entry0.focus_set())

        if num is None:
            pass
        else:
            while self.result_num is None:
                self.main_window.update()
                if self.result_num is not None:
                    return self.result_num

        self.window.mainloop()

    def judge(self,input_string,input_string_2,window,num=None,p_time=None):
        if num is None:
            if p_time is None:
                judge_of_bool = bool(re.match(r"^\d+(\.\d+)?$", input_string))
                judge_of_bool_2 = bool(re.match(r"^\d+(\.\d+)?$", input_string_2))
                input_string_0 = float(input_string)
                input_string_1 = float(input_string_2)
            else:
                judge_of_bool = bool(re.match(r"^\d+$", input_string))
                judge_of_bool_2 = bool(re.match(r"^\d+$", input_string_2))
                input_string_0 = int(input_string)
                input_string_1 = int(input_string_2)

            if judge_of_bool and judge_of_bool_2:
                XLR_JSON[self.num1] = input_string_0
                XLR_JSON[self.num2] = input_string_1
                JsonFile.File.dict_save(XLR_DATA_PATH, XLR_JSON.file_dict)
                window_closes(window, self.main_window)
            else:
                messagebox.showerror("错误",
                                     message="请按以下格式输入：\n例1：\n始范围：1\n例2：\n末范围：9",
                                     parent=window)
        elif num == 1:
            judge_of_bool = bool(re.match(r"^\d+$", input_string))
            judge_of_bool_2 = bool(re.match(r"^\d+$", input_string_2))
            if judge_of_bool and judge_of_bool_2:
                XLR_JSON[self.num1] = int(input_string)
                XLR_JSON[self.num2] = int(input_string_2)
                JsonFile.File.dict_save(XLR_DATA_PATH, XLR_JSON.file_dict)
                self.result_num = self.generate_numbers(XLR_JSON[self.num1],XLR_JSON[self.num2],p_time)
                window_closes(window, self.main_window)
            else:
                messagebox.showerror("错误",
                                     message="请按以下格式输入：\n例1：\n始范围：1\n例2：\n末范围：9\n只能输入整数",
                                     parent=window)


    @staticmethod
    def generate_numbers(a, b, p):
        num1 = random.randint(a, b)
        num2 = random.randint(a, b - num1)
        num3 = p - num1 - num2
        return num1, num2, num3

    @staticmethod
    def generate_numbers_small_p(p):
        a = random.randint(0, p)
        b = random.randint(0, p - a)
        c = p - a - b
        return a, b, c
