import ctypes
import datetime
import os
import shutil
import threading
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox
from tkinter.ttk import Separator

import dateutil.tz
import pystray
import ttkbootstrap as ttk
import windnd
from PIL import Image
from pystray import MenuItem, Menu
from ttkbootstrap.constants import *

import function.ProjectCapabilityVariables
from ProjectFunctions import t_save, save, t_load, var_save
from function import JsonFile
from function.ProjectDictionaryVariables import UTC_TIME
from function.ProjectPathVariables import A_PATH, B_PATH, C_PATH, H_PATH, I_PATH, J_PATH, \
    K_PATH, L_PATH, M_PATH, N_PATH, R_PATH, S_PATH, T_PATH, W_PATH, X_PATH, Z_PATH, AA_PATH, AB_PATH, \
    W_ROOT2_C_VAR_2_PATH, ICON_PATH, DATA_FILE_PATH
from window_module import NewXiaoLiuRenWindow
from window_module.OldXiaoLiuRenWindow import xiao_liu_ren_window
from window_module.PictureWindow import picture
from window_module.RegressionWindow import regression


def load_theme():
    try:
        with open(B_PATH, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def s():
    global v
    v = v + 1
def s2():
    global v2
    v2 = v2+1
def s3():
    global v3
    v3 = v3+1
def s4():
    global v4
    v4 = v4+1
def s5():
    global v5
    v5 = v5+1
def s6():
    global v6
    v6 = v6+1
def var_num_w_4_3_s():
    global var_num_w_4_3
    var_num_w_4_3 += 1
    t_save(Z_PATH, var_num_w_4_3)
def var2_num_w_4_3_s():
    global var2_num_w_4_3
    var2_num_w_4_3 += 1
    t_save(AA_PATH, var2_num_w_4_3)

def var3_num_w_4_3_s():
    global var3_num_w_4_3
    var3_num_w_4_3 += 1
    t_save(AB_PATH, var3_num_w_4_3)


###分割线
#关于紫微斗数###分割线

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def gadget():

    def triangle():
        pass

    window = ttk.Toplevel(str(root))
    window.title("轻量记事本-小工具")
    window.iconbitmap(ICON_PATH)
    b1 = ttk.Button(window, text="小六壬", style=OUTLINE, command=lambda: xiao_liu_ren_window(root, icon, FONT_STYLE))
    b1.grid(column=0,row=0,padx=10,pady=10)
    b2 = ttk.Button(window, text="紫微斗数", style=OUTLINE, command=lambda: xiao_liu_ren_window(root, FONT_STYLE))
    b2.grid(column=1,row=0,padx=10,pady=10)
    b3 = ttk.Button(window, text="机器学习-回归问题", style=OUTLINE, command=lambda: regression(root))
    b3.grid(column=2,row=0,padx=10,pady=10)
    b4 = ttk.Button(window, text="三角形计算", style=OUTLINE, command=triangle)
    b4.grid(column=3,row=0,padx=10,pady=10)
    b5 = ttk.Button(window, text="图片操作", style=OUTLINE, command=picture)
    b5.grid(column=4,row=0,padx=10,pady=10)
###分割线

#关于设置界面###分割线
# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def set_window():
    child_windows = []

    window = ttk.Toplevel()
    window.resizable(None,None)
    window.title("轻量记事本-设置")
    window.iconbitmap(ICON_PATH)

    # noinspection PyBroadException
    def window_close():
        for win in child_windows:
            try:
                win.destroy()
            except:
                pass
        window.destroy()

    # noinspection PyBroadException
    def window_close_():
        for win in child_windows:
            try:
                win.destroy()
            except:
                pass

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
    def w_root1():

        global theme_cbo

        # noinspection SpellCheckingInspection
        def bao_chun():
            global v2,v3,v4
            p1=v2%2
            p2=v3%2
            p3=v4%2
            window_close_()
            if p1+p2+p3==1:
                save(theme_cbo.get(),v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3)
            else:
                messagebox.showerror("错误", message="不支持多字体或无字体选择",parent=window)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_theme(event):
            theme_cbo_value = theme_cbo.get()
            style.theme_use(theme_cbo_value)
            theme_cbo.selection_clear()

        w_ = ttk.Frame(window)
        w_.grid(row=0,column=0,sticky=W)

        lbl = ttk.Label(w_, text="选择主题:")
        lbl.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        lb2 = ttk.Label(w_, text="选择字体:")
        lb2.grid(column=0,row=1,padx=10,pady=10,ipadx=5)

        window_button_two = ttk.Button(w_, text="返回", style=OUTLINE, command=window_close)
        window_button_two.grid(column=4,row=0,padx=10,pady=10)
        window_button = ttk.Button(w_, text="保存当前设置", style=OUTLINE, command=bao_chun)
        window_button.grid(column=3,row=0,padx=10,pady=10)

        w2 = ttk.Frame(w_)
        w2.grid(row=1,column=1,sticky=W)

        consider_var_2 = ttk.IntVar()
        if v2 % 2 == 1:
            consider_var_2.set(1)
        else:
            consider_var_2.set(0)
        consider_checkbutton2 = ttk.Checkbutton(w2, text="宋体", variable=consider_var_2, command=s2, style="round-toggle")
        consider_checkbutton2.grid(column=1,row=1,padx=10,pady=10)

        consider_var_3 = ttk.IntVar()
        if v3 % 2 == 1:
            consider_var_3.set(1)
        else:
            consider_var_3.set(0)
        consider_checkbutton3 = ttk.Checkbutton(w2, text="等线", variable=consider_var_3, command=s3, style="round-toggle")
        consider_checkbutton3.grid(column=2,row=1,padx=10,pady=10)

        consider_var_4 = ttk.IntVar()
        if v4 % 2 == 1:
            consider_var_4.set(1)
        else:
            consider_var_4.set(0)
        consider_checkbutton4 = ttk.Checkbutton(w2, text="黑体", variable=consider_var_4, command=s4, style="round-toggle")
        consider_checkbutton4.grid(column=3,row=1,padx=10,pady=10)

        w4 = ttk.Frame(w_)
        w4.grid(row=0,column=1,sticky=W)

        style = ttk.Style()
        theme_names = style.theme_names()
        theme_cbo = ttk.Combobox(master=w4, values=theme_names, state="readonly")
        theme_cbo.grid(column=1,row=0,padx=10,pady=10)
        theme_cbo.current(theme_names.index(style.theme_use()))
        theme_cbo.bind('<<ComboboxSelected>>', change_theme)

    w_root1()

    sep = Separator(window, orient='horizontal')
    sep.grid(column=0, row=1,pady=30,sticky='ew',columnspan=2)

    def w_root2():

        var2 = int(t_load(W_ROOT2_C_VAR_2_PATH) or 0)

        w_2 = ttk.Frame(window)
        w_2.grid(row=2,column=0,sticky=W)

        lb3 = ttk.Label(w_2, text="关联设置:")
        lb3.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        consider_var = ttk.IntVar()
        if v % 2 == 1:
            consider_var.set(1)
        else:
            consider_var.set(0)
        consider_checkbutton = ttk.Checkbutton(w_2, text="是否关联上一次保存的文件", variable=consider_var, command=s, style="round-toggle")
        consider_checkbutton.grid(column=1,row=0,padx=10,pady=10)

        consider_var_2 = ttk.IntVar()
        if var2 % 2 == 1:
            consider_var_2.set(1)
        else:
            consider_var_2.set(0)
        consider_checkbutton_2 = ttk.Checkbutton(w_2, text="用户选择为主", variable=consider_var_2, command=lambda:var_save(W_ROOT2_C_VAR_2_PATH, var2), style="round-toggle")
        consider_checkbutton_2.grid(column=2, row=0, padx=10, pady=10)

    w_root2()

    sep2 = Separator(window, orient='horizontal')
    sep2.grid(column=0, row=3,pady=30,sticky='ew',columnspan=2)

    def w_root3():
        w_3 = ttk.Frame(window)
        w_3.grid(row=4,column=0,sticky=W)


        lb4 = ttk.Label(w_3, text="文件设置:")
        lb4.grid(column=0,row=0,padx=10,pady=10,ipadx=5,sticky=W)

        w5 = ttk.Frame(w_3)
        w5.grid(row=0,column=1,sticky=W)

        # noinspection PyGlobalUndefined
        def combobox():
            global combobox1,combobox2,combobox0,combobox3

            w5lb0 = ttk.Label(w5, text="区分文件:")
            w5lb0.grid(column=0,row=0,padx=10,pady=10)
            w5lb3 = ttk.Label(w5, text="文件循环导入值:")
            w5lb3.grid(column=0,row=1,padx=10,pady=10)
            w5lb1 = ttk.Label(w5, text="大文件定义:")
            w5lb1.grid(column=0,row=2,padx=10,pady=10)
            w5lb2 = ttk.Label(w5, text="大文件分割:")
            w5lb2.grid(column=0,row=3,padx=10,pady=10)

            combobox2_group1 = ["等于大文件定义","5MB","10MB","15MB","30MB"]
            combobox1_group1 = [ "50MB", "70MB", "128MB", "256MB", "512MB"]
            combobox0_group1 = ["开启","关闭"]
            combobox3_group1 = ["5MB","10MB","30MB","50MB","70MB", "128MB", "256MB", "512MB"]

            combobox1 = ttk.Combobox(master=w5, values=combobox1_group1, state="readonly")
            combobox1.grid(row=2, column=2,padx=10,pady=10)

            combobox2 = ttk.Combobox(master=w5, values=combobox2_group1, state="readonly")
            combobox2.grid(row=3, column=2,padx=10,pady=10)

            combobox0 = ttk.Combobox(master=w5, values=combobox0_group1, state="readonly")
            combobox0.grid(row=0, column=2,padx=10,pady=10)

            combobox3 = ttk.Combobox(master=w5, values=combobox3_group1, state="readonly")
            combobox3.grid(row=1, column=2,padx=10,pady=10)
            combobox0.set("开启")
            combobox1.set("70MB")
            combobox2.set("等于大文件定义")
            combobox3.set("30MB")

            match _size_:
                case "70MB" | "50MB" | "128MB" | "256MB" | "512MB":
                    combobox1.set(_size_)
                case _:
                    combobox1.set("70MB")
                    save(theme_cbo.get(),v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3)

            match divide_up:
                case "等于大文件定义" | "5MB" | "10MB" | "15MB" | "30MB":
                    combobox2.set(divide_up)
                case _:
                    combobox2.set("70MB")
                    save(theme_cbo.get(),v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3)

            match onandoff:
                case "开启" | "关闭":
                    combobox0.set(onandoff)
                case "关闭":
                    combobox0.set("开启")
                    save(theme_cbo.get(),v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3)

            match circular:
                case "5MB" | "10MB" | "30MB" | "50MB" | "70MB" | "128MB" | "256MB" | "512MB":
                    combobox3.set(circular)
                case _:
                    save(theme_cbo.get(),v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3)
        combobox()

    w_root3()

    sep3 = Separator(window, orient='horizontal')
    sep3.grid(column=0, row=5,pady=30,sticky='ew',columnspan=2)

    def w_root4():

        w_4 = ttk.Frame(window)
        w_4.grid(row=6,column=0,sticky=W)

        w_4_1 = ttk.Frame(w_4)
        w_4_1.grid(column=1,row=0,sticky=W)

        def w_root4_row6():
            w_4_row_6 = ttk.Frame(window)
            w_4_row_6.grid(row=6,column=1,sticky=W)

            w_4_2 = ttk.Frame(w_4_row_6)
            w_4_2.grid(column=1,row=0,sticky=W)

            w_4_3 = ttk.Frame(w_4_row_6)
            w_4_3.grid(column=1,row=1,sticky=W)

            w_4_3_1 = ttk.Frame(w_4_3)
            w_4_3_1.grid(column=1,row=2,sticky=W)

            lb7 = ttk.Label(w_4_row_6, text="紫微斗数:")
            lb7.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

            lb8 = ttk.Label(w_4_row_6, text="图片操作:")
            lb8.grid(column=0,row=1,padx=10,pady=10,ipadx=5)

            w_4_2_lb1 = ttk.Label(w_4_2, text="界面样式：")
            w_4_2_lb1.grid(column=0,row=0,padx=5,pady=5)

            w_4_2_lb2 = ttk.Label(w_4_2, text="闰月问题：")
            w_4_2_lb2.grid(column=0,row=1,padx=5,pady=5)

            w_4_2_lb3 = ttk.Label(w_4_2, text="时辰问题：")
            w_4_2_lb3.grid(column=0,row=2,padx=5,pady=5)

            w_4_3_lb1 = ttk.Label(w_4_3, text="颜色输入：")
            w_4_3_lb1.grid(column=0,row=0,padx=5,pady=5)

            w_4_3_lb2 = ttk.Label(w_4_3, text="色彩空间：")
            w_4_3_lb2.grid(column=0,row=1,padx=5,pady=5)

            w_4_3_lb3 = ttk.Label(w_4_3, text="精灵图文件导出：")
            w_4_3_lb3.grid(column=0,row=2,padx=5,pady=5)

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
            def w_4_3_():

                def down_box_save_1():
                    with open(W_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box.get()))

                def down_box_save_2():
                    with open(X_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box2.get()))

                def w_4_3_load():
                    try:
                        with open(W_PATH, 'r', encoding='utf-8') as file:
                            return file.read()
                    except FileNotFoundError:
                        pass

                def w_4_3_load_2():
                    try:
                        with open(X_PATH, 'r', encoding='utf-8') as file:
                            return file.read()
                    except FileNotFoundError:
                        pass

                down_box = ttk.Combobox(w_4_3, values=["颜色选择器", "十六进制", "RGB值"], state="readonly")
                down_box.grid(row=0, column=1, padx=5, pady=5)
                down_box.bind("<<ComboboxSelected>>", lambda event: down_box_save_1())
                t = str(w_4_3_load() or "颜色选择器")
                match t:
                    case "颜色选择器" | "十六进制" | "RGB值":
                        down_box.set(t)
                    case _:
                        down_box.set("颜色选择器")
                        down_box_save_1()

                down_box2 = ttk.Combobox(w_4_3, values=["RGBA", "RGB"], state="readonly")
                down_box2.grid(row=1, column=1, padx=5, pady=5)
                down_box2.bind("<<ComboboxSelected>>", lambda event: down_box_save_2())
                t_ = str(w_4_3_load_2() or "RGBA")
                match t_:
                    case "RGBA" | "RGB":
                        down_box2.set(t_)
                    case _:
                        down_box2.set("RGBA")
                        down_box_save_2()

                var_num_w_4_3 = int(t_load(Z_PATH) or 1)
                var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
                var3_num_w_4_3 = int(t_load(AB_PATH) or 0)

                w_4_3_var = ttk.IntVar()
                if var_num_w_4_3 % 2 == 1:
                    w_4_3_var.set(1)
                else:
                    w_4_3_var.set(0)
                w_4_3_var_ = ttk.Checkbutton(w_4_3_1, text="PNG", variable=w_4_3_var, command=var_num_w_4_3_s, style="round-toggle")
                w_4_3_var_.grid(column=0,row=0,padx=5,pady=5)

                w_4_3_var2 = ttk.IntVar()
                if var2_num_w_4_3 % 2 == 1:
                    w_4_3_var2.set(1)
                else:
                    w_4_3_var2.set(0)
                w_4_3_var2_ = ttk.Checkbutton(w_4_3_1, text="CSS", variable=w_4_3_var2, command=var2_num_w_4_3_s, style="round-toggle")
                w_4_3_var2_.grid(column=1,row=0,padx=5,pady=5)

                w_4_3_var3 = ttk.IntVar()
                if var3_num_w_4_3 % 2 == 1:
                    w_4_3_var3.set(1)
                else:
                    w_4_3_var3.set(0)
                w_4_3_var3_ = ttk.Checkbutton(w_4_3_1, text="HTML", variable=w_4_3_var3, command=var3_num_w_4_3_s, style="round-toggle")
                w_4_3_var3_.grid(column=2,row=0,padx=5,pady=5)

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
            def w_4_2_():

                def event_t():
                    with open(R_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box.get()))
                    w_root5()

                def down_box2_save():
                    with open(S_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box2.get()))

                def down_box3_save():
                    with open(T_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box3.get()))

                down_box = ttk.Combobox(w_4_2, values=["横排样式", "竖排样式", "自定义样式【未完成】"], state="readonly")
                down_box.grid(row=0, column=1, padx=5, pady=5)
                down_box.bind("<<ComboboxSelected>>", lambda event: event_t())
                t = str(t_load(R_PATH) or "横排样式")
                match t:
                    case "横排样式" | "竖排样式":
                        down_box.set(t)
                    case _:
                        down_box.set("横排样式")
                        event_t()

                down_box2 = ttk.Combobox(w_4_2, values=["作本月", "作下月", "月中为界"], state="readonly")
                down_box2.grid(row=1, column=1, padx=5, pady=5)
                down_box2.bind("<<ComboboxSelected>>", lambda event: down_box2_save())
                t2 = str(t_load(S_PATH) or "作下月")
                match t2:
                    case "作下月" | "作本月" | "月中为界":
                        down_box2.set(t2)
                    case _:
                        down_box2.set("作下月")
                        down_box2_save()

                down_box3 = ttk.Combobox(w_4_2, values=["子时视明日", "子时视本日", "子时中而分界"], state="readonly")
                down_box3.grid(row=2, column=1, padx=5, pady=5)
                down_box3.bind("<<ComboboxSelected>>", lambda event: down_box3_save())
                t3 = str(t_load(T_PATH) or "子时视明日")
                match t3:
                    case "子时视明日" | "子时视本日" | "子时中而分界":
                        down_box3.set(t3)
                    case _:
                        down_box3.set("子时视明日")
                        down_box3_save()

            w_4_3_()

            w_4_2_()

        lb6 = ttk.Label(w_4, text="小六壬:")
        lb6.grid(column=0,row=0,padx=10,pady=10,ipadx=5)        

        consider_var = ttk.IntVar()
        if v5 % 2 == 1:
            consider_var.set(1)
        else:
            consider_var.set(0)
        consider_checkbutton = ttk.Checkbutton(w_4_1, text="使用三宫定义", variable=consider_var, command=s5, style="round-toggle")
        

        consider_var2 = ttk.IntVar()
        if v6 % 2 == 1:
            consider_var2.set(1)
        else:
            consider_var2.set(0)
        consider_checkbutton2 = ttk.Checkbutton(w_4_1, text="不计算吉值", variable=consider_var2, command=s6, style="round-toggle")
        
        consider_checkbutton.grid(column=0,row=4,padx=10,pady=10,sticky=W)
        consider_checkbutton2.grid(column=0,row=5,padx=10,pady=10,sticky=W)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def w_4_1_():

            xlr_data = {
                "起卦历法": 0,
                "起卦时间": 0,
                "起卦时区": 0,
                "起卦方式": 0,
            }

            xlr_data_path = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
            xlr_json = JsonFile.File.dict_load(xlr_data_path, xlr_data)

            w_4_1_v_0 = ["新历","农历","道历"]
            w_4_1_v_1 = ["时区","平太阳时","真太阳时"]
            w_4_1_v_3 = ["时起卦", "随机数起卦", "五行起卦", "八卦起卦", "八卦五行起卦"]

            def utc():
                local_timezone = dateutil.tz.tzlocal()
                now = datetime.now(local_timezone)
                offset = now.strftime('%z')
                formatted_offset = f"UTC{offset[:3]}:{offset[3:]}"
                var2 = int(t_load(W_ROOT2_C_VAR_2_PATH) or 0)
                if xlr_json[2] != UTC_TIME.index(formatted_offset):
                    if var2 % 2 == 1:
                        down_box_2.set(UTC_TIME[int(xlr_json[2])])
                    else:
                        down_box_2.set(UTC_TIME[UTC_TIME.index(formatted_offset)])
                        xlr_json[2] = UTC_TIME.index(formatted_offset)
                        JsonFile.File.dict_save(xlr_data_path, xlr_json.file_dict)
                else:
                    down_box_2.set(UTC_TIME[UTC_TIME.index(formatted_offset)])
                down_box_0.set(w_4_1_v_0[xlr_json[0]])
                down_box_1.set(w_4_1_v_1[xlr_json[1]])
                down_box_3.set(w_4_1_v_3[xlr_json[3]])

            def modify_xlr_json():
                
                print(down_box_0.get(),down_box_1.get(),down_box_2.get(),down_box_3.get())

                xlr_json[0] = w_4_1_v_0.index(down_box_0.get())

                xlr_json[1] = w_4_1_v_1.index(down_box_1.get())

                xlr_json[2] = UTC_TIME.index(down_box_2.get())

                xlr_json[3] = w_4_1_v_3.index(down_box_3.get())

                JsonFile.File.dict_save(xlr_data_path, xlr_json.file_dict)

            w_4_1_f_1 = ttk.Frame(w_4_1)

            w_4_1_text_0 = ttk.Label(w_4_1_f_1,text="起卦历法:")
            w_4_1_text_1 = ttk.Label(w_4_1_f_1, text="起卦时间:")
            w_4_1_text_2 = ttk.Label(w_4_1_f_1, text="起卦时区:")
            w_4_1_text_3 = ttk.Label(w_4_1_f_1, text="起卦方法:")

            down_box_0 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_0, state="readonly")
            down_box_0.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_1 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_1, state="readonly")
            down_box_1.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_2 = ttk.Combobox(w_4_1_f_1, values=UTC_TIME, state="readonly")
            down_box_2.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_3 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_3, state="readonly")
            down_box_3.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            messagebox.showerror("错误", message=f"{xlr_json}", parent=w_4) if isinstance(xlr_json,Exception) else utc()

            w_4_1_f_1.grid(row=0,column=0,padx=10,pady=10,sticky=W)

            w_4_1_text_0.grid(row=0,column=0,padx=5,pady=5,sticky=W)
            w_4_1_text_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_2.grid(row=2, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_3.grid(row=3, column=0, padx=5, pady=5, sticky=W)
            down_box_0.grid(row=0, column=1, padx=5, pady=5, sticky=W)
            down_box_1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            down_box_2.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            down_box_3.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        w_4_1_()

        w_root4_row6()


    w_root4()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
    def w_root5():

        t = str(t_load(R_PATH) or "横排样式")

        def w_root5_window1_():
                w_root5_window1 = ttk.Toplevel()
                child_windows.append(w_root5_window1)
                w_root5_window1.resizable(None,None)
                w_root5_window1.title("轻量记事本-界面示例")
                w_root5_window1.iconbitmap(ICON_PATH)
                text = tk.Label(w_root5_window1,text="年:")
                text.grid(column=0,row=0,padx=5,pady=5)
                text = tk.Label(w_root5_window1,text="月:")
                text.grid(column=2,row=0,padx=5,pady=5)
                text = tk.Label(w_root5_window1,text="日:")
                text.grid(column=4,row=0,padx=5,pady=5)
                text = tk.Label(w_root5_window1,text="时:")
                text.grid(column=6,row=0,padx=5,pady=5)
                text5 = tk.Label(w_root5_window1,text="性别:")
                text5.grid(column=8,row=0,padx=5,pady=5)
                entry = tk.Entry(w_root5_window1)
                entry.grid(column=1,row=0,padx=5,pady=5)
                entry2 = tk.Entry(w_root5_window1)
                entry2.grid(column=3,row=0,padx=5,pady=5)
                entry3 = tk.Entry(w_root5_window1)
                entry3.grid(column=5,row=0,padx=5,pady=5)
                entry4 = tk.Entry(w_root5_window1)
                entry4.grid(column=7,row=0,padx=5,pady=5)
                combobox = ttk.Combobox(master=w_root5_window1, values=["男", "女", "其它"])
                combobox.grid(row=0, column=9,padx=10,pady=10)

        def w_root5_window2_():
                w_root5_window2 = ttk.Toplevel()
                child_windows.append(w_root5_window2)
                w_root5_window2.resizable(None,None)
                w_root5_window2.title("轻量记事本-界面示例")
                w_root5_window2.iconbitmap(ICON_PATH)
                text2_2 = tk.Label(w_root5_window2,text="年:")
                text2_2.grid(column=0,row=0,padx=5,pady=5)
                text3_2 = tk.Label(w_root5_window2,text="月:")
                text3_2.grid(column=0,row=1,padx=5,pady=5)
                text4_2 = tk.Label(w_root5_window2,text="日:")
                text4_2.grid(column=0,row=2,padx=5,pady=5)
                text5_2 = tk.Label(w_root5_window2,text="时:")
                text5_2.grid(column=0,row=3,padx=5,pady=5)
                text5 = tk.Label(w_root5_window2,text="性别:")
                text5.grid(column=0,row=4,padx=5,pady=5)
                entry1_2 = tk.Entry(w_root5_window2)
                entry1_2.grid(column=1,row=0,padx=5,pady=5)
                entry2_2 = tk.Entry(w_root5_window2)
                entry2_2.grid(column=1,row=1,padx=5,pady=5)
                entry3_2 = tk.Entry(w_root5_window2)
                entry3_2.grid(column=1,row=2,padx=5,pady=5)
                entry4_2 = tk.Entry(w_root5_window2)
                entry4_2.grid(column=1,row=3,padx=5,pady=5)
                combobox = ttk.Combobox(master=w_root5_window2, values=["男", "女", "其它"])
                combobox.grid(row=4, column=1,padx=10,pady=10)

        match t:
            case "横排样式":
                w_root5_window1_()
            case "竖排样式":
                w_root5_window2_()

    w_root5()

    window.protocol("WM_DELETE_WINDOW", window_close)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()
###分割线

#关于主界面###分割线
def quit_window():
    root.destroy()

def show_window():
    root.deiconify()

def on_exit():
    root.withdraw()


# noinspection PyPep8Naming
def 前_下拉框事件():
        if 下拉框.get() == "保存":
            save_t()
        elif 下拉框.get() == "设置":
            set_window()
        elif 下拉框.get() == "小工具":
            gadget()

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()


# noinspection PyUnusedLocal
def a(event):
     deleted_text.append(text_widget.get('1.0', tk.END))
     text_widget.delete('1.0', tk.END)
deleted_text = []
def b():
    if deleted_text:
        deleted_content = deleted_text.pop()
        text_widget.insert(tk.END, deleted_content)

def c():
    text_widget.insert(tk.END, "\n")

def on():
    text_widget.tag_configure("found", background="")
    toggle_window()

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def two_window():
    global window2

    # noinspection PyPep8Naming
    def mySearch():
        text_widget.tag_remove("found","1.0",END)
        start = "1.0"
        key = entry.get()
        if len(key.strip()) == 0:
            return
        while True:
            pos = text_widget.search(key,start,END)
            if pos == "":
                break
            text_widget.tag_add("found",pos,"%s+%dc" %(pos,len(key)))
            start = "%s+%dc" % (pos,len(key))
    def focus2():
        entry2.focus_set()
    def focus1():
        entry.focus_set()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyAssignmentToLoopOrWithParameter
    def replace():
        k = entry.get()
        f = entry2.get()
        t = text_widget.get(1.0, tk.END)
        new_text = t.replace(k, f)
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, new_text)
    if not window2:
        window2 = tk.Toplevel()
        window2.title("查找与替换")
        window2.iconbitmap(ICON_PATH)
        window2.resizable( width=False, height=False )
        window2.wm_attributes("-topmost", True)
        lbl = ttk.Label(window2, text="查找:")
        lbl.grid(row=0, column=0, padx=5, pady=5)
        entry = tk.Entry(window2, width=30)
        entry.grid(row=0, column=1,padx=5,pady=5)
        entry.bind("<Return>", lambda event: mySearch())
        entry.focus_set()
        lb2 = ttk.Label(window2, text="替换:")
        lb2.grid(row=1, column=0, padx=5, pady=5)
        entry2 = tk.Entry(window2, width=30)
        entry2.grid(row=1, column=1,padx=5,pady=5)
        entry2.bind("<Return>", lambda event: replace())
        window2.protocol("WM_DELETE_WINDOW", on)
        window2.bind("<Control-f> ", lambda event:toggle_window())
        entry.bind("<Control-f> ", lambda event:toggle_window())
        entry.bind(" <Down>",lambda event:focus2())
        entry2.bind("<Up>",lambda event:focus1())
        entry2.bind("<Control-f> ", lambda event:toggle_window())
        window2.mainloop()

def toggle_window():
    global window2
    if window2:
        # noinspection PyUnresolvedReferences
        window2.destroy()
        window2 = None
    else:
        two_window()

def save_2():
    def save_2t():
        file_path = filedialog.asksaveasfilename(parent=root, defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])

        with open(A_PATH, 'w', encoding='utf-8') as file:
             lines = text_widget.get("1.0","end")
             file.writelines(lines)

        if file_path:
            shutil.copy(A_PATH, file_path)

    thread = threading.Thread(target=save_2t)
    thread.start()

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def read(filename, msg):
    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyAssignmentToLoopOrWithParameter
    def read_and_split():
        global index,index_,t_size
        with open(msg, 'r',encoding='utf-8',errors = 'ignore') as file:
            index = 0
            while True:
                file.seek(index * t_divide_up)
                data = file.read(t_divide_up)
                if not data:
                    folder = os.path.join(DATA_FILE_PATH, "text-temp")
                    try:
                        os.mkdir("text-temp")
                    except:
                        shutil.rmtree(folder)
                        os.mkdir("text-temp")
                    index -= 1
                    progressbarOne['value'] -= 1
                    while True:
                        progressbarOne['value'] += 1
                        try:
                            shutil.move(f'{filename}_{index}', folder)
                            index -= 1
                        except:
                            try:
                                os.remove(f'{filename}_{index}')
                            except:
                                index = 0
                                index_ = 1
                                folder_t = (folder + "\\" + f'{filename}_{index}')

                                size = os.path.getsize(msg)
                                division = size//t_divide_up
                                division08=division*0.1
                                progressbarOne['value'] -= division08

                                with open(folder_t, 'r',encoding='utf-8',errors = 'ignore') as file:
                                    a = file.read()
                                    progressbarOne['value'] += division08
                                    text_widget.insert(tk.END, a)
                                    window3.destroy()
                                    root.attributes("-disabled", 0)
                            break
                    break

                with open(f'{filename}_{index}', 'w',encoding='utf-8',errors = 'ignore') as file:
                    file.write(str(data))
                index += 1
                progressbarOne['value'] += 1


    thread = threading.Thread(target=read_and_split)
    thread.start()


# noinspection PyGlobalUndefined
def save_ff():

    global progressbarOne2

    def save_tf():

     # noinspection PyBroadException,PyShadowingNames
     def save_tt():
         folder = os.path.join(DATA_FILE_PATH, "text-temp")
         filename_ = os.path.join(folder, f'{filename}')
         index = 0
         while True:
             try:
                 folder_t = (folder + "\\" + f'{filename}_{index}')
                 with open(folder_t, 'r',encoding='utf-8',errors = 'ignore') as file:
                     a = file.read()
                     index += 1
                 with open(filename_,'a',encoding='utf-8',errors = 'ignore') as file:
                     file.write(a)
                     progressbarOne2['value'] += 1
             except:
                 index -= 1
                 print(index)
                 division08=division*0.1
                 progressbarOne2['value'] -= division08
                 shutil.copy(filename_, msg)
                 progressbarOne2['value'] += division08
                 window4.destroy()
                 root.attributes("-disabled", 0)
                 icon.notify("文件已成功保存", "Lightweight text editor")
                 break
     thread = threading.Thread(target=save_tt)
     thread.start()

    size = os.path.getsize(msg)
    division = size//t_divide_up
    window4 = tk.Toplevel(root)
    window4.title("保存")
    window4.resizable(None, None)
    window4.iconbitmap(ICON_PATH)
    window4.minsize(400, 50)
    window4.maxsize(400, 50)
    window4.wm_attributes("-topmost", True)
    root.attributes("-disabled", 1)
    lbl = ttk.Label(window4, text="正在保存中")
    lbl.pack(padx=5, pady=5)
    def on2():
        messagebox.showerror("错误", message="正在保存中，请勿退出",parent=window4)
    progressbarOne2 = ttk.Progressbar(window4,style="striped")
    progressbarOne2.pack(pady=5,fill=X)
    progressbarOne2['maximum'] = division
    progressbarOne2['value'] = 0
    window4.protocol("WM_DELETE_WINDOW", on2)
    save_tf()
    window4.mainloop()


# noinspection PyBroadException,PyShadowingNames
def save_t():
    try:
     size = os.path.getsize(msg)
     filename = os.path.basename(msg)
     if os.path.exists(msg):
        if size < t_size:
            with open(msg, 'w', encoding='utf-8') as file:
                lines = text_widget.get("1.0","end")
                file.writelines(lines)
                icon.notify("文件已成功保存", "Lightweight text editor")
        else:
            if index_ ==  1:
                folder = os.path.join(DATA_FILE_PATH, "text-temp")
                folder_t = (folder + "\\" + f'{filename}_{index}')
                with open(folder_t, 'w',encoding='utf-8') as file:
                    lines = text_widget.get("1.0","end")
                    file.writelines(lines)
                    save_ff()
            else:
                pass
     else:
        save_2()
    except:
        save_2()


# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
def i(files):
    global progressbarOne,window3,filename,t_size,msg
    msg = '\n'.join((item.decode('gbk') for item in files))
    filename = os.path.basename(msg)
    size = os.path.getsize(msg)

    if size < t_size:
        with open(msg, 'r', encoding='utf-8') as file:
            data = file.read()
            text_widget.insert(tk.END, data)

    elif onandoff == "关闭":

        # noinspection PyShadowingNames
        def save_ttt():
            icon.notify("正在导入文件，不建议操作当前窗口", "Lightweight text editor")
            with open(msg, 'r', encoding='utf-8') as file:

                while True:

                    data = file.readlines(circular_num)

                    if not data:
                        icon.notify("导入成功", "Lightweight text editor")
                        break

                    text_widget.insert(tk.END, ''.join(data))

        thread = threading.Thread(target=save_ttt)
        thread.start()

    else:
        size = os.path.getsize(msg)
        division = size//t_divide_up
        window3 = tk.Toplevel(root)
        window3.title("导入")
        window3.resizable(None, None)
        window3.iconbitmap(ICON_PATH)
        window3.minsize(400, 50)
        window3.maxsize(400, 50)
        window3.wm_attributes("-topmost", True)
        root.attributes("-disabled", 1)
        lbl = ttk.Label(window3, text="正在导入中")
        lbl.pack(padx=5, pady=5)
        def on2():
            messagebox.showerror("错误", message="导入过程中，请勿退出",parent=window3)
        progressbarOne = ttk.Progressbar(window3,style="striped")
        progressbarOne.pack(pady=5,fill=X)
        progressbarOne['maximum'] = division
        progressbarOne['value'] = 0
        window3.protocol("WM_DELETE_WINDOW", on2)
        read(filename, msg)
        window3.mainloop()


# noinspection PyBroadException,PyGlobalUndefined
def next_page():
    global index,index_
    if index_ ==  1:
        try:
         index += 1
         folder = os.path.join(DATA_FILE_PATH, "text-temp")
         folder_t = (folder + "\\" + f'{filename}_{index}')
         with open(folder_t, 'r',encoding='utf-8') as file:
             text_widget.delete('1.0', tk.END)
             next_page_text = file.read()
             text_widget.insert(tk.END, next_page_text)
        except:
            messagebox.showerror("错误", message="已经是尾页",parent=root)
            index -= 1
            folder = os.path.join(DATA_FILE_PATH, "text-temp")
            folder_t = (folder + "\\" + f'{filename}_{index}')
            with open(folder_t, 'r',encoding='utf-8') as file:
             text_widget.delete('1.0', tk.END)
             next_page_text = file.read()
             text_widget.insert(tk.END, next_page_text)
    else:
        messagebox.showerror("错误", message="仅限大文件操作",parent=root)


# noinspection PyBroadException
def return_page():
    global index,index_
    if index_ ==  1:
        try:
         index -= 1
         folder = os.path.join(DATA_FILE_PATH, "text-temp")
         folder_t = (folder + "\\" + f'{filename}_{index}')
         with open(folder_t, 'r',encoding='utf-8') as file:
             text_widget.delete('1.0', tk.END)
             return_page_text = file.read()
             text_widget.insert(tk.END, return_page_text)
        except:
            messagebox.showerror("错误", message="已经是首页",parent=root)
            index += 1
            folder = os.path.join(DATA_FILE_PATH, "text-temp")
            folder_t = (folder + "\\" + f'{filename}_{index}')
            with open(folder_t, 'r',encoding='utf-8') as file:
             text_widget.delete('1.0', tk.END)
             return_page_text = file.read()
             text_widget.insert(tk.END, return_page_text)
    else:
        messagebox.showerror("错误", message="仅限大文件操作",parent=root)

def sever():
    w.grid_forget()
    window = tk.Toplevel(root)
    window.title("分离控制")
    window.resizable(None, None)
    window.iconbitmap(ICON_PATH)
    window.minsize(400, 50)
    window.maxsize(400, 50)
    sever_window_b2 = ttk.Button(window, text="下一页", style="link", command=next_page)
    sever_window_b2.pack(padx=5, pady=5, side='right')
    sever_window_b3 = ttk.Button(window, text="上一页", style="link", command=return_page)
    sever_window_b3.pack(padx=5, pady=5, side='right')
    def on2():
        window.destroy()
        w.grid(row=2,column=0,sticky=E)
    b4 = ttk.Button(window, text="取消分离", style="link", command=on2)
    b4.pack(padx=5,pady=5,side='left')
    window.protocol("WM_DELETE_WINDOW", on2)
    window.mainloop()

if __name__ == '__main__':
    v = int(t_load(C_PATH) or 0)
    v5 = int(t_load(L_PATH) or 0)
    v6 = int(t_load(M_PATH) or 0)
    num_wv1 = int(t_load(N_PATH) or 0)
    var_num_w_4_3 = int(t_load(Z_PATH) or 1)
    var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
    var3_num_w_4_3 = int(t_load(AB_PATH) or 0)
    _size_ = (t_load(H_PATH) or "70MB")
    divide_up = (t_load(I_PATH) or "等于大文件定义")
    # noinspection SpellCheckingInspection
    onandoff = (t_load(J_PATH) or "开启")
    circular = (t_load(K_PATH) or "30MB")
    menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
    image = Image.open(ICON_PATH)
    icon = pystray.Icon("icon", image, "轻量记事本", menu)
    root = tk.Tk()
    root.title("轻量记事本")
    root.iconbitmap(ICON_PATH)
    FONT_STYLE,v2,v3,v4 = function.ProjectCapabilityVariables.font_set()
    t_size = 0
    t_divide_up = 0
    circular_num = 31457280
    size_map = {
        "70MB": 73400320,
        "50MB": 52428800,
        "128MB": 134217728,
        "256MB": 268435456,
        "512MB": 536870912
    }
    divide_map = {
        "5MB": 5242880,
        "10MB": 10485760,
        "15MB": 15728640,
        "30MB": 31457280,
        "等于大文件定义": None
    }

    if _size_ in size_map:
        t_size = size_map[_size_]
        if divide_up == "等于大文件定义":
            t_divide_up = t_size
        else:
            t_divide_up = divide_map.get(divide_up, 31457280)
    circular_map = {
        "5MB": 5242880,
        "10MB": 10485760,
        "30MB": 31457280,
        "50MB": 52428800,
        "70MB": 73400320,
        "128MB": 134217728,
        "256MB": 268435456,
        "512MB": 536870912
    }
    circular_num = circular_map.get(circular, 31457280)

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor / 75)
    style = ttk.Style()
    current_theme = load_theme()
    if current_theme in style.theme_names():
        style.theme_use(current_theme)
    下拉菜单组 = ["保存", "设置","小工具"]
    下拉框 = ttk.Combobox(root, values=下拉菜单组, state="readonly")
    下拉框.grid(row=0, column=0, sticky="e",pady=5)
    下拉框.bind("<Button-3>", 下拉框事件)
    下拉框.set("保存")
    scrollbar = ttk.Scrollbar(root, style="round")
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_widget = tk.Text(root, wrap="word",
                          yscrollcommand=scrollbar.set, font=FONT_STYLE)
    text_widget.grid(row=1, column=0, sticky="nsew")
    text_widget.tag_configure("found", background="yellow")
    t=text_widget.get("1.0",tk.END)
    text_widget.focus_set()
    w = ttk.Frame(root)
    w.grid(row=2,column=0,sticky=E)
    b1 = ttk.Button(w, text="分离控制", style="link", command=sever)
    b1.pack(padx=5,pady=5,side='left')
    b2 = ttk.Button(w, text="下一页", style="link", command=next_page)
    b2.pack(padx=5,pady=5,side='right')
    b3 = ttk.Button(w, text="上一页", style="link", command=return_page)
    b3.pack(padx=5,pady=5, side='right')
    window2 = None
    windnd.hook_dropfiles(root,func=i)
    root.protocol('WM_DELETE_WINDOW', on_exit)
    threading.Thread(target=icon.run, daemon=True).start()
    root.bind("<Control-z> ", a)
    root.bind("<Control-y>", lambda event: b())
    root.bind("<Shift_L>",lambda event: c())
    root.bind("<Control-f> ", lambda event:toggle_window())
    scrollbar.config(command=text_widget.yview)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    index_ = 0

    action_map = {
        1: lambda: (root.withdraw(), xiao_liu_ren_window(root, icon, FONT_STYLE)),    }

    action_map.get(num_wv1 % 2, lambda: None)()

    try:
        if v % 2 == 1:
            text_widget.delete('1.0', tk.END)
            with open(A_PATH, 'r', encoding='utf-8') as f_:
                data = f_.read()
                text_widget.insert(tk.END, data)
    except Exception as error:
        messagebox.showerror("错误", f"发生错误: {error}")

    NewX = NewXiaoLiuRenWindow.NewX(root)

    root.mainloop()