import os
import re
from tkinter import messagebox

import ttkbootstrap as ttk

from function.ProjectFunctions import window_init
from function.JsonFile import File
from function.ProjectDictionaryVariables import XLR_DATA
from function.ProjectPathVariables import DATA_FILE_PATH, ICON_PATH
from module.XiaoLiuRenJson import Calendar
from function.SolarTimeCalculator import SolarTimeCalculator


class NewX:
    def __init__(self,root_main):
        self.input_string = None
        self.xlr_data_path = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
        xlr_json = File.dict_load(self.xlr_data_path, XLR_DATA)
        self.calendar = xlr_json[0]
        self.time = xlr_json[1]
        self.time_zone = xlr_json[2]
        self.function = xlr_json[3]
        self.shichen = xlr_json[4]
        self.runyue = xlr_json[5]

        self.root_main = root_main


    def choose(self):

        time_dict = {
            0:self.time_zone,
            1:self.flat_solar_time,
            2:self.true_solar_time
        }
        time_dict[self.time]()

    def time_zone(self):
        choose_dict = {
            0: self.time_qi_gua,
        }

        choose_dict[self.function]()

    def flat_solar_time(self):
        window = ttk.Toplevel(self.root_main)
        window_init(window, self.root_main, "平太阳时")
        window.resizable(False, False)
        text0 = ttk.Label(window,text="经度")
        entry0 = ttk.Entry(window)

        text0.grid(column=0, row=0, padx=5, pady=5)
        entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
        entry0.focus_set()
        entry0.bind('<Shift_R>', lambda event: self.flat_solar_judge_t(entry0.get(),window,0))
        entry0.bind('<Shift_L>', lambda event: self.flat_solar_judge_t(entry0.get(),window,1))


    def true_solar_time(self):
        pass

    def time_qi_gua(self):
        p = Calendar(self.calendar,self.shichen,self.runyue)

        p0,p1,p2,p3 = p.function_selection()

    @staticmethod
    def solar_judge(input_string):
        return bool(re.match(r"^-?\d+(\.\d+)?$", input_string))

    def flat_solar_judge_t(self,input_string,window,num):
        tf = self.solar_judge(input_string)
        if tf:
            if num == 0:
                a = SolarTimeCalculator(float(input_string))
                print(a.flat_solar_time())
            elif num == 1:
                pass
        else:
            messagebox.showerror("错误", message="请按以下格式输入：\n例1：\n经度：116.39\n例2：\n经度：-77.00941797699967", parent=window)