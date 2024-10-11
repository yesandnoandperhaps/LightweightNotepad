import os
import re
from tkinter import messagebox
import random

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
        self.shuzhi = xlr_json[9]
        self.shike = xlr_json[10]
        self.num_begin = xlr_json[11]
        self.num_end = xlr_json[12]
        self.root_main = root_main

    def choose(self):
        time_dict = {
            0: self.time_zone_,
            1: self.flat_solar_time,
            2: self.true_solar_time
        }

        (time_dict[self.time]() if self.function in (0, 1) else time_dict[0]())

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
        # noinspection PyTupleAssignmentBalance
        t, r, d = self.result

        # 获取对应的元组
        t1, t2, t3, t4, t5, t6 = g[t]
        r1, r2, r3, r4, r5, r6 = g[r]
        d1, d2, d3, d4, d5, d6 = g[d]

        return t1, t2, t3, t4, t5, t6,\
                r1, r2, r3, r4, r5, r6,\
                d1, d2, d3, d4, d5, d6

    def time_zone_(self,shi=None):
        if self.function == 0:
            return self.time_qi_gua_(shi)
        elif self.function == 1:
            return self.time_qi_gua_2_(shi)
        elif self.function == 2:
            return self.average_random_number()
        elif self.function == 3:
            return self.random_number()

        print(f"NewX:function {self.function}")

    def create_solar_time_window(self, title, judge_function,num):
        window = ttk.Toplevel(self.root_main)
        window_init(window, self.root_main, title)
        window.resizable(False, False)

        text0 = ttk.Label(window, text="经度")
        entry0 = ttk.Entry(window)

        text0.grid(column=0, row=0, padx=5, pady=5)
        entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
        entry0.focus_set()

        # 绑定 Shift 键事件
        entry0.bind('<Shift_R>', lambda event: judge_function(entry0.get(), window,num))
        entry0.bind('<Shift_L>', lambda event: judge_function(entry0.get(), window,num))

    def flat_solar_time(self):
        self.create_solar_time_window("平太阳时", self.flat_solar_judge_t,0)

    def true_solar_time(self):
        self.create_solar_time_window("真太阳时", self.flat_solar_judge_t,1)

    def time_qi_gua_(self, shi=None):
        p0 = self.time_qi_gua(shi)
        print(f"time_qi_gua_ results: p0={p0}")  # Debug print
        self.result = XiaoLiuRenNum(p0[1], p0[2], p0[3],
                                    self.shuzhi, method=self.suanfa).xiao_liu_ren_num()

    def time_qi_gua_2_(self, shi=None):
        p0 = self.time_qi_gua_2(shi)
        print(f"time_qi_gua_2_ results: p0={p0}")  # Debug print
        self.result = XiaoLiuRenNum(p0[1], p0[2], p0[3],
                                    self.shuzhi, method=self.suanfa).xiao_liu_ren_num()

    def time_qi_gua_2(self, shi=None):
        args = (self.calendar, self.shichen,
                self.runyue, shi,self.shike,1) if shi is not None else (
        self.calendar, self.shichen,
        self.runyue,None,self.shike,1)
        return Calendar(*args).function_selection()

    def time_qi_gua(self, shi=None):
        args = (self.calendar, self.shichen,
                self.runyue, shi,self.shike,0) if shi is not None else (
            self.calendar, self.shichen,
            self.runyue,None,self.shike,0)
        return Calendar(*args).function_selection()

    @staticmethod
    def solar_judge(input_string):
        return bool(re.match(r"^-?\d+(\.\d+)?$", input_string))

    def flat_solar_judge_t(self,input_string,window,num=0):
        tf = self.solar_judge(input_string)
        if tf:
            if num == 0:
                a = SolarTimeCalculator(float(input_string)).flat_solar_time()
                window_closes(window, self.root_main)
                self.time_zone_(a)
            else:
                a = SolarTimeCalculator(float(input_string)).true_solar_time()
                window_closes(window, self.root_main)
                self.time_zone_(a)
        else:
            messagebox.showerror("错误", message="请按以下格式输入：\n例1：\n经度：116.39\n例2：\n经度：-77.00941797699967", parent=window)

    def average_random_number(self):
        new_num1 = round(random.uniform(0, 5))
        new_num2 = round(random.uniform(0, 5))
        new_num3 = round(random.uniform(0, 5))
        self.result = XiaoLiuRenNum(new_num1,new_num2,new_num3,
                                    self.shuzhi, method=self.suanfa).xiao_liu_ren_num()

    def random_number(self):
        new_num1 = round(random.uniform(self.num_begin, self.num_end))
        new_num2 = round(random.uniform(self.num_begin, self.num_end))
        new_num3 = round(random.uniform(self.num_begin, self.num_end))
        self.result = XiaoLiuRenNum(new_num1, new_num2, new_num3,
                                    self.shuzhi, method=self.suanfa).xiao_liu_ren_num()

