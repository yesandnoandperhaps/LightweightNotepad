import datetime
import re
import tkinter as tk
import datetime
from tkinter import messagebox

import ttkbootstrap as ttk

from function.ProjectFunctions import t_load
from function.variables.ProjectPathVariables import R_PATH, ICON_PATH
from function.variables.ProjectDictionaryVariables import ZHI_DICT_NUM
from module.ZiWeiDouShu import ZiWeiDouShu

class GridLabelText:
    def __init__(self):
        self.positions = {}
    

    def grid_label_text(self, name, label_text,row, column,frame_window):
        while (row, column,frame_window) in self.positions:
            print(f"位置 ({row}, {column},{frame_window}) 已被 {self.positions[(row, column,frame_window)]} 占用，尝试下一个位置.")
            column += 1

        label_text.grid(row=row, column=column)
        self.positions[(row, column,frame_window)] = name
        print(f"{name} 被放置在位置 ({row}, {column},{frame_window})") 

    @staticmethod
    def get_window(label_text):
        return label_text.nametowidget(label_text.winfo_parent())
    
    @staticmethod
    def get_no_name(class_name,name_window,name_list_label,font_style,num0,num1):
        for window, text in zip(name_window, name_list_label):
            label = ttk.Label(window, text=text, font=font_style)
            class_name.grid_label_text(text, label, num0, num1,GridLabelText.get_window(label))

    @staticmethod
    def accumulate_vector(initial_vector, increment=10, times=11, reverse_result=False):
        result = []
        vector = initial_vector[:]
        
        for _ in range(times):
            vector = [x + increment for x in vector]
            result.append(f"{vector[0]}-{vector[1]}")
        
        # 根据参数选择是否翻转结果
        if reverse_result:
            result.reverse()
        
        return [f"{initial_vector[0]}-{initial_vector[1]}"] + result



class ZiWeiDouShuWindow:
    def __init__(self,root_main,font_style):
        t = str(t_load(R_PATH) or "横排样式")
        self.font_style = font_style
        match t:

            case "横排样式":
                window = ttk.Toplevel(str(root_main))
                window.title("紫微斗数")
                window.iconbitmap(ICON_PATH)
                text1 = tk.Label(window,text="年:")
                text1.grid(column=0,row=0,padx=5,pady=5)
                text2 = tk.Label(window,text="月:")
                text2.grid(column=2,row=0,padx=5,pady=5)
                text3 = tk.Label(window,text="日:")
                text3.grid(column=4,row=0,padx=5,pady=5)
                text4 = tk.Label(window,text="时:")
                text4.grid(column=6,row=0,padx=5,pady=5)
                text5 = tk.Label(window,text="性别:")
                text5.grid(column=8,row=0,padx=5,pady=5)
                entry1 = tk.Entry(window)
                entry1.grid(column=1,row=0,padx=5,pady=5)
                entry2 = tk.Entry(window)
                entry2.grid(column=3,row=0,padx=5,pady=5)
                entry3 = tk.Entry(window)
                entry3.grid(column=5,row=0,padx=5,pady=5)
                entry4 = tk.Entry(window)
                entry4.grid(column=7,row=0,padx=5,pady=5)
                combobox = ttk.Combobox(master=window, values=["男", "女", "其它"])
                combobox.grid(row=0, column=9,padx=10,pady=10)
                entry1.focus_set()
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry3.focus_set())
                entry3.bind("<Return>", lambda event: entry4.focus_set())
                entry4.bind("<Return>", lambda event: combobox.focus_set())
                combobox.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry2.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry3.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry4.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                combobox.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
            case "竖排样式":
                window = ttk.Toplevel(str(root_main))
                window.title("紫微斗数")
                window.iconbitmap(ICON_PATH)
                text1 = tk.Label(window,text="年:")
                text1.grid(column=0,row=0,padx=5,pady=5)
                text2 = tk.Label(window,text="月:")
                text2.grid(column=0,row=1,padx=5,pady=5)
                text3 = tk.Label(window,text="日:")
                text3.grid(column=0,row=2,padx=5,pady=5)
                text4 = tk.Label(window,text="时:")
                text4.grid(column=0,row=3,padx=5,pady=5)
                text5 = tk.Label(window,text="性别:")
                text5.grid(column=0,row=4,padx=5,pady=5)
                entry1 = tk.Entry(window)
                entry1.grid(column=1,row=0,padx=5,pady=5)
                entry2 = tk.Entry(window)
                entry2.grid(column=1,row=1,padx=5,pady=5)
                entry3 = tk.Entry(window)
                entry3.grid(column=1,row=2,padx=5,pady=5)
                entry4 = tk.Entry(window)
                entry4.grid(column=1,row=3,padx=5,pady=5)
                combobox = ttk.Combobox(master=window, values=["男", "女", "其它"])
                combobox.grid(row=4, column=1,padx=10,pady=10)
                entry1.focus_set()
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry3.focus_set())
                entry3.bind("<Return>", lambda event: entry4.focus_set())
                entry4.bind("<Return>", lambda event: combobox.focus_set())
                combobox.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry2.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry3.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                entry4.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
                combobox.bind('<Shift_R>', lambda event: self.z_judge(window,entry1,entry2,entry3,entry4,combobox))
    
    def z_judge(self,window,entry1,entry2,entry3,entry4,combobox):
        gain_entry1 = entry1.get()
        gain_entry2 = entry2.get()
        gain_entry3 = entry3.get()
        gain_entry4 = entry4.get()
        gain_combobox = combobox.get()
        r = re.sub(r'[^公元前\d]+', '', gain_entry1)
        r_ = re.sub(r'\D+',"",gain_entry2)
        r__ = re.sub(r'\D+',"",gain_entry3)
        r___ = re.sub(r'\D+',"",gain_entry4)
        r____ = re.sub(r'^(?!男$|女$|其它$).+$',"",gain_combobox)
        if gain_entry1 and (r != gain_entry1):
            messagebox.showerror("错误", message="请按以下格式输入：\n例：\n年：2024或公元前2024\n月：4\n日：1\n时：1\n性别：其它\n注：以正月初一为起", parent=window)
        elif gain_entry2 and (r_ != gain_entry2):
            messagebox.showerror("错误", message="请按以下格式输入：\n例：\n年：2024或公元前2024\n月：4\n日：1\n时：1\n性别：其它\n注：以正月初一为起", parent=window)
        elif gain_entry3 and (r__ != gain_entry3):
            messagebox.showerror("错误", message="请按以下格式输入：\n例：\n年：2024或公元前2024\n月：4\n日：1\n时：1\n性别：其它\n注：以正月初一为起", parent=window)
        elif gain_entry4 and (r___ != gain_entry4):
            messagebox.showerror("错误", message="请按以下格式输入：\n例：\n年：2024或公元前2024\n月：4\n日：1\n时：1\n性别：其它\n注：以正月初一为起", parent=window)
        elif gain_combobox and (r____ != gain_combobox):
            messagebox.showerror("错误", message="请按以下格式输入：\n例：\n年：2024或公元前2024\n月：4\n日：1\n时：1\n性别：其它\n注：以正月初一为起", parent=window)
        elif not (r and r_ and r__ and r___ and r____):
            messagebox.showerror("错误", message="并未输入值", parent=window)
        else:
            datetime.datetime(int(re.sub(r'\D+',"",r)), int(r_), int(r__)).date()
            if not (0 < int(r___) <= 24):
                messagebox.showerror("错误", message="错误的日期", parent=window)
            else:
                self.ziWei = ZiWeiDouShu(r, r_, r__, r___)
                self.nianGan,nianGanwuXing,nianGanyinYang\
    ,self.nianZhi,nianZhiwuXing,nianZhiyinYang,nianZhishengXiao\
        ,yueGan,yueGanwuXing,yueGanyinYang\
            ,self.yueZhi,yueZhiwuXing,yueZhiyinYang,yueZhishengXiao\
            ,self.shiChen,shiChenwuXing,shiChenyinYang,shiChenshengXiao\
                ,self.Ming,self.Shen,self.wuXingju,self.ziWei\
                    ,JD,NOONJD,MJD\
                        ,riGan,riGanwuXing,ruGanyinYang\
                            ,riZhi,riZhiwuXing,riZhiyinYang,ruZhishengXiao\
                            ,shiGan,shiGanwuXing,shiGanyinYang\
                            ,self.day\
                                                      = self.ziWei.ZiWeisoushu()
                ganZhi = self.nianGan+self.nianZhi+yueGan+self.yueZhi+riGan+riZhi+shiGan+self.shiChen
                wuXing = nianGanwuXing+nianZhiwuXing+yueGanwuXing+yueZhiwuXing+riGanwuXing+riZhiwuXing+shiGanwuXing+shiChenwuXing
                yinYang = nianGanyinYang+nianZhiyinYang+yueGanyinYang+yueZhiyinYang+ruGanyinYang+riZhiyinYang+shiGanyinYang+shiChenyinYang
                shengXiao = "无"+nianZhishengXiao+"无"+yueZhishengXiao+"无"+ruZhishengXiao+"无"+shiChenshengXiao
                self.male_or_female = nianGanyinYang + r____

                self.group_w13\
                     = "天干地支：{}\n干支五行：{}\n干支阴阳：{}\n干支生肖：{}\n儒略日【傍晚】：{}\n儒略日【正午】：{}\n简化儒略日：{}\n五行局：{}\n{}\n"\
                    .format(ganZhi,wuXing,yinYang,shengXiao,JD,NOONJD,MJD,self.wuXingju,self.male_or_female)
                
                self.zi_wei_dou_shu()

    def zi_wei_dou_shu(self):
        self.window_z = ttk.Toplevel()
        self.window_z.title("轻量记事本-小工具-紫微斗数-三合派")
        self.window_z.iconbitmap(ICON_PATH)
        self.w = ttk.Frame(self.window_z)
        self.w.grid(row=0,column=0,padx=10,pady=10)
        self.w2 = ttk.Frame(self.window_z)
        self.w2.grid(row=0,column=1,padx=10,pady=10)
        self.w3 = ttk.Frame(self.window_z)
        self.w3.grid(row=0,column=2,padx=10,pady=10)
        self.w4 = ttk.Frame(self.window_z)
        self.w4.grid(row=0,column=3,padx=10,pady=10)
        self.w5 = ttk.Frame(self.window_z)
        self.w5.grid(row=1,column=0,padx=10,pady=10)
        self.w6 = ttk.Frame(self.window_z)
        self.w6.grid(row=2,column=0,padx=10,pady=10)
        self.w7 = ttk.Frame(self.window_z)
        self.w7.grid(row=3,column=0,padx=10,pady=10)
        self.w8 = ttk.Frame(self.window_z)
        self.w8.grid(row=3,column=1,padx=10,pady=10)
        self.w9 = ttk.Frame(self.window_z)
        self.w9.grid(row=3,column=2,padx=10,pady=10)
        self.w10 = ttk.Frame(self.window_z)
        self.w10.grid(row=3,column=3,padx=10,pady=10)
        self.w11 = ttk.Frame(self.window_z)
        self.w11.grid(row=2,column=3,padx=10,pady=10)
        self.w12 = ttk.Frame(self.window_z)
        self.w12.grid(row=1,column=3,padx=10,pady=10)
        self.w13 = ttk.Frame(self.window_z)
        self.w13.grid(row=1,column=1,rowspan=1,columnspan=1,padx=10,pady=10)
        class_grid = GridLabelText()

        # 定义窗口列表
        windows = [self.w, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w13]
        texts = ["巳", "午", "未", "申", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", self.group_w13]

        god_labels = [
            ("命宫", 10, 1),
            ("兄弟", 10, 1),
            ("夫妻", 10, 1),
            ("子女", 10, 1),
            ("财帛", 10, 1),
            ("疾厄", 10, 1),
            ("迁移", 10, 1),
            ("仆役", 10, 1),
            ("官禄", 10, 1),
            ("田宅", 10, 1),
            ("福德", 10, 1),
            ("父母", 10, 1),
        ]
        
        positions = {
            "子": [self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8],
            "丑": [self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7],
            "寅": [self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6],
            "卯": [self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5],
            "辰": [self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w],
            "巳": [self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2],
            "午": [self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3],
            "未": [self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4],
            "申": [self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12],
            "酉": [self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11],
            "戌": [self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10],
            "亥": [self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9],
        }
        
        # 生成标签
        for i, (label_text, row, col) in enumerate(god_labels):
            if self.Ming in positions:
                ttk.Label(positions[self.Ming][i], text=label_text, font=self.font_style).grid(row=row, column=col)
        
        shen_map = {
            "子": self.w9, "丑": self.w8, "寅": self.w7, "卯": self.w6,
            "辰": self.w5, "巳": self.w, "午": self.w2, "未": self.w3,
            "申": self.w4, "酉": self.w12, "戌": self.w11, "亥": self.w10
        }

        天才_map = {
            "子":positions[self.Ming][0],"丑":positions[self.Ming][11],"寅":positions[self.Ming][10],"卯":positions[self.Ming][9],
            "辰":positions[self.Ming][8],"巳":positions[self.Ming][7],"午":positions[self.Ming][6],"未":positions[self.Ming][5],
            "申":positions[self.Ming][4],"酉":positions[self.Ming][3],"戌":positions[self.Ming][2],"亥":positions[self.Ming][1]
        }

        命主_map = {
            self.w9:"子",
            self.w8:"丑",
            self.w7:"寅",
            self.w6:"卯",
            self.w5:"辰",
            self.w:"巳",
            self.w2:"午",
            self.w3:"未",
            self.w4:"申",
            self.w12:"酉",
            self.w11:"戌",
            self.w10:"亥"
        }

        命主_dict = {
            "子":"贪狼",
            "丑":"巨门",
            "寅":"禄存",
            "卯":"文曲",
            "辰":"廉贞",
            "巳":"武曲",
            "午":"破军",
            "未":"武曲",
            "申":"廉贞",
            "酉":"文曲",
            "戌":"禄存",
            "亥":"巨门"
        }

        身主_dict = {
            "子":"火星",
            "丑":"天相",
            "寅":"天梁",
            "卯":"天同",
            "辰":"文昌",
            "巳":"天机",
            "午":"火星",
            "未":"天相",
            "申":"天梁",
            "酉":"天同",
            "戌":"文昌",
            "亥":"天机"
        }

        Shen_ = ttk.Label(shen_map[self.Shen], text="身宫", font=self.font_style,foreground="#cb0008")
        class_grid.grid_label_text("身宫", Shen_, 9, 2,GridLabelText.get_window(Shen_))
        天才 = ttk.Label(天才_map[self.nianZhi],text="天才",font=self.font_style)
        天伤 = ttk.Label(positions[self.Ming][7],text="天伤",font=self.font_style)
        天使 = ttk.Label(positions[self.Ming][5],text="天使",font=self.font_style)
        命主 = 命主_dict[命主_map[positions[self.Ming][0]]]
        身主 = 身主_dict[self.nianZhi]
        self.group_w13 += f"命主：{命主}\n身主：{身主}" 

        
        windows = [self.w7,
                   self.w6,
                   self.w5,
                   self.w,
                   self.w2,
                   self.w3,
                   self.w4,
                   self.w12,
                   self.w11,
                   self.w10,
                   self.w9,
                   self.w8
                   ]
        labels = {
            "甲": ["丙", "丁", "戊", "己", "庚", "庚", "壬", "癸", "甲", "乙", "丙", "丁"],
            "己": ["丙", "丁", "戊", "己", "庚", "庚", "壬", "癸", "甲", "乙", "丙", "丁"],
            "乙": ["戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"],
            "庚": ["戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"],
            "丙": ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛"],
            "辛": ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛"],
            "丁": ["壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
            "壬": ["壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
            "戊": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙"],
            "癸": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙"],
        }

        texts = labels[self.nianGan]

        for i, text in enumerate(texts):
            label = ttk.Label(windows[i], text=text, font=self.font_style)
            class_grid.grid_label_text(text, label, 9, 0,GridLabelText.get_window(label))

        match self.ziWei:
            case "子":
                ziWei_ = ttk.Label(self.w9, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w10, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w12, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w4, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w3, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w5, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w5, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w2, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w3, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w4, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w12, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w11, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w7, text="破军", font=self.font_style)
                match self.nianZhi:
                    case"戌":
                        pass
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w5, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w7, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w4, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w12, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w10, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w12, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w9, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w3, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w10, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w5, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w3, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w10, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w3, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w2, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w10, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w4, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w2, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w12, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w12, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w4, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w3, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w3, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w12, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w12, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w9, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w4, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w7, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w3, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w2, text="贪狼【忌】", font=self.font_style)
            case "丑":
                ziWei_ = ttk.Label(self.w8, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w9, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w11, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w12, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w4, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w6, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w5, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w2, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w3, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w4, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w12, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w8, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w8, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w12, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w5, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w9, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w4, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w8, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w5, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w4, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w9, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w5, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w4, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w9, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w2, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w5, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w9, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w12, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w4, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w11, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w12, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w5, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w4, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w2, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w11, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w4, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w8, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w12, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w8, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w2, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w5, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w, text="贪狼【忌】", font=self.font_style)
            case "寅":
                ziWei_ = ttk.Label(self.w7, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w8, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w10, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w11, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w12, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w2, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w7, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w6, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w5, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w2, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w3, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w4, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w9, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w2, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w9, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w11, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w10, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w8, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w3, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w7, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w6, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w12, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w8, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w2, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w6, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w12, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w8, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w5, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w6, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w8, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w11, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w5, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w3, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w10, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w11, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w6, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w12, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w10, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w3, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w7, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w11, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w9, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w6, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w5, text="贪狼【忌】", font=self.font_style)
            case "卯":
                ziWei_ = ttk.Label(self.w6, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w7, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w9, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w10, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w11, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w3, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w8, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w7, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w6, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w5, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w2, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w3, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w10, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w3, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w10, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w10, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w9, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w7, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w2, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w6, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w7, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w11, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w7, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w3, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w7, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w11, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w7, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w5, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w6, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w7, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w7, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w10, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w6, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w2, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w9, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w10, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w7, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w11, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w5, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w9, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w2, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w6, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w10, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w10, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w5, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w7, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w6, text="贪狼【忌】", font=self.font_style)
            case "辰":
                ziWei_ = ttk.Label(self.w5, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w6, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w8, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w9, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w10, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w4, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w9, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w8, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w7, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w6, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w5, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w2, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w11, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w4, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w11, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w9, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w8, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w6, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w5, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w8, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w10, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w6, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w4, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w8, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w10, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w6, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w6, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w7, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w8, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w6, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w9, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w7, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w8, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w9, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w8, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w10, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w6, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w8, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w5, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w9, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w11, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w6, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w8, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w7, text="贪狼【忌】", font=self.font_style)
            case "巳":
                ziWei_ = ttk.Label(self.w, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w5, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w7, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w8, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w9, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w12, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w10, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w9, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w8, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w7, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w6, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w5, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w12, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w12, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w12, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w8, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w7, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w5, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w5, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w9, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w9, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w5, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w12, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w9, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w9, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w5, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w7, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w8, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w9, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w5, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w9, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w8, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w5, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w7, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w8, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w9, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w9, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w7, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w7, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w5, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w8, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w12, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w7, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w9, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w8, text="贪狼【忌】", font=self.font_style)
            case "午":
                ziWei_ = ttk.Label(self.w2, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w6, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w7, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w8, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w11, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w11, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w10, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w9, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w8, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w7, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w6, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w5, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w4, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w11, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w4, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w7, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w6, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w6, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w2, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w10, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w8, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w11, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w10, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w8, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w8, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w9, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w10, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w7, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w9, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w6, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w6, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w7, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w10, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w8, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w8, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w6, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w6, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w2, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w7, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w4, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w8, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w10, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w9, text="贪狼【忌】", font=self.font_style)
            case "未":
                ziWei_ = ttk.Label(self.w3, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w2, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w5, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w6, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w7, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w10, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w12, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w11, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w10, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w9, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w8, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w7, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w6, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w3, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w10, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w3, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w6, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w5, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w2, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w7, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w3, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w11, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w7, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w2, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w10, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w11, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w7, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w2, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w9, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w10, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w11, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w2, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w6, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w10, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w7, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w5, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w6, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w11, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w7, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w9, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w5, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w7, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w3, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w6, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w3, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w9, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w11, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w10, text="贪狼【忌】", font=self.font_style)
            case "申":
                ziWei_ = ttk.Label(self.w4, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w3, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w5, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w6, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w9, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w4, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w12, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w11, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w10, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w9, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w8, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w7, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w2, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w9, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w2, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w5, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w3, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w8, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w4, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w12, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w6, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w3, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w9, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w12, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w6, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w3, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w10, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w11, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w12, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w3, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w5, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w11, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w8, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w5, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w12, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w6, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w10, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w8, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w4, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w5, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w2, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w10, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w12, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w11, text="贪狼【忌】", font=self.font_style)
            case "酉":
                ziWei_ = ttk.Label(self.w12, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w4, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w2, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w5, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w8, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w3, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w4, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w12, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w11, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w10, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w9, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w8, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w8, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w2, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w4, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w9, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w12, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w4, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w5, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w4, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w8, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w4, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w5, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w4, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w11, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w12, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w4, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w4, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w12, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w9, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w2, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w4, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w5, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w11, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w2, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w9, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w12, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w11, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w4, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w12, text="贪狼【忌】", font=self.font_style)
            case "戌":
                ziWei_ = ttk.Label(self.w11, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w12, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w3, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w2, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w7, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w2, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w3, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w4, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w12, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w11, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w10, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w9, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w5, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w7, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w5, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w2, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w3, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w12, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w10, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w11, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w3, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w12, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w7, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w3, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w12, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w12, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w4, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w3, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w12, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w2, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w4, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w10, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w3, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w2, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w3, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w12, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w3, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w10, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w11, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w2, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w5, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w12, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w3, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w4, text="贪狼【忌】", font=self.font_style)
            case "亥":
                ziWei_ = ttk.Label(self.w10, text="紫微", font=self.font_style)
                tianJi = ttk.Label(self.w11, text="天机", font=self.font_style)
                taiYang = ttk.Label(self.w4, text="太阳", font=self.font_style)
                wuQu = ttk.Label(self.w3, text="武曲", font=self.font_style)
                tianTong = ttk.Label(self.w2, text="天同", font=self.font_style)
                lianZhen = ttk.Label(self.w6, text="廉贞", font=self.font_style)
                tianFu = ttk.Label(self.w, text="天府", font=self.font_style)
                taiYin = ttk.Label(self.w2, text="太阴", font=self.font_style)
                tanLang = ttk.Label(self.w3, text="贪狼", font=self.font_style)
                juMen = ttk.Label(self.w4, text="巨门", font=self.font_style)
                天相 = ttk.Label(self.w12, text="天相", font=self.font_style)
                tianLiang = ttk.Label(self.w11, text="天梁", font=self.font_style)
                qiSha = ttk.Label(self.w10, text="七杀", font=self.font_style)
                poJun = ttk.Label(self.w6, text="破军", font=self.font_style)
                match self.nianGan:
                    case "甲":
                        禄存 = ttk.Label(self.w7, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w6, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w8, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w3, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w12, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        lianZhen = ttk.Label(self.w6, text="廉贞【禄】", font=self.font_style)
                        poJun = ttk.Label(self.w6, text="破军【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w3, text="武曲【科】", font=self.font_style)
                        taiYang = ttk.Label(self.w4, text="太阳【忌】", font=self.font_style)
                    case "乙":
                        禄存 = ttk.Label(self.w6, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w5, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w7, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w5, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w4, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tianJi = ttk.Label(self.w11, text="天机【禄】", font=self.font_style)
                        tianLiang = ttk.Label(self.w11, text="天梁【权】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w10, text="紫微【科】", font=self.font_style)
                        taiYin = ttk.Label(self.w2, text="太阴【忌】", font=self.font_style)
                    case "丙":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w9, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w9, text="天厨", font=self.font_style)
                        tianTong = ttk.Label(self.w2, text="天同【禄】", font=self.font_style)
                        tianJi = ttk.Label(self.w11, text="天机【权】", font=self.font_style)
                        lianZhen = ttk.Label(self.w6, text="廉贞【忌】", font=self.font_style)
                    case "丁":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w10, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w12, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w7, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w10, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w, text="天厨", font=self.font_style)
                        taiYin = ttk.Label(self.w2, text="太阴【禄】", font=self.font_style)
                        tianTong = ttk.Label(self.w2, text="天同【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w11, text="天机【科】", font=self.font_style)
                        juMen = ttk.Label(self.w4, text="巨门【忌】", font=self.font_style)
                    case "戊":
                        禄存 = ttk.Label(self.w, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w2, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w5, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w6, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w6, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        tanLang = ttk.Label(self.w3, text="贪狼【禄】", font=self.font_style)
                        taiYin = ttk.Label(self.w2, text="太阴【权】", font=self.font_style)
                        tianJi = ttk.Label(self.w11, text="天机【忌】", font=self.font_style)
                    case "己":
                        禄存 = ttk.Label(self.w2, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w3, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w9, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w4, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w7, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w4, text="天厨", font=self.font_style)
                        wuQu = ttk.Label(self.w3, text="武曲【禄】", font=self.font_style)
                        tanLang = ttk.Label(self.w3, text="贪狼【权】", font=self.font_style)
                        tianLiang = ttk.Label(self.w11, text="天梁【科】", font=self.font_style)
                    case "庚":
                        禄存 = ttk.Label(self.w4, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w12, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w3, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w8, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w3, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w10, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w7, text="天厨", font=self.font_style)
                        taiYang = ttk.Label(self.w4, text="太阳【禄】", font=self.font_style)
                        wuQu = ttk.Label(self.w3, text="武曲【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w2, text="太阴【科】", font=self.font_style)
                        tianTong = ttk.Label(self.w2, text="天同【忌】", font=self.font_style)
                    case "辛":
                        禄存 = ttk.Label(self.w12, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w11, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w4, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w2, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w7, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w12, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w2, text="天厨", font=self.font_style)
                        juMen = ttk.Label(self.w4, text="巨门【禄】", font=self.font_style)
                        taiYang = ttk.Label(self.w4, text="太阳【权】", font=self.font_style)
                    case "壬":
                        禄存 = ttk.Label(self.w10, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w9, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w11, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w11, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w2, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w12, text="天厨", font=self.font_style)
                        tianLiang = ttk.Label(self.w11, text="天梁【禄】", font=self.font_style)
                        ziWei_ = ttk.Label(self.w10, text="紫微【权】", font=self.font_style)
                        wuQu = ttk.Label(self.w3, text="武曲【忌】", font=self.font_style)
                    case "癸":
                        禄存 = ttk.Label(self.w9, text="禄存", font=self.font_style)
                        擎羊 = ttk.Label(self.w8, text="擎羊", font=self.font_style)
                        陀罗 = ttk.Label(self.w10, text="陀罗", font=self.font_style)
                        天魁 = ttk.Label(self.w6, text="天魁", font=self.font_style)
                        天钺 = ttk.Label(self.w, text="天钺", font=self.font_style)
                        天官 = ttk.Label(self.w2, text="天官", font=self.font_style)
                        天福 = ttk.Label(self.w, text="天福", font=self.font_style)
                        天厨 = ttk.Label(self.w10, text="天厨", font=self.font_style)
                        poJun = ttk.Label(self.w6, text="破军【禄】", font=self.font_style)
                        juMen = ttk.Label(self.w4, text="巨门【权】", font=self.font_style)
                        taiYin = ttk.Label(self.w2, text="太阴【科】", font=self.font_style)
                        tanLang = ttk.Label(self.w3, text="贪狼【忌】", font=self.font_style)

        match self.male_or_female:
            case "阳男"|"阴女":
                match self.nianGan:
                    case "甲":
                        博士 = ttk.Label(self.w7, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w6, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w5, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w2, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w3, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w4, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w12, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w11, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w10, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w9, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w8, text="官府", font=self.font_style)
                    case "乙":
                        博士 = ttk.Label(self.w6, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w5, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w2, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w3, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w4, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w12, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w11, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w10, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w9, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w8, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w7, text="官府", font=self.font_style)
                    case "丙":
                        博士 = ttk.Label(self.w, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w2, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w3, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w4, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w12, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w11, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w10, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w9, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w8, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w7, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w6, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w5, text="官府", font=self.font_style)
                    case "丁":
                        博士 = ttk.Label(self.w2, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w3, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w4, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w12, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w11, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w10, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w9, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w8, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w7, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w6, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w5, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w, text="官府", font=self.font_style)
                    case "戊":
                        博士 = ttk.Label(self.w, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w2, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w3, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w4, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w12, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w11, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w10, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w9, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w8, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w7, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w6, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w5, text="官府", font=self.font_style)
                    case "己":
                        博士 = ttk.Label(self.w2, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w3, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w4, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w12, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w11, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w10, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w9, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w8, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w7, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w6, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w5, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w, text="官府", font=self.font_style)
                    case "庚":
                        博士 = ttk.Label(self.w4, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w12, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w11, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w10, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w9, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w8, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w7, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w6, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w5, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w2, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w3, text="官府", font=self.font_style)
                    case "辛":
                        博士 = ttk.Label(self.w12, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w11, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w10, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w9, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w8, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w7, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w6, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w5, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w2, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w3, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w4, text="官府", font=self.font_style)
                    case "壬":
                        博士 = ttk.Label(self.w10, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w9, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w8, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w7, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w6, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w5, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w2, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w3, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w4, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w12, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w11, text="官府", font=self.font_style)
                    case "癸":
                        博士 = ttk.Label(self.w9, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w8, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w7, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w6, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w5, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w2, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w3, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w4, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w12, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w11, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w10, text="官府", font=self.font_style)
            case "阴男"|"阳女":
                match self.nianGan:
                    case "甲":
                        博士 = ttk.Label(self.w7, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w8, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w9, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w10, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w11, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w12, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w4, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w3, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w2, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w5, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w6, text="官府", font=self.font_style)
                    case "乙":
                        博士 = ttk.Label(self.w6, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w7, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w8, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w9, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w10, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w11, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w12, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w4, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w3, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w2, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w5, text="官府", font=self.font_style)
                    case "丙":
                        博士 = ttk.Label(self.w, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w5, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w6, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w7, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w8, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w9, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w10, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w11, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w12, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w4, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w3, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w2, text="官府", font=self.font_style)
                    case "丁":
                        博士 = ttk.Label(self.w2, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w5, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w6, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w7, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w8, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w9, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w10, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w11, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w12, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w4, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w3, text="官府", font=self.font_style)
                    case "戊":
                        博士 = ttk.Label(self.w, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w5, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w6, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w7, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w8, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w9, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w10, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w11, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w12, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w4, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w3, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w2, text="官府", font=self.font_style)
                    case "己":
                        博士 = ttk.Label(self.w2, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w5, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w6, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w7, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w8, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w9, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w10, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w11, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w12, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w4, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w3, text="官府", font=self.font_style)
                    case "庚":
                        博士 = ttk.Label(self.w4, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w3, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w2, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w5, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w6, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w7, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w8, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w9, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w10, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w11, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w12, text="官府", font=self.font_style)
                    case "辛":
                        博士 = ttk.Label(self.w12, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w4, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w3, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w2, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w5, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w6, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w7, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w8, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w9, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w10, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w11, text="官府", font=self.font_style)
                    case "壬":
                        博士 = ttk.Label(self.w10, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w11, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w12, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w4, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w3, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w2, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w5, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w6, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w7, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w8, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w9, text="官府", font=self.font_style)
                    case "癸":
                        博士 = ttk.Label(self.w9, text="博士", font=self.font_style)
                        力士 = ttk.Label(self.w10, text="力士", font=self.font_style)
                        青龙 = ttk.Label(self.w11, text="青龙", font=self.font_style)
                        小耗 = ttk.Label(self.w12, text="小耗", font=self.font_style)
                        将军 = ttk.Label(self.w4, text="将军", font=self.font_style)
                        奏书 = ttk.Label(self.w3, text="奏书", font=self.font_style)
                        飞廉 = ttk.Label(self.w2, text="飞廉", font=self.font_style)
                        喜神 = ttk.Label(self.w, text="喜神", font=self.font_style)
                        病符 = ttk.Label(self.w5, text="病符", font=self.font_style)
                        大耗 = ttk.Label(self.w6, text="大耗", font=self.font_style)
                        伏兵 = ttk.Label(self.w7, text="伏兵", font=self.font_style)
                        官府 = ttk.Label(self.w8, text="官府", font=self.font_style)        

        博士.grid(row=11,column=0)
        力士.grid(row=11,column=0)
        青龙.grid(row=11,column=0)
        小耗.grid(row=11,column=0)
        将军.grid(row=11,column=0)
        奏书.grid(row=11,column=0)
        飞廉.grid(row=11,column=0)
        喜神.grid(row=11,column=0)
        病符.grid(row=11,column=0)
        大耗.grid(row=11,column=0)
        伏兵.grid(row=11,column=0)
        官府.grid(row=11,column=0)

        Shen_num = ZHI_DICT_NUM[self.Shen]
        nianZhi_num = ZHI_DICT_NUM[self.nianZhi]
        Ming_num = ZHI_DICT_NUM[self.Ming]
        天寿_num = (Shen_num-1+nianZhi_num)%12#宫位
        window_w =[self.w9,self.w8,self.w7,self.w6,self.w5,self.w,self.w2,self.w3,self.w4,self.w12,self.w11,self.w10]
        w_value = window_w[天寿_num]

        match self.nianZhi:
            case "戌"|"午"|"寅":
                match self.shiChen:
                    case "子":
                        wenChang = ttk.Label(self.w11, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w5, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w8, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w6, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w10, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w10, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w2, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w7, text="封诰", font=self.font_style)
                    case "丑":
                        wenChang = ttk.Label(self.w12, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w7, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w5, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w9, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w11, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w3, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w6, text="封诰", font=self.font_style)
                    case "寅":
                        wenChang = ttk.Label(self.w4, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w2, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w6, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w8, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w12, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w4, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w5, text="封诰", font=self.font_style)
                    case "卯":
                        wenChang = ttk.Label(self.w3, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w3, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w5, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w2, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w7, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w4, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w12, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w, text="封诰", font=self.font_style)
                    case "辰":
                        wenChang = ttk.Label(self.w2, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w4, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w3, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w6, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w3, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w11, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w2, text="封诰", font=self.font_style)
                    case "巳":
                        wenChang = ttk.Label(self.w, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w12, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w2, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w4, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w5, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w2, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w10, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w3, text="封诰", font=self.font_style)
                    case "午":
                        wenChang = ttk.Label(self.w5, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w11, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w3, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w12, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w9, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w4, text="封诰", font=self.font_style)
                    case "未":
                        wenChang = ttk.Label(self.w6, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w10, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w4, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w11, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w2, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w5, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w8, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w12, text="封诰", font=self.font_style)
                    case "申":
                        wenChang = ttk.Label(self.w7, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w9, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w12, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w10, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w3, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w6, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w7, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w11, text="封诰", font=self.font_style)
                    case "酉":
                        wenChang = ttk.Label(self.w8, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w8, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w11, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w9, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w4, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w7, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w6, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w10, text="封诰", font=self.font_style)
                    case "戌":
                        wenChang = ttk.Label(self.w9, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w7, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w10, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w8, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w12, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w8, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w5, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w9, text="封诰", font=self.font_style)
                    case "亥":
                        wenChang = ttk.Label(self.w10, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w6, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w9, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w7, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w11, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w9, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w8, text="封诰", font=self.font_style)
            case "辰"|"子"|"申":
                match self.shiChen:
                    case "子":
                        wenChang = ttk.Label(self.w11, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w5, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w7, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w11, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w10, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w10, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w2, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w7, text="封诰", font=self.font_style)
                    case "丑":
                        wenChang = ttk.Label(self.w12, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w6, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w10, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w9, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w11, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w3, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w6, text="封诰", font=self.font_style)
                    case "寅":
                        wenChang = ttk.Label(self.w4, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w2, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w5, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w9, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w8, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w12, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w4, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w5, text="封诰", font=self.font_style)
                    case "卯":
                        wenChang = ttk.Label(self.w3, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w3, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w8, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w7, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w4, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w12, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w, text="封诰", font=self.font_style)
                    case "辰":
                        wenChang = ttk.Label(self.w2, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w4, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w2, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w7, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w6, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w3, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w11, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w2, text="封诰", font=self.font_style)
                    case "巳":
                        wenChang = ttk.Label(self.w, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w12, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w3, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w6, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w5, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w2, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w10, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w3, text="封诰", font=self.font_style)
                    case "午":
                        wenChang = ttk.Label(self.w5, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w11, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w4, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w5, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w9, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w4, text="封诰", font=self.font_style)
                    case "未":
                        wenChang = ttk.Label(self.w6, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w10, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w12, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w2, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w5, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w8, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w12, text="封诰", font=self.font_style)
                    case "申":
                        wenChang = ttk.Label(self.w7, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w9, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w11, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w2, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w3, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w6, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w7, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w11, text="封诰", font=self.font_style)
                    case "酉":
                        wenChang = ttk.Label(self.w8, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w8, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w10, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w3, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w4, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w7, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w6, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w10, text="封诰", font=self.font_style)
                    case "戌":
                        wenChang = ttk.Label(self.w9, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w7, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w9, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w4, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w12, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w8, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w5, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w9, text="封诰", font=self.font_style)
                    case "亥":
                        wenChang = ttk.Label(self.w10, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w6, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w8, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w12, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w11, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w9, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w8, text="封诰", font=self.font_style)
            case "丑"|"酉"|"巳":
                match self.shiChen:
                    case "子":
                        wenChang = ttk.Label(self.w11, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w5, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w6, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w11, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w10, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w10, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w2, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w7, text="封诰", font=self.font_style)
                    case "丑":
                        wenChang = ttk.Label(self.w12, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w5, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w10, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w9, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w11, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w3, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w6, text="封诰", font=self.font_style)
                    case "寅":
                        wenChang = ttk.Label(self.w4, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w2, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w9, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w8, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w12, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w4, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w5, text="封诰", font=self.font_style)
                    case "卯":
                        wenChang = ttk.Label(self.w3, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w3, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w2, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w8, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w7, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w4, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w12, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w, text="封诰", font=self.font_style)
                    case "辰":
                        wenChang = ttk.Label(self.w2, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w4, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w3, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w7, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w6, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w3, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w11, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w2, text="封诰", font=self.font_style)
                    case "巳":
                        wenChang = ttk.Label(self.w, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w12, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w4, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w6, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w5, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w2, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w10, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w3, text="封诰", font=self.font_style)
                    case "午":
                        wenChang = ttk.Label(self.w5, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w11, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w12, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w5, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w9, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w4, text="封诰", font=self.font_style)
                    case "未":
                        wenChang = ttk.Label(self.w6, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w10, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w11, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w2, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w5, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w8, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w12, text="封诰", font=self.font_style)
                    case "申":
                        wenChang = ttk.Label(self.w7, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w9, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w10, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w2, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w3, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w6, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w7, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w11, text="封诰", font=self.font_style)
                    case "酉":
                        wenChang = ttk.Label(self.w8, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w8, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w9, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w3, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w4, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w7, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w6, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w10, text="封诰", font=self.font_style)
                    case "戌":
                        wenChang = ttk.Label(self.w9, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w7, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w8, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w4, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w12, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w8, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w5, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w9, text="封诰", font=self.font_style)
                    case "亥":
                        wenChang = ttk.Label(self.w10, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w6, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w7, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w12, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w11, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w9, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w8, text="封诰", font=self.font_style)
            case "未"|"卯"|"亥":
                match self.shiChen:
                    case "子":
                        wenChang = ttk.Label(self.w11, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w5, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w12, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w11, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w10, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w10, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w2, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w7, text="封诰", font=self.font_style)
                    case "丑":
                        wenChang = ttk.Label(self.w12, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w11, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w10, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w9, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w11, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w3, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w6, text="封诰", font=self.font_style)
                    case "寅":
                        wenChang = ttk.Label(self.w4, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w2, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w10, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w9, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w8, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w12, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w4, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w5, text="封诰", font=self.font_style)
                    case "卯":
                        wenChang = ttk.Label(self.w3, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w3, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w9, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w8, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w7, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w4, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w12, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w, text="封诰", font=self.font_style)
                    case "辰":
                        wenChang = ttk.Label(self.w2, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w4, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w8, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w7, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w6, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w3, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w11, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w2, text="封诰", font=self.font_style)
                    case "巳":
                        wenChang = ttk.Label(self.w, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w12, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w7, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w6, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w5, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w2, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w10, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w3, text="封诰", font=self.font_style)
                    case "午":
                        wenChang = ttk.Label(self.w5, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w11, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w6, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w5, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w9, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w4, text="封诰", font=self.font_style)
                    case "未":
                        wenChang = ttk.Label(self.w6, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w10, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w5, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w2, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w5, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w8, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w12, text="封诰", font=self.font_style)
                    case "申":
                        wenChang = ttk.Label(self.w7, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w9, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w2, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w3, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w6, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w7, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w11, text="封诰", font=self.font_style)
                    case "酉":
                        wenChang = ttk.Label(self.w8, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w8, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w2, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w3, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w4, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w7, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w6, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w10, text="封诰", font=self.font_style)
                    case "戌":
                        wenChang = ttk.Label(self.w9, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w7, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w3, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w4, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w12, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w8, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w5, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w9, text="封诰", font=self.font_style)
                    case "亥":
                        wenChang = ttk.Label(self.w10, text="文昌", font=self.font_style)
                        wenQu = ttk.Label(self.w6, text="文曲", font=self.font_style)
                        huoXing = ttk.Label(self.w4, text="火星", font=self.font_style)
                        lingXing = ttk.Label(self.w12, text="铃星", font=self.font_style)
                        diJie = ttk.Label(self.w11, text="地劫", font=self.font_style)
                        dikong = ttk.Label(self.w9, text="地空", font=self.font_style)
                        taiFu = ttk.Label(self.w, text="台辅", font=self.font_style)
                        fengGao = ttk.Label(self.w8, text="封诰", font=self.font_style)

        match self.yueZhi:
            case "寅":
                zuofu_num = 5
                youbi_num = 11
                zuofu = ttk.Label(self.w5, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w11, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w12, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w8, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w11, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w7, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w11, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w5, text="左辅【科】", font=self.font_style)
            case "卯":
                zuofu_num = 6
                youbi_num = 10
                zuofu = ttk.Label(self.w, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w12, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w11, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w7, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w4, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w11, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w9, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w12, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w, text="左辅【科】", font=self.font_style)
            case "辰":
                zuofu_num = 7
                youbi_num = 9
                zuofu = ttk.Label(self.w2, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w4, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w10, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w6, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w7, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w5, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w11, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w4, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w2, text="左辅【科】", font=self.font_style)
            case "巳":
                zuofu_num = 8
                youbi_num = 8
                zuofu = ttk.Label(self.w3, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w3, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w9, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w5, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w10, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w7, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w4, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w3, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w3, text="左辅【科】", font=self.font_style)
            case "午":
                zuofu_num = 9
                youbi_num = 7
                zuofu = ttk.Label(self.w4, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w2, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w8, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w3, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w2, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w2, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w4, text="左辅【科】", font=self.font_style)
            case "未":
                zuofu_num = 10
                youbi_num = 6
                zuofu = ttk.Label(self.w12, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w7, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w2, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w4, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w6, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w5, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w12, text="左辅【科】", font=self.font_style)
            case "申":
                zuofu_num = 11
                youbi_num = 5
                zuofu = ttk.Label(self.w11, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w5, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w6, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w3, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w7, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w10, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w7, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w5, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w11, text="左辅【科】", font=self.font_style)
            case "酉":
                zuofu_num = 12
                youbi_num = 4
                zuofu = ttk.Label(self.w10, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w6, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w5, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w4, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w10, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w3, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w9, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w6, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w10, text="左辅【科】", font=self.font_style)
            case "戌":
                zuofu_num = 1
                youbi_num = 3
                zuofu = ttk.Label(self.w9, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w7, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w12, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w7, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w11, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w7, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w9, text="左辅【科】", font=self.font_style)
            case "亥":
                zuofu_num = 2
                youbi_num = 2
                zuofu = ttk.Label(self.w8, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w8, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w2, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w11, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w4, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w2, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w4, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w8, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w8, text="左辅【科】", font=self.font_style)
            case "子":
                zuofu_num = 3
                youbi_num = 1
                zuofu = ttk.Label(self.w7, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w9, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w3, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w10, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w7, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w11, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w2, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w9, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w7, text="左辅【科】", font=self.font_style)
            case "丑":
                zuofu_num = 4
                youbi_num = 12
                zuofu = ttk.Label(self.w6, text="左辅", font=self.font_style)
                youbi = ttk.Label(self.w10, text="右弼", font=self.font_style)
                tianxing = ttk.Label(self.w4, text="天刑", font=self.font_style)
                tianyao = ttk.Label(self.w9, text="天姚", font=self.font_style)
                tianwu = ttk.Label(self.w10, text="天巫", font=self.font_style)
                tianyue = ttk.Label(self.w7, text="天月", font=self.font_style)
                tiansha = ttk.Label(self.w5, text="阴煞", font=self.font_style)
                if self.nianGan == "戊":
                    youbi = ttk.Label(self.w10, text="右弼【科】", font=self.font_style)
                if self.nianGan == "壬":
                    zuofu = ttk.Label(self.w6, text="左辅【科】", font=self.font_style)
        match self.shiChen:
            case "子":
                wenchang_num = 11
                wenqu_num = 5
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w11, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w11, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w5, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w5, text="文曲【忌】", font=self.font_style)
            case "丑":
                wenchang_num = 10
                wenqu_num = 6
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w12, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w12, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w, text="文曲【忌】", font=self.font_style)
            case "寅":
                wenchang_num = 9
                wenqu_num = 7
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w4, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w4, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w2, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w2, text="文曲【忌】", font=self.font_style)
            case "卯":
                wenchang_num = 8
                wenqu_num = 8
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w3, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w3, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w3, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w3, text="文曲【忌】", font=self.font_style)
            case "辰":
                wenchang_num = 7
                wenqu_num = 9
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w2, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w2, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w4, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w4, text="文曲【忌】", font=self.font_style)
            case "巳":
                wenchang_num = 6
                wenqu_num = 10
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w12, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w12, text="文曲【忌】", font=self.font_style)
            case "午":
                wenchang_num = 5
                wenqu_num = 11
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w5, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w5, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w11, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w11, text="文曲【忌】", font=self.font_style)
            case "未":
                wenchang_num = 4
                wenqu_num = 12
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w6, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w6, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w10, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w10, text="文曲【忌】", font=self.font_style)
            case "申":
                wenchang_num = 3
                wenqu_num = 1
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w7, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w7, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w9, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w9, text="文曲【忌】", font=self.font_style)
            case "酉":
                wenchang_num = 2
                wenqu_num = 2
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w8, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w8, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w8, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w8, text="文曲【忌】", font=self.font_style)
            case "戌":
                wenchang_num = 1
                wenqu_num = 3
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w9, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w9, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w7, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w7, text="文曲【忌】", font=self.font_style)
            case "亥":
                wenchang_num = 12
                wenqu_num = 4
                if self.nianGan == "丙":
                    wenChang = ttk.Label(self.w10, text="文昌【科】", font=self.font_style)
                elif self.nianGan == "辛":
                    wenChang = ttk.Label(self.w10, text="文昌【忌】", font=self.font_style)
                    wenQu = ttk.Label(self.w6, text="文曲【科】", font=self.font_style)
                elif self.nianGan == "己":
                    wenQu = ttk.Label(self.w6, text="文曲【忌】", font=self.font_style)

        zuofu_num = (zuofu_num - 1 + self.day)%12
        youbi_num = ((youbi_num - 1 - self.day) % 12 + 2)%12
        wenchang_num = ((wenchang_num - 1 - self.day)%12 + 1)%12
        wenqu_num = ((wenqu_num - 1 - self.day) % 12 + 1)%12

        dic_windows = {
            1: self.w9,
            2: self.w8,
            3: self.w7,
            4: self.w6,
            5: self.w5,
            6: self.w,
            7: self.w2,
            8: self.w3,
            9: self.w4,
            10: self.w12,
            11: self.w11,
            0: self.w10
        }

        santai = ttk.Label(dic_windows[zuofu_num], text="三台", font=self.font_style)
        bazuo  = ttk.Label(dic_windows[youbi_num], text="八座", font=self.font_style)
        enguang = ttk.Label(dic_windows[wenchang_num], text="恩光", font=self.font_style)
        tiangui = ttk.Label(dic_windows[wenqu_num], text="天贵", font=self.font_style)
        天寿 = ttk.Label(w_value,text="天寿",font=self.font_style)

        支系 ={
            "子":list(reversed([self.w, self.w8, self.w, self.w4, self.w11, self.w7, self.w12, self.w6, self.w11, self.w5, self.w2, self.w2, self.w11, self.w7])),
            "丑":list(reversed([self.w2, self.w7, self.w8, self.w12, self.w11, self.w7, self.w4, self.w7, self.w12, self.w, self.w3, self.w, self.w12, self.w10])),
            "寅":list(reversed([self.w3, self.w6, self.w12, self.w11, self.w8, self.w, self.w3, self.w8, self.w4, self.w2, self.w4, self.w5, self.w4, self.w4])),
            "卯":list(reversed([self.w4, self.w5, self.w, self.w, self.w8, self.w, self.w2, self.w9, self.w3, self.w3, self.w12, self.w6, self.w3, self.w])),
            "辰":list(reversed([self.w12, self.w, self.w8, self.w2, self.w8, self.w, self.w, self.w10, self.w2, self.w4, self.w11, self.w7, self.w2, self.w7])),
            "巳":list(reversed([self.w11, self.w2, self.w12, self.w3, self.w5, self.w4, self.w5, self.w11, self.w, self.w12, self.w10, self.w8, self.w, self.w10])),
            "午":list(reversed([self.w10, self.w3, self.w, self.w7, self.w5, self.w4, self.w6, self.w12, self.w5, self.w11, self.w9, self.w9, self.w5, self.w4])),
            "未":list(reversed([self.w9, self.w4, self.w8, self.w6, self.w5, self.w4, self.w7, self.w4, self.w6, self.w10, self.w8, self.w10, self.w6, self.w])),
            "申":list(reversed([self.w8, self.w12, self.w12, self.w5, self.w3, self.w10, self.w8, self.w3, self.w7, self.w9, self.w7, self.w11, self.w7, self.w7])),
            "酉":list(reversed([self.w7, self.w11, self.w, self.w10, self.w3, self.w10, self.w9, self.w2, self.w8, self.w8, self.w6, self.w12, self.w8, self.w10])),
            "戌":list(reversed([self.w6, self.w10, self.w8, self.w9, self.w3, self.w10, self.w10, self.w, self.w9, self.w7, self.w5, self.w4, self.w9, self.w4])),
            "亥":list(reversed([self.w5, self.w9, self.w12, self.w8, self.w11, self.w7, self.w11, self.w5, self.w10, self.w6, self.w, self.w3, self.w10, self.w]))
        }

        长生十二 = {
            "水二局":{
                "阴女":[self.w4, self.w12, self.w11, self.w10, self.w9, self.w8, self.w7, self.w6, self.w5, self.w, self.w2, self.w3],
                "阳女":[self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12]
            },
            "木三局":{
                "阴女":[self.w10, self.w9, self.w8, self.w7, self.w6, self.w5, self.w, self.w2, self.w3, self.w4, self.w12, self.w11],
                "阳女":[self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9]
            },
            "金四局":{
                "阴女":[self.w, self.w2, self.w3, self.w4, self.w12, self.w11, self.w10, self.w9, self.w8, self.w7, self.w6, self.w5],
                "阳女":[self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2]
            },
            "土五局":{
                "阴女":[self.w4, self.w12, self.w11, self.w10, self.w9, self.w8, self.w7, self.w6, self.w5, self.w, self.w2, self.w3],
                "阳女":[self.w4, self.w3, self.w2, self.w, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12]
            },
            "火六局":{
                "阴女":[self.w7, self.w6, self.w5, self.w, self.w2, self.w3, self.w4, self.w12, self.w11, self.w10, self.w9, self.w8],
                "阳女":[self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w4, self.w3, self.w2, self.w, self.w5, self.w6]
            }
        }

        截空 = {
            "甲":[self.w4, self.w12],
            "己":[self.w12, self.w4],
            "乙":[self.w3, self.w2],
            "庚":[self.w2, self.w3],
            "丙":[self.w5, self.w],
            "辛":[self.w, self.w5],
            "丁":[self.w7, self.w6],
            "壬":[self.w6, self.w7],
            "戊":[self.w9, self.w8],
            "癸":[self.w8, self.w9]
        }
        
        旬空 = {
            "甲":{
                "子":[self.w11, self.w10],
                "戌":[self.w4, self.w12],
                "申":[self.w2, self.w3],
                "午":[self.w5, self.w],
                "辰":[self.w7, self.w6],
                "寅":[self.w9, self.w8]
            },
            "乙":{
                "丑":[self.w11, self.w10],
                "亥":[self.w4, self.w12],
                "酉":[self.w2, self.w3],
                "未":[self.w5, self.w],
                "巳":[self.w7, self.w6],
                "卯":[self.w9, self.w8]
            },
            "丙":{
                "寅":[self.w11, self.w10],
                "子":[self.w4, self.w12],
                "戌":[self.w2, self.w3],
                "申":[self.w5, self.w],
                "午":[self.w7, self.w6],
                "辰":[self.w9, self.w8]
            },
            "丁":{
                "卯":[self.w11, self.w10],
                "丑":[self.w4, self.w12],
                "亥":[self.w2, self.w3],
                "酉":[self.w5, self.w],
                "未":[self.w7, self.w6],
                "巳":[self.w9, self.w8]
            },
            "戊":{
                "辰":[self.w11, self.w10],
                "寅":[self.w4, self.w12],
                "子":[self.w2, self.w3],
                "戌":[self.w5, self.w],
                "申":[self.w7, self.w6],
                "午":[self.w9, self.w8]
            },
            "己":{
                "巳":[self.w11, self.w10],
                "卯":[self.w4, self.w12],
                "丑":[self.w2, self.w3],
                "亥":[self.w5, self.w],
                "酉":[self.w7, self.w6],
                "未":[self.w9, self.w8]
            },
            "庚":{
                "午":[self.w11, self.w10],
                "辰":[self.w4, self.w12],
                "寅":[self.w2, self.w3],
                "子":[self.w5, self.w],
                "戌":[self.w7, self.w6],
                "申":[self.w9, self.w8]
            },
            "辛":{
                "未":[self.w11, self.w10],
                "巳":[self.w4, self.w12],
                "卯":[self.w2, self.w3],
                "丑":[self.w5, self.w],
                "亥":[self.w7, self.w6],
                "酉":[self.w9, self.w8]
            },
            "壬":{
                "申":[self.w11, self.w10],
                "午":[self.w4, self.w12],
                "辰":[self.w2, self.w3],
                "寅":[self.w5, self.w],
                "子":[self.w7, self.w6],
                "戌":[self.w9, self.w8]
            },
            "癸":{
                "酉":[self.w11, self.w10],
                "未":[self.w4, self.w12],
                "巳":[self.w2, self.w3],
                "卯":[self.w5, self.w],
                "丑":[self.w7, self.w6],
                "亥":[self.w9, self.w8]
            }
        }
        
        大限 = {
            "水二局":{
                "阴女":GridLabelText.accumulate_vector(initial_vector=[2,11], reverse_result=True),
                "阳女":GridLabelText.accumulate_vector(initial_vector=[2,11], reverse_result=False)
            },
            "木三局":{
                "阴女":GridLabelText.accumulate_vector(initial_vector=[3,12], reverse_result=True),
                "阳女":GridLabelText.accumulate_vector(initial_vector=[3,12], reverse_result=False)
            },
            "金四局":{
                "阴女":GridLabelText.accumulate_vector(initial_vector=[4,13], reverse_result=True),
                "阳女":GridLabelText.accumulate_vector(initial_vector=[4,13], reverse_result=False)
            },
            "土五局":{
                "阴女":GridLabelText.accumulate_vector(initial_vector=[5,14], reverse_result=True),
                "阳女":GridLabelText.accumulate_vector(initial_vector=[5,14], reverse_result=False)
            },
            "火六局":{
                "阴女":GridLabelText.accumulate_vector(initial_vector=[6,15], reverse_result=True),
                "阳女":GridLabelText.accumulate_vector(initial_vector=[6,15], reverse_result=False)
            }
        }
        
        小限 = {
            "寅":{
                "男":["辰","巳","午","未"]
            }
        }

        if self.male_or_female == "阳男":
            male_or_female = "阴女"
        elif self.male_or_female == "阴男":
            male_or_female = "阳女"

        支系_window = 支系[self.nianZhi]

        支系_list_label = ["天马", "解神", "天哭", "天虚", "龙池", "凤阁", "红鸾", "天喜", "孤辰", "寡宿", "蜚廉", "破碎", "天空", "月德"]

        长生十二_window = 长生十二[self.wuXingju][male_or_female]
        长生十二_list_label = ["长生","沐浴","冠带","临官","帝旺","衰","病","死","墓","绝","胎","养"]

        截空_window = 截空[self.nianGan]
        截空_list_label = ["正截空","副截空"]

        旬空_window = 旬空[self.nianGan][self.nianZhi]
        旬空_list_label = ["正旬空","副旬空"]

        大限_window = [
            positions[self.Ming][0],positions[self.Ming][11],positions[self.Ming][10],positions[self.Ming][9],
            positions[self.Ming][8],positions[self.Ming][7],positions[self.Ming][6],positions[self.Ming][5],
            positions[self.Ming][4],positions[self.Ming][3],positions[self.Ming][2],positions[self.Ming][1]
            ]

        大限_list_label = 大限[self.wuXingju][male_or_female]

        # 控件名称与变量名映射
        controls = {
            "禄存": 禄存, "擎羊": 擎羊, "陀罗": 陀罗, "天魁": 天魁, "天钺": 天钺,
            "文昌": wenChang, "文曲": wenQu, "火星": huoXing, "铃星": lingXing,
            "左辅": zuofu, "右弼": youbi, "紫微": ziWei_, "天机": tianJi, "太阳": taiYang,
            "武曲": wuQu, "天同": tianTong, "廉贞": lianZhen, "天府": tianFu,
            "太阴": taiYin, "贪狼": tanLang, "巨门": juMen, "天相": 天相,
            "天梁": tianLiang, "七杀": qiSha, "破军": poJun,
            "地劫": diJie, "地空": dikong,
            "台辅": taiFu, "封诰": fengGao, "天刑": tianxing,
            "天姚":tianyao,"天巫": tianwu,
            "天月": tianyue, "阴煞": tiansha, "三台":santai,
            "八座":bazuo, "恩光":enguang,"天贵":tiangui,
            "天寿":天寿,"天官":天官,"天福":天福,"天厨":天厨,"天才":天才,"天使":天使,"天伤":天伤
        }

        # 生成包含控件父窗口的字典
        window_frame = {name: GridLabelText.get_window(widget) for name, widget in controls.items()}

        for i, (win, text) in enumerate(zip(windows, texts)):
            label = ttk.Label(win, text=text, font=self.font_style)
            label.grid(row=10, column=0)

        class_grid.grid_label_text("紫微", ziWei_, 8, 1, window_frame["紫微"])
        class_grid.grid_label_text("天机", tianJi, 8, 1, window_frame["天机"])
        class_grid.grid_label_text("太阳", taiYang, 8, 1, window_frame["太阳"])
        class_grid.grid_label_text("武曲", wuQu, 8, 1, window_frame["武曲"])
        class_grid.grid_label_text("天同", tianTong, 8, 1, window_frame["天同"])
        class_grid.grid_label_text("廉贞", lianZhen, 8, 1, window_frame["廉贞"])
        class_grid.grid_label_text("天府", tianFu, 8, 1, window_frame["天府"])
        class_grid.grid_label_text("太阴", taiYin, 8, 1, window_frame["太阴"])
        class_grid.grid_label_text("贪狼", tanLang, 8, 1, window_frame["贪狼"])
        class_grid.grid_label_text("巨门", juMen, 8, 1, window_frame["巨门"])
        class_grid.grid_label_text("天相", 天相, 8, 1, window_frame["天相"])
        class_grid.grid_label_text("天梁", tianLiang, 8, 1, window_frame["天梁"])
        class_grid.grid_label_text("七杀", qiSha, 8, 1, window_frame["七杀"])
        class_grid.grid_label_text("破军", poJun, 8, 1, window_frame["破军"])

        class_grid.grid_label_text("文昌", wenChang, 8, 1, window_frame["文昌"])
        class_grid.grid_label_text("文曲", wenQu, 8, 1, window_frame["文曲"])
        class_grid.grid_label_text("火星", huoXing, 8, 1, window_frame["火星"])
        class_grid.grid_label_text("铃星", lingXing, 8, 1, window_frame["铃星"])
        class_grid.grid_label_text("左辅", zuofu, 8, 1, window_frame["左辅"])
        class_grid.grid_label_text("右弼", youbi, 8, 1, window_frame["右弼"])
        
        class_grid.grid_label_text("禄存", 禄存, 8, 1, window_frame["禄存"])
        class_grid.grid_label_text("擎羊", 擎羊, 8, 1, window_frame["擎羊"])
        class_grid.grid_label_text("陀罗", 陀罗, 8, 1, window_frame["陀罗"])
        class_grid.grid_label_text("天魁", 天魁, 8, 1, window_frame["天魁"])
        class_grid.grid_label_text("天钺", 天钺, 8, 1, window_frame["天钺"])

        class_grid.grid_label_text("天官", 天官, 7, 1, window_frame["天官"])
        class_grid.grid_label_text("天福", 天福, 7, 1, window_frame["天福"])
        class_grid.grid_label_text("天厨", 天厨, 7, 1, window_frame["天厨"])

        class_grid.grid_label_text("地劫", diJie, 7, 1, window_frame["地劫"])
        class_grid.grid_label_text("地空", dikong, 7, 1, window_frame["地空"])
        class_grid.grid_label_text("台辅", taiFu, 7, 1, window_frame["台辅"])
        class_grid.grid_label_text("封诰", fengGao, 7, 1, window_frame["封诰"])
        class_grid.grid_label_text("天刑", tianxing, 7, 1, window_frame["天刑"])
        class_grid.grid_label_text("天姚", tianyao, 7, 1, window_frame["天姚"])
        class_grid.grid_label_text("天巫", tianwu, 7, 1, window_frame["天巫"])
        class_grid.grid_label_text("天月", tianyue, 7, 1, window_frame["天月"])
        class_grid.grid_label_text("阴煞", tiansha, 7, 1, window_frame["阴煞"])
        class_grid.grid_label_text("三台", santai, 7, 1, window_frame["三台"])
        class_grid.grid_label_text("八座", bazuo, 7, 1, window_frame["八座"])
        class_grid.grid_label_text("恩光", enguang, 7, 1, window_frame["恩光"])
        class_grid.grid_label_text("天贵", tiangui, 7, 1, window_frame["天贵"])

        GridLabelText.get_no_name(class_grid,支系_window, 支系_list_label,self.font_style,7,1)
        GridLabelText.get_no_name(class_grid,长生十二_window, 长生十二_list_label,self.font_style,9,1)
        GridLabelText.get_no_name(class_grid,截空_window, 截空_list_label,self.font_style,7,1)
        GridLabelText.get_no_name(class_grid,旬空_window, 旬空_list_label,self.font_style,7,1)

        class_grid.grid_label_text("天才", 天才, 7, 1, window_frame["天才"])
        class_grid.grid_label_text("天寿", 天寿, 7, 1, window_frame["天寿"])
        class_grid.grid_label_text("天伤", 天伤, 7, 1, window_frame["天伤"])
        class_grid.grid_label_text("天使", 天使, 7, 1, window_frame["天使"])

        GridLabelText.get_no_name(class_grid,大限_window, 大限_list_label,self.font_style,12,0)

        self.window_z.grid_rowconfigure(1, weight=1)
        self.window_z.grid_columnconfigure(1, weight=1)

    '''
        [ self.w  巳 ][ self.w2 午 ][ self.w3 未 ][ self.w4 申 ]
        [ self.w5 辰 ][ w13][     ][ self.w12  酉 ]
        [ self.w6 卯 ][     ][     ][ self.w11 戌]
        [ self.w7 寅 ][ self.w8 丑 ][ self.w9 子 ][ self.w10  亥]
    '''

    