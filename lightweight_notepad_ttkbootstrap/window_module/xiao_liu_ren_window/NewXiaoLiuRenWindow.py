import re
from tkinter import messagebox
import random
import re
from tkinter import messagebox

import ttkbootstrap as ttk

from function.DownBoxModify import DownBoxModify
from function.ProjectFunctions import window_init, window_closes
from function.XiaoLiuRenNum import XiaoLiuRenNum
from function.time.SolarTimeCalculator import SolarTimeCalculator
from function.variables.ProjectPathVariables import XLR_JSON, XLR_DATA_WU_XING_JI_LU_PATH, XLR_WU_XING_JI_LU_JSON, \
    XLR_WU_XING_JSON
from function.variables.ProjectDictionaryVariables import SI_XIANG_WU_XING, HOU_TIAN_WU_XING, DI_ZHI_DICT, ZHI_DICT_NUM, \
    ZAO_WAN_DI_ZHI_DICT, WAN_ZAO_DI_ZHI_DICT
from module.XiaoLiuRenDate import Calendar
from window_module.set_window.RandomNumbersWindow import RandomNumbersWindow


class NewX:
    def __init__(self,root_main):
        self.result = None
        self.input_string = None
        self.xiao_liu_ren_result = None
        self.calendar = XLR_JSON[0]
        self.time = XLR_JSON[1]
        self.time_zone = XLR_JSON[2]
        self.function = XLR_JSON[3]
        self.shichen = XLR_JSON[4]
        self.runyue = XLR_JSON[5]
        self.suanfa = XLR_JSON[8]
        self.shuzhi = XLR_JSON[9]
        self.shike = XLR_JSON[10]
        self.num_begin = XLR_JSON[11]
        self.num_end = XLR_JSON[12]
        self.num2_begin = XLR_JSON[13]
        self.num2_end = XLR_JSON[14]
        self.wu_xing_input = XLR_WU_XING_JSON[0]
        self.wu_xing_take_num = XLR_WU_XING_JSON[1]
        self.yin_yang = XLR_WU_XING_JSON[2]
        self.yin_yang_take_num_compute = XLR_WU_XING_JSON[3]
        self.yin_yang_take_num = XLR_WU_XING_JSON[4]
        self.wu_xing_take_num_compute_t = XLR_WU_XING_JSON[5]
        self.before_after_input = XLR_WU_XING_JSON[6]
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
        elif self.function == 4:
            return self.wu_xing_window()

        print(f"NewX:function {self.function}")

    def create_solar_time_window(self, title, judge_function,num,method=None,wu_time_list=None):
        window = ttk.Toplevel(self.root_main)
        window_init(window, self.root_main, title)
        window.resizable(False, False)

        text0 = ttk.Label(window, text="经度:")
        entry0 = ttk.Entry(window)

        text0.grid(column=0, row=0, padx=5, pady=5)
        entry0.grid(column=1, row=0, padx=5, pady=5, ipadx=20)
        entry0.focus_set()

        # 绑定 Shift 键事件
        entry0.bind('<Control_R>', lambda event: judge_function(entry0.get(), window,num,method,wu_time_list))
        entry0.bind('<Control_L>', lambda event: judge_function(entry0.get(), window,num,method,wu_time_list))

    def wu_xing_window(self):
        if self.wu_xing_input == 0:
            down_dox_values_group_main = []
            down_dox_group_main = []

            down_box_group_1 = ["金","木","水","火","土"]
            down_dox_values_group_main.append(down_box_group_1)

            window = ttk.Toplevel(self.root_main)
            window_init(window, self.root_main, "五行输入")
            window.resizable(False, False)

            text0 = ttk.Label(window, text="所算事五行:")
            down_box_1 = ttk.Combobox(master=window, values=down_box_group_1, state="readonly")
            down_box_1.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JI_LU_JSON,
                                                                                XLR_DATA_WU_XING_JI_LU_PATH,
                                                                                down_dox_values_group_main,
                                                                                down_dox_group_main)
                            .for_modify()
                            )
            down_box_1.bind("<Button-3>", lambda event: self.wu_xing(down_box_1.get(),window))
            down_dox_group_main.append(down_box_1)

            messagebox.showerror("错误", message=f"{XLR_WU_XING_JI_LU_JSON}", parent=window) if isinstance(XLR_WU_XING_JI_LU_JSON,
                                                                                                     Exception) else DownBoxModify(
                XLR_WU_XING_JI_LU_JSON,
                XLR_DATA_WU_XING_JI_LU_PATH,
                down_dox_values_group_main,
                down_dox_group_main).for_set()

            text0.grid(column=0, row=0, padx=5, pady=5)
            down_box_1.grid(row=0, column=1, padx=10, pady=10)


        elif self.wu_xing_num == 1:
            pass


    def flat_solar_time(self):
        self.create_solar_time_window("平太阳时", self.flat_solar_judge_t,0)

    def true_solar_time(self):
        self.create_solar_time_window("真太阳时", self.flat_solar_judge_t,1)

    def time_qi_gua_(self, shi=None):
        p0 = self.time_qi_gua(shi)
        print(f"time_qi_gua_ results: p0={p0}")  # Debug print
        self.result = XiaoLiuRenNum(p0[1], p0[2], p0[3][0],
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

    def flat_solar_judge_t(self,input_string,window,num=0,method=None,wu_time_list=None):
        tf = self.solar_judge(input_string)
        if tf:
            if num == 0:
                a = SolarTimeCalculator(float(input_string)).flat_solar_time()
                window_closes(window, self.root_main)
                if method is None:
                    self.time_zone_(a)
                else:
                    print("f")
                    wu_time_list.append(a)
                    method(wu_time_list)
            else:
                a = SolarTimeCalculator(float(input_string)).true_solar_time()
                window_closes(window, self.root_main)
                if method is None:
                    self.time_zone_(a)
                else:
                    print("f_")
                    wu_time_list.append(a)
                    method(wu_time_list)
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


    def wu_xing(self,wu,window):
        window_closes(window, self.root_main)
        wu_time_list = [wu]
        print(self.time)
        if self.time == 0:
            p0 = self.time_qi_gua()
            wu_time_list.append(p0[3][0])
            self.wu_xing_(wu_time_list)

        elif self.time == 1:
            self.create_solar_time_window(title="平太阳时", judge_function=self.flat_solar_judge_t,
                                          num=0,method=self.wu_xing_,
                                          wu_time_list=wu_time_list)
        elif self.time == 2:
            self.create_solar_time_window(title="真太阳时", judge_function=self.flat_solar_judge_t,
                                          num=1,method=self.wu_xing_,
                                          wu_time_list=wu_time_list)

    # noinspection PyUnboundLocalVariable
    def wu_xing_(self,wu_time_list):
        print(wu_time_list)
        if self.wu_xing_take_num == 0:
            p0 = HOU_TIAN_WU_XING[wu_time_list[0]]
            s0 = wu_time_list[1] if isinstance(wu_time_list[1], str) else self.time_qi_gua(wu_time_list[1])

            if isinstance(s0, str):
                dz_index = ZHI_DICT_NUM[s0[0]]
            else:
                dz_index = ZHI_DICT_NUM[s0[3][0]]

            d0 = DI_ZHI_DICT[dz_index]
            l0 = ZAO_WAN_DI_ZHI_DICT[dz_index]
            j0 = WAN_ZAO_DI_ZHI_DICT[dz_index]

            if self.yin_yang == 0:
                p_time = NewX.find(d0,self.yin_yang_take_num_compute,self.yin_yang_take_num,p0)
            elif self.yin_yang == 1:
                p_time = NewX.find(l0,self.yin_yang_take_num_compute,self.yin_yang_take_num,p0)
            elif self.yin_yang == 2:
                p_time = NewX.find(j0,self.yin_yang_take_num_compute,self.yin_yang_take_num,p0)
            elif self.yin_yang == 3:
                pass

            if self.wu_xing_take_num_compute_t == 0:
                num1,num2,num3 = RandomNumbersWindow.generate_numbers_small_p(p_time)
                self.result = XiaoLiuRenNum(month=num1, day=num2, hour=num3,
                                            shuzhi=self.shuzhi, method=self.suanfa).xiao_liu_ren_num()
            else:
                if self.before_after_input == 0:
                    num1,num2,num3 = RandomNumbersWindow(self.root_main,13,14,p_time).event0(1)
                    self.result = XiaoLiuRenNum(month=num1,day=num2,hour=num3,
                                                shuzhi=self.shuzhi, method=self.suanfa).xiao_liu_ren_num()
                elif self.before_after_input == 1:
                    num1,num2,num3 = RandomNumbersWindow.generate_numbers(self.num2_begin, self.num2_end,p_time)
                    self.result = XiaoLiuRenNum(month=num1, day=num2, hour=num3,
                                                shuzhi=self.shuzhi, method=self.suanfa).xiao_liu_ren_num()
        elif self.wu_xing_take_num == 1:
            pass
        elif self.wu_xing_take_num == 2:
            pass

    @staticmethod
    def find(look, compute, take, p0):
        p_time = None
        if compute == 0:
            if look[1] == "阳":
                if take == 0:
                    p_time = p0[0]
                elif take == 1:
                    p_time = p0[1]
            elif look[1] == "阴":
                if take == 0:
                    p_time = p0[1]
                elif take == 1:
                    p_time = p0[0]
        else:
            p_time = p0[0] + p0[1]
        return p_time