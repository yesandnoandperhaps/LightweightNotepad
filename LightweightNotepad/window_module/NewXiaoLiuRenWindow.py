import os
import re
from tkinter import messagebox

import ttkbootstrap as ttk

from function.JsonFile import File
from function.ProjectDictionaryVariables import XLR_DATA
from function.ProjectFunctions import window_init, window_closes
from function.ProjectPathVariables import DATA_FILE_PATH
from function.SolarTimeCalculator import SolarTimeCalculator
from function.XiaoLiuRenNum import XiaoLiuRenNum
from module.XiaoLiuRenJson import Calendar


class NewX:
    def __init__(self,root_main):
        self.result = None
        self.input_string = None
        self.xiao_liu_ren_result = None
        self.xlr_data_path = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
        xlr_json = File.dict_load(self.xlr_data_path, XLR_DATA)
        self.calendar = xlr_json[0]
        self.time = xlr_json[1]
        self.time_zone = xlr_json[2]
        self.function = xlr_json[3]
        self.shichen = xlr_json[4]
        self.runyue = xlr_json[5]
        self.suanfa = xlr_json[8]

        self.root_main = root_main

    def choose(self):
        time_dict = {
            0: self.time_zone_,
            1: self.flat_solar_time,
            2: self.true_solar_time
        }
        time_dict[self.time]()

        while self.result is None:
            self.root_main.update()

        g = {
            1: ("大安", "青龙木", "春季", "东", "寅卯", "事业宫"),
            2: ("流连", "四方土", "四季", "四角", "丑辰;未戍", "田宅宫"),
            3: ("速喜", "朱雀火", "夏季", "南", "巳午", "情感宫"),
            4: ("赤口", "白虎金", "秋季", "西", "申酉", "疾厄宫"),
            5: ("小吉", "玄武水", "冬季", "北", "亥子", "驿马宫"),
            0: ("空亡", "勾陈土", "不在四季", "央", "戊已", "福德宫")
        }

        # 从结果中解包
        t, r, d = self.result

        # 获取对应的元组
        t1, t2, t3, t4, t5, t6 = g[t]
        r1, r2, r3, r4, r5, r6 = g[r]
        d1, d2, d3, d4, d5, d6 = g[d]

        return t1, t2, t3, t4, t5, t6,\
                r1, r2, r3, r4, r5, r6,\
                d1, d2, d3, d4, d5, d6

    def time_zone_(self,shi=None):
        choose_dict = {
            0: self.time_qi_gua_(shi),
        }

        return choose_dict[self.function]

    def flat_solar_time(self):
        window = ttk.Toplevel(self.root_main)
        window_init(window, self.root_main, "平太阳时")
        window.resizable(False, False)
        text0 = ttk.Label(window,text="经度")
        entry0 = ttk.Entry(window)

        text0.grid(column=0, row=0, padx=5, pady=5)
        entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
        entry0.focus_set()
        entry0.bind('<Shift_R>', lambda event: self.flat_solar_judge_t(entry0.get(),window))
        entry0.bind('<Shift_L>', lambda event: self.flat_solar_judge_t(entry0.get(),window))


    def true_solar_time(self):
        pass

    def time_qi_gua_(self,shi=None):
        p0, p1, p2, p3 = self.time_qi_gua(shi)
        self.result = XiaoLiuRenNum(p1, p2, p3, self.suanfa).xiao_liu_ren_num()

    def time_qi_gua(self, shi=None):
        args = (self.calendar, self.shichen, self.runyue, shi) if shi is not None else (self.calendar, self.shichen, self.runyue)
        return Calendar(*args).function_selection()

    @staticmethod
    def solar_judge(input_string):
        return bool(re.match(r"^-?\d+(\.\d+)?$", input_string))

    def flat_solar_judge_t(self,input_string,window):
        tf = self.solar_judge(input_string)
        if tf:
            a = SolarTimeCalculator(float(input_string)).flat_solar_time()
            window_closes(window, self.root_main)
            self.time_zone_(a)
        else:
            messagebox.showerror("错误", message="请按以下格式输入：\n例1：\n经度：116.39\n例2：\n经度：-77.00941797699967", parent=window)