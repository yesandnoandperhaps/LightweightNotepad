import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from function.ProjectFunctions import t_load
from function.variables.ProjectPathVariables import ICON_PATH, Q_PATH
from module import XiaoLiuRen


class JiZhiWindow:
    def __init__(self, root_main, font_style):
        self.text1 = None
        self.entry1 = None
        self.text2 = None
        self.text = None
        self.entry2 = None
        self.entry = None
        self.window = None
        self.xiao_liu_ren_list = ["大安", "速喜", "小吉", "流连", "赤口", "空亡"]
        self.result = None
        self.root_main = root_main
        self.font_style = font_style

    def create_window(self):
        self.window = ttk.Toplevel(self.root_main)
        self.window.title("小六壬")

        self.entry = tk.Entry(self.window, font=self.font_style)
        self.entry1 = tk.Entry(self.window, font=self.font_style)
        self.entry2 = tk.Entry(self.window, font=self.font_style)
        self.text = ttk.Label(self.window, text="天宫", font=self.font_style)
        self.text1 = ttk.Label(self.window, text="人宫", font=self.font_style)
        self.text2 = ttk.Label(self.window, text="地宫", font=self.font_style)

        self.text.grid(column=0, row=0, padx=5, pady=5)
        self.text1.grid(column=1, row=0, padx=5, pady=5)
        self.text2.grid(column=2, row=0, padx=5, pady=5)
        self.entry.grid(column=0, row=1, padx=5, pady=5)
        self.entry1.grid(column=1, row=1, padx=5, pady=5)
        self.entry2.grid(column=2, row=1, padx=5, pady=5)

        self.entry.focus_set()
        self.entry.bind('<Return>', lambda event: self.entry1.focus_set())
        self.entry1.bind('<Return>', lambda event: self.entry2.focus_set())
        self.entry2.bind('<Return>', lambda event: self.entry.focus_set())
        self.entry.bind('<Control_R>', lambda event: self.judgement())
        self.entry1.bind('<Control_R>', lambda event: self.judgement())
        self.entry2.bind('<Control_R>', lambda event: self.judgement())
        self.entry.bind('<Control_L>', lambda event: self.window.destroy())
        self.entry1.bind('<Control_L>', lambda event: self.window.destroy())
        self.entry2.bind('<Control_L>', lambda event: self.window.destroy())

        self.window.wait_window()
        return self.result

    def judgement(self):
        if (
                self.entry.get() in self.xiao_liu_ren_list
                and self.entry1.get() in self.xiao_liu_ren_list
                and self.entry2.get() in self.xiao_liu_ren_list
        ):
            g = {"大安": 1, "流连": 2, "速喜": 3, "赤口": 4, "小吉": 5, "空亡": 0}
            loop_t_rule_num2 = int(t_load(Q_PATH) or 2)
            if loop_t_rule_num2 == 1:
                self.result = XiaoLiuRen.numgua2_1(g[self.entry.get()], g[self.entry1.get()], g[self.entry2.get()])
            elif loop_t_rule_num2 == 2:
                self.result = XiaoLiuRen.numgua2_2(g[self.entry.get()], g[self.entry1.get()], g[self.entry2.get()])
            elif loop_t_rule_num2 == 0:
                self.result = XiaoLiuRen.numgua2_0(g[self.entry.get()], g[self.entry1.get()], g[self.entry2.get()])
            self.window.destroy()
        else:
            messagebox.showerror(
                "错误",
                message="请按以下格式输入：\n例：天宫：大安\n人宫：流连\n地宫：速喜\n只可输入：大安,速喜,小吉,流连,赤口,空亡",
                parent=self.window,
            )