import io
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import ctypes
import os
import shutil
import pystray
from PIL import Image
from pystray import MenuItem, Menu
import threading
import windnd
from tkinter.ttk import Separator
from tkinter import messagebox
from XiaoLliuren import g_path
import XiaoLliuren
import tkinter.ttk
import re
from PIL import Image
import pandas as pd
import msvcrt
import wmi

def get_pid_by_name(process_name):
    pid = None
    c = wmi.WMI()
    for process in c.Win32_Process():
        if process.Name == process_name:
            pid = process.ProcessId
            break
    return pid

def save(theme):
    with open(b_path, 'w',encoding='utf-8') as file:
        file.write(theme)
    with open(c_path, 'w',encoding='utf-8') as file:
        file.write(str(v))
    with open(d_path,"w",encoding='utf-8')as f:
        f.write(str(v2))
    with open(e_path,"w",encoding='utf-8')as f:
        f.write(str(v3))
    with open(f_path,"w",encoding='utf-8')as f:
        f.write(str(v4))
    with open(l_path,"w",encoding='utf-8')as f:
        f.write(str(v5))
    with open(m_path,"w",encoding='utf-8')as f:
        f.write(str(v6))
    with open(h_path,"w",encoding='utf-8')as f:
        f.write(combobox1.get())
    with open(i_path,"w",encoding='utf-8')as f:
        f.write(combobox2.get())
    with open(j_path,"w",encoding="utf-8")as f:
        f.write(combobox0.get()) 
    with open(k_path,"w",encoding="utf-8")as f:
        f.write(combobox3.get()) 

def x_save():
    with open(n_path,"w",encoding='utf-8')as f:
        f.write(str(num_wv1))

def x_save2(r):
    with open(p_path,"w",encoding='utf-8')as f:
        f.write(str(r))

def x_save3(r):
    with open(q_path,"w",encoding='utf-8')as f:
        f.write(str(r))

def load_theme():
    try:
        with open(b_path, 'r',encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
def load():
    try:
        with open(c_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load2():
    try:
        with open(d_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load3():
    try:
        with open(e_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load4():
    try:
        with open(f_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load5():
    try:
        with open(h_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load6():
    try:
        with open(i_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load7():
    try:
        with open(j_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load8():
    try:
        with open(k_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load9():
    try:
        with open(l_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load10():
    try:
        with open(m_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load11():
    try:
        with open(n_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load12():
    try:
        with open(p_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def load13():
    try:
        with open(q_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
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
def wv_1():
    global num_wv1
    num_wv1 = num_wv1 + 1
    x_save()

def x():
    window = ttk.Toplevel(root)
    window.title("小六壬")
    window.iconbitmap(icon_path)
    def LoopOutput2():

        file_path_csv = filedialog.asksaveasfilename(parent=window, defaultextension=".csv", 
                                                 filetypes=[("csv-utf-8", "*.csv")])
        
        def entry2_():
            icon.notify("循环过程中不可加入新循环\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2__():
            icon.notify("循环过程中不可做出任何改变\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2___():
            icon.notify("不可关闭该循环过程\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2_2():
            window.destroy()
            x()
        def T_LoopOutput_X():
            def LoopOutput_X():
                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)

                match entry___:
                    case []:
                        text_widget.insert(tk.END,"已循环次数：0")
                        while True:
                            if num == int(entry_):
                                #shutil.copy(o_path, file_path_csv)
                                #csv = pd.read_csv(file_path_csv, delimiter=', ', engine='python')
                                #csv.to_csv(file_path_csv, index=False)
                                text_widget.delete(1.0, END)
                                text_widget.insert(tk.END,"已完成循环")
                                entry2.pack_forget()
                                text2.pack_forget()
                                entry.pack(padx=5,pady=5,side='right')
                                entry.config(font=font_style)
                                text.pack(padx=5,pady=5,side='right')
                                w3.grid_remove()
                                w.grid()
                                break
                            with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                    t_rule_num = int(load12() or 1)
                                    t_rule_num2 = int(load13() or 2)
                                    if t_rule_num == 0:
                                        match t_rule_num2:
                                            case 1:
                                                f.write(XiaoLliuren.numgua2_1())
                                            case 0:
                                                f.write(XiaoLliuren.numgua2_0())
                                            case 2:
                                                f.write(XiaoLliuren.numgua2_2())
                                    elif t_rule_num == 1:
                                        f.write(XiaoLliuren.numgua2_3())
                            num = num + 1
                            text_widget.delete(1.0, END)
                            text_widget.insert(tk.END,"已循环次数：{}".format(num))
                    case _:
                        messagebox.showerror("错误", message="请只输入整数",parent=window)
                        entry2.pack_forget()
                        text2.pack_forget()
                        entry.pack(padx=5,pady=5,side='right')
                        entry.config(font=font_style)
                        text.pack(padx=5,pady=5,side='right')
                        w3.grid_remove()
                        w.grid()
            def x_x():
                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()
                def entry_row_name_():
                    if entry_row_name.get():
                        try:
                            with open(file_path_csv, 'w',encoding='utf-8') as f:
                                f.write("{}\n".format(entry_row_name.get()))
                            window_x.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=LoopOutput_X)
                            thread.start()
                        except:
                            icon.notify("未设置文件，已退出循环", "Lightweight text editor")
                            entry2_2_1()
                    else:
                        icon.notify("必须有列名", "Lightweight text editor")
                window_x = ttk.Toplevel(window)
                window_x.title("小六壬")
                window_x.iconbitmap(icon_path)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text = ttk.Label(window_x,text="列名：")
                text.pack(padx=5,pady=5,side="left")
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.pack(padx=5,pady=5,side="right")
                entry_row_name.insert(tk.END,"吉值")
                entry_row_name.bind('<Return>', lambda event: entry_row_name_())
                entry_row_name.bind('<Shift_L>', lambda event: entry2_2_1())
            
            def x_x_():

                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                def entry_row_name_():
                    if entry_row_name.get() and entry_row_name2.get() and entry_row_name3.get() and entry_row_name4.get():
                        try:
                            with open(file_path_csv, 'w',encoding='utf-8') as f:
                                f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                            window_x.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=LoopOutput_X)
                            thread.start()
                        except:
                            icon.notify("未设置文件，已退出循环", "Lightweight text editor")
                            entry2_2_1()
                    else:
                        icon.notify("必须有列名", "Lightweight text editor")

                window_x = ttk.Toplevel(window)
                window_x.title("小六壬")
                window_x.iconbitmap(icon_path)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text = ttk.Label(window_x,text="列名一")
                text.grid(row=0,column=0,padx=5,pady=5)
                text2 = ttk.Label(window_x,text="列名二")
                text2.grid(row=0,column=1,padx=5,pady=5)
                text3 = ttk.Label(window_x,text="列名三")
                text3.grid(row=0,column=2,padx=5,pady=5)
                text4 = ttk.Label(window_x,text="列名四")
                text4.grid(row=0,column=3,padx=5,pady=5)
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.grid(row=1,column=0,padx=5,pady=5)
                entry_row_name2 = ttk.Entry(window_x)
                entry_row_name2.grid(row=1,column=1,padx=5,pady=5)
                entry_row_name3 = ttk.Entry(window_x)
                entry_row_name3.grid(row=1,column=2,padx=5,pady=5)
                entry_row_name4 = ttk.Entry(window_x)
                entry_row_name4.grid(row=1,column=3,padx=5,pady=5)
                entry_row_name.insert(tk.END,"天宫")
                entry_row_name2.insert(tk.END,"地宫")
                entry_row_name3.insert(tk.END,"人宫")
                entry_row_name4.insert(tk.END,"吉值")
                entry_row_name.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name2.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name3.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name4.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name.bind('<Return>', lambda event: entry_row_name2.focus_set())
                entry_row_name2.bind('<Return>', lambda event: entry_row_name3.focus_set())
                entry_row_name3.bind('<Return>', lambda event: entry_row_name4.focus_set())
                entry_row_name4.bind('<Return>', lambda event: entry_row_name.focus_set())
                entry_row_name.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name2.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name3.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name4.bind('<Shift_L>', lambda event: entry2_2_1())
            
            check_up_num = int(load12() or 1)
            if check_up_num == 0:
                x_x()
            elif check_up_num == 1:
                x_x_()
            window.focus_set()
            entrynum = entry.get()
            entry.pack_forget()
            text.pack_forget()
            entry2 = tk.Entry(w2)
            entry2.pack(padx=5,pady=5,side='right')
            entry2.config(font=font_style)
            entry2.insert(tk.END,entrynum)
            entry2.bind('<Return>', lambda event: entry2_())
            entry2.bind('<Shift_L>', lambda event: entry2_2())
            text2 = ttk.Label(w2, text="循环次数")
            text2.pack(padx=5,pady=5,side='right')
            text_widget.delete(1.0, END)
            w.grid_remove()
            w3 = ttk.Frame(window)
            w3.grid(row=2,column=0,sticky=E)
            if t_rule_num2 == 1:
                b3 = ttk.Button(w3, text="输出不去尾", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')
            elif t_rule_num2 == 0:
                b3 = ttk.Button(w3, text="输出保留整数", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')
            elif t_rule_num2 == 2:
                b3 = ttk.Button(w3, text="输出保留两位", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')

            if t_rule_num == 1:
                b2 = ttk.Button(w3, text="常规循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')

            b4 = ttk.Button(w3,text="循环输出csv文件",bootstyle="outline", command=entry2__)
            b4.pack(padx=5,pady=5,side='right')
            b1 = ttk.Button(w3, text="循环输出txt文件", bootstyle="outline", command=entry2__)
            b1.pack(padx=5,pady=5,side='right')
            Separator(w3, orient=VERTICAL).pack(fill=Y,padx=5,pady=5,side='right')
            wv1 = ttk.IntVar()
            if num_wv1 % 2 == 1:
                wv1.set(1)
            else:
                wv1.set(0)
            consider_checkbutton2 = ttk.Checkbutton(w3, text="本页为首", variable=wv1, command=wv_1, bootstyle="round-toggle",state="disabled")
            consider_checkbutton2.pack(padx=5,pady=5,side='right')
        
        combo.grid_remove()
        w2 = ttk.Frame(window)
        w2.grid(row=0,column=0,sticky=W)
        entry = tk.Entry(w2)
        entry.pack(padx=5,pady=5,side='right')
        entry.config(font=font_style)
        text = ttk.Label(w2, text="循环次数")
        text.pack(padx=5,pady=5,side='right')
        entry.focus_set()
        entry.bind('<Return>', lambda event: T_LoopOutput_X())
        entry.bind('<Shift_L>', lambda event: entry2_2())

    def LoopOutput():
        file_path = filedialog.asksaveasfilename(parent=window, defaultextension=".txt", 
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        def entry2_():
            icon.notify("循环过程中不可加入新循环\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2__():
            icon.notify("循环过程中不可做出任何改变\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2_2():
            window.destroy()
            x()
        def T_LoopOutput_X():
            def LoopOutput_X():
                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)
                match entry___:
                    case []:
                        text_widget.insert(tk.END,"已循环次数：0")
                        with open(file_path, 'w',encoding='utf-8') as f:
                            f.truncate()
                        while True:
                            if num == int(entry_):
                                #shutil.copy(o_path, file_path)
                                text_widget.delete(1.0, END)
                                text_widget.insert(tk.END,"已完成循环")
                                entry2.pack_forget()
                                text2.pack_forget()
                                entry.pack(padx=5,pady=5,side='right')
                                entry.config(font=font_style)
                                text.pack(padx=5,pady=5,side='right')
                                w3.grid_remove()
                                w.grid()
                                break
                            with open(file_path, 'a+',encoding='utf-8') as f:
                                    t_rule_num = int(load12() or 1)
                                    t_rule_num2 = int(load13() or 2)
                                    if t_rule_num == 0:
                                        match t_rule_num2:
                                            case 1:
                                                f.write(XiaoLliuren.numgua2_1())
                                            case 0:
                                                f.write(XiaoLliuren.numgua2_0())
                                            case 2:
                                                f.write(XiaoLliuren.numgua2_2())
                                    elif t_rule_num == 1:
                                        f.write(XiaoLliuren.numgua())
                            num = num + 1
                            text_widget.delete(1.0, END)
                            text_widget.insert(tk.END,"已循环次数：{}".format(num))
                    case _:
                        messagebox.showerror("错误", message="请只输入整数",parent=window)
                        entry2.pack_forget()
                        text2.pack_forget()
                        entry.pack(padx=5,pady=5,side='right')
                        entry.config(font=font_style)
                        text.pack(padx=5,pady=5,side='right')
                        w3.grid_remove()
                        w.grid()
            
            window.focus_set()
            entrynum = entry.get()
            entry.pack_forget()
            text.pack_forget()
            entry2 = tk.Entry(w2)
            entry2.pack(padx=5,pady=5,side='right')
            entry2.config(font=font_style)
            entry2.insert(tk.END,entrynum)
            entry2.bind('<Return>', lambda event: entry2_())
            entry2.bind('<Shift_L>', lambda event: entry2_2())
            text2 = ttk.Label(w2, text="循环次数")
            text2.pack(padx=5,pady=5,side='right')
            text_widget.delete(1.0, END)
            thread = threading.Thread(target=LoopOutput_X)
            thread.start()
            w.grid_remove()
            w3 = ttk.Frame(window)
            w3.grid(row=2,column=0,sticky=E)
            if t_rule_num2 == 1:
                b3 = ttk.Button(w3, text="输出不去尾", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')
            elif t_rule_num2 == 0:
                b3 = ttk.Button(w3, text="输出保留整数", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')
            elif t_rule_num2 == 2:
                b3 = ttk.Button(w3, text="输出保留两位", bootstyle="outline", command=entry2__)
                b3.pack(padx=5,pady=5,side='right')

            if t_rule_num == 1:
                b2 = ttk.Button(w3, text="常规循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')

            b4 = ttk.Button(w3,text="循环输出csv文件",bootstyle="outline", command=entry2__)
            b4.pack(padx=5,pady=5,side='right')
            b1 = ttk.Button(w3, text="循环输出txt文件", bootstyle="outline", command=entry2__)
            b1.pack(padx=5,pady=5,side='right')
            Separator(w3, orient=VERTICAL).pack(fill=Y,padx=5,pady=5,side='right')
            wv1 = ttk.IntVar()
            if num_wv1 % 2 == 1:
                wv1.set(1)
            else:
                wv1.set(0)
            consider_checkbutton2 = ttk.Checkbutton(w3, text="本页为首", variable=wv1, command=wv_1, bootstyle="round-toggle",state="disabled")
            consider_checkbutton2.pack(padx=5,pady=5,side='right')
        
        combo.grid_remove()
        w2 = ttk.Frame(window)
        w2.grid(row=0,column=0,sticky=W)
        entry = tk.Entry(w2)
        entry.pack(padx=5,pady=5,side='right')
        entry.config(font=font_style)
        text = ttk.Label(w2, text="循环次数")
        text.pack(padx=5,pady=5,side='right')
        entry.focus_set()
        entry.bind('<Return>', lambda event: T_LoopOutput_X())
        entry.bind('<Shift_L>', lambda event: entry2_2())
        
        
    def CountB3_3():
        rule_num = 1
        b3.config(text="输出不去尾",command=CountB3_1)
        x_save3(rule_num)

    def CountB3_2():
        rule_num = 2
        b3.config(text="输出保留两位",command=CountB3_3)
        x_save3(rule_num)
    
    def CountB3_1():
        rule_num = 0
        b3.config(text="输出保留整数",command=CountB3_2)
        x_save3(rule_num)

    def CountB2_2():
        rule_num = 1
        b2.config(text="常规循环输出",command=CountB2_1)
        x_save2(rule_num)

    def CountB2_1():
        rule_num = 0
        b2.config(text="只循环输出吉值",command=CountB2_2)
        x_save2(rule_num)

    def generate_and_display():
        text_widget.delete(1.0, END)
        if combo.get() == "算一卦":
            text_widget.insert(tk.END,XiaoLliuren.numgua())

    def on_right_click(event):
        x, y = event.x_root, event.y_root
        if combo.winfo_rootx() < x < combo.winfo_rootx() + combo.winfo_width() and \
                combo.winfo_rooty() < y < combo.winfo_rooty() + combo.winfo_height():
            generate_and_display()
    values = ["算一卦"]
    combo = ttk.Combobox(window, values=values, state="readonly")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    combo.bind("<Button-3>", on_right_click)
    combo.set("算一卦")

    def 前_下拉框事件():
        if 下拉框.get() == "返回主页":
            window.destroy()
            root.deiconify()
        if 下拉框.get() == "保存数据":
            save_data()
        if 下拉框.get() == "上传数据":
            window.destroy()
            

    def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()


    下拉菜单组 = ["返回主页", "保存数据", "上传数据"]
    下拉框 = ttk.Combobox(window, values=下拉菜单组, state="readonly")
    下拉框.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    下拉框.bind("<Button-3>", 下拉框事件)
    下拉框.set("返回主页")
    scrollbar = ttk.Scrollbar(window, style="TScrollbar", bootstyle="round")
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_widget = tk.Text(window, wrap="word",
                          yscrollcommand=scrollbar.set, font=font_style)
    text_widget.grid(row=1, column=0, sticky="nsew")
    scrollbar.config(command=text_widget.yview)
    
    w = ttk.Frame(window)
    w.grid(row=2,column=0,sticky=E)

    if t_rule_num2 == 1:
        b3 = ttk.Button(w, text="输出不去尾", bootstyle="outline", command=CountB3_1)
        b3.pack(padx=5,pady=5,side='right')
    elif t_rule_num2 == 0:
        b3 = ttk.Button(w, text="输出保留整数", bootstyle="outline", command=CountB3_2)
        b3.pack(padx=5,pady=5,side='right')
    elif t_rule_num2 == 2:
        b3 = ttk.Button(w, text="输出保留两位", bootstyle="outline", command=CountB3_3)
        b3.pack(padx=5,pady=5,side='right')

    if t_rule_num == 1:
        b2 = ttk.Button(w, text="常规循环输出", bootstyle="outline", command=CountB2_1)
        b2.pack(padx=5,pady=5,side='right')
    elif t_rule_num == 0:
        b2 = ttk.Button(w, text="只循环输出吉值", bootstyle="outline", command=CountB2_2)
        b2.pack(padx=5,pady=5,side='right')
    
    b4 = ttk.Button(w,text="循环输出csv文件",bootstyle="outline", command=LoopOutput2)
    b4.pack(padx=5,pady=5,side='right')
    b1 = ttk.Button(w, text="循环输出txt文件", bootstyle="outline", command=LoopOutput)
    b1.pack(padx=5,pady=5,side='right')
    Separator(w, orient=VERTICAL).pack(fill=Y,padx=5,pady=5,side='right')
    wv1 = ttk.IntVar()
    if num_wv1 % 2 == 1:
        wv1.set(1)
    else:
        wv1.set(0)
    consider_checkbutton2 = ttk.Checkbutton(w, text="本页为首", variable=wv1, command=wv_1, bootstyle="round-toggle")
    consider_checkbutton2.pack(padx=5,pady=5,side='right')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    def save_data():
        file_path = filedialog.asksaveasfilename(parent=window, defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            shutil.copy(g_path, file_path)

    window.mainloop()

def gadget():
        
    def z():
        window = ttk.Toplevel()
        window.title("轻量记事本-小工具-紫微斗数")
        window.iconbitmap(icon_path)
    window = ttk.Toplevel()
    window.title("轻量记事本-小工具")
    window.iconbitmap(icon_path)
    b1 = ttk.Button(window, text="小六壬", bootstyle="outline", command=x)
    b1.grid(column=0,row=0,padx=10,pady=10)
    b2 = ttk.Button(window, text="紫微斗数", bootstyle="outline", command=z)
    b2.grid(column=1,row=0,padx=10,pady=10)






def root_window():
    
    window = ttk.Toplevel()
    window.resizable(0,0)
    window.title("轻量记事本-设置")
    window.iconbitmap(icon_path)

    def w_root1():

        global theme_cbo

        def bao_chun(): 
            global v2,v3,v4
            p1=v2%2
            p2=v3%2
            p3=v4%2
            if p1+p2+p3==1:
                save(theme_cbo.get())    
            else:
                messagebox.showerror("错误", message="不支持多字体或无字体选择",parent=window)
        
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

        window_Button_two = ttk.Button(w_, text="返回", bootstyle="outline", command=window.destroy)
        window_Button_two.grid(column=4,row=0,padx=10,pady=10)
        window_Button = ttk.Button(w_, text="保存当前设置", bootstyle="outline", command=bao_chun)
        window_Button.grid(column=3,row=0,padx=10,pady=10)

        w2 = ttk.Frame(w_)
        w2.grid(row=1,column=1,sticky=W)

        consider_var_2 = ttk.IntVar()
        if v2 % 2 == 1:
            consider_var_2.set(1)
        else:
            consider_var_2.set(0)
        consider_checkbutton2 = ttk.Checkbutton(w2, text="宋体", variable=consider_var_2, command=s2, bootstyle="round-toggle")
        consider_checkbutton2.grid(column=1,row=1,padx=10,pady=10)

        consider_var_3 = ttk.IntVar()
        if v3 % 2 == 1:
            consider_var_3.set(1)
        else:
            consider_var_3.set(0)
        consider_checkbutton3 = ttk.Checkbutton(w2, text="等线", variable=consider_var_3, command=s3, bootstyle="round-toggle")
        consider_checkbutton3.grid(column=2,row=1,padx=10,pady=10)

        consider_var_4 = ttk.IntVar()
        if v4 % 2 == 1:
            consider_var_4.set(1)
        else:
            consider_var_4.set(0)
        consider_checkbutton4 = ttk.Checkbutton(w2, text="黑体", variable=consider_var_4, command=s4, bootstyle="round-toggle")
        consider_checkbutton4.grid(column=3,row=1,padx=10,pady=10)

        w4 = ttk.Frame(w_)
        w4.grid(row=0,column=1,sticky=W)

        style = ttk.Style()
        theme_names = style.theme_names()
        theme_cbo = ttk.Combobox(master=w4, values=theme_names)
        theme_cbo.grid(column=1,row=0,padx=10,pady=10)
        theme_cbo.current(theme_names.index(style.theme_use()))
        theme_cbo.bind('<<ComboboxSelected>>', change_theme)
        
    w_root1()
    
    sep = Separator(window)
    sep.grid(column=0, row=1,pady=30,ipadx=300)

    def w_root2():
        w_2 = ttk.Frame(window)
        w_2.grid(row=2,column=0,sticky=W)
        
        lb3 = ttk.Label(w_2, text="关联设置:")
        lb3.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        consider_var = ttk.IntVar()
        if v % 2 == 1:
            consider_var.set(1)
        else:
            consider_var.set(0)
        consider_checkbutton = ttk.Checkbutton(w_2, text="是否关联上一次保存的文件", variable=consider_var, command=s, bootstyle="round-toggle")
        consider_checkbutton.grid(column=1,row=0,padx=10,pady=10)

    w_root2()
    
    sep2 = Separator(window)
    sep2.grid(column=0, row=3,pady=30,ipadx=300)
    
    def w_root3():
        w_3 = ttk.Frame(window)
        w_3.grid(row=4,column=0,sticky=W)
        
        
        lb4 = ttk.Label(w_3, text="文件设置:")
        lb4.grid(column=0,row=0,padx=10,pady=10,ipadx=5,sticky=W)

        w5 = ttk.Frame(w_3)
        w5.grid(row=0,column=1,sticky=W)

        def combobox():
            global combobox1,combobox2,combobox0,combobox3

            w5lb0 = ttk.Label(w5,text="区分文件:")
            w5lb0.grid(column=0,row=0,padx=10,pady=10)
            w5lb3 = ttk.Label(w5,text="文件循环导入值:")
            w5lb3.grid(column=0,row=1,padx=10,pady=10)
            w5lb1 = ttk.Label(w5,text="大文件定义:")
            w5lb1.grid(column=0,row=2,padx=10,pady=10)
            w5lb2 = ttk.Label(w5,text="大文件分割:")
            w5lb2.grid(column=0,row=3,padx=10,pady=10)

            combobox2_group1 = ["等于大文件定义","5MB","10MB","15MB","30MB"]
            combobox1_group1 = [ "50MB", "70MB", "128MB", "256MB", "512MB"]
            combobox0_group1 = ["开启","关闭"]
            combobox3_group1 = ["5MB","10MB","30MB","50MB","70MB", "128MB", "256MB", "512MB"]

            combobox1 = ttk.Combobox(master=w5, values=combobox1_group1)
            combobox1.grid(row=2, column=2,padx=10,pady=10)

            combobox2 = ttk.Combobox(master=w5, values=combobox2_group1)
            combobox2.grid(row=3, column=2,padx=10,pady=10)

            combobox0 = ttk.Combobox(master=w5, values=combobox0_group1)
            combobox0.grid(row=0, column=2,padx=10,pady=10)

            combobox3 = ttk.Combobox(master=w5, values=combobox3_group1)
            combobox3.grid(row=1, column=2,padx=10,pady=10)
            combobox0.set("开启")
            combobox1.set("70MB")
            combobox2.set("等于大文件定义")
            combobox3.set("30MB")

            match _size_:
                case "70MB":
                    combobox1.set("70MB")
                case "50MB":
                    combobox1.set("50MB")
                case "128MB":
                    combobox1.set("128MB")
                case "256MB":
                    combobox1.set("256MB")
                case "512MB":
                    combobox1.set("512MB")

            match divide_up:
                case "等于大文件定义":
                    combobox2.set("等于大文件定义")
                case "5MB":
                    combobox2.set("5MB")
                case "10MB":
                    combobox2.set("10MB")
                case "15MB":
                    combobox2.set("15MB")
                case "30MB":
                    combobox2.set("30MB")

            match onandoff:
                case "开启":
                    combobox0.set("开启")
                case "关闭":
                    combobox0.set("关闭")

            match circular:
                case "5MB":
                    combobox3.set("5MB")
                case "10MB":
                    combobox3.set("10MB")
                case "30MB":
                    combobox3.set("30MB")
                case "50MB":
                    combobox3.set("50MB")
                case "70MB":
                    combobox3.set("70MB")
                case "128MB":
                    combobox3.set("128MB")
                case "256MB":
                    combobox3.set("256MB")
                case "512MB":
                    combobox3.set("512MB")
        
        combobox()

    w_root3()
    
    sep3 = Separator(window)
    sep3.grid(column=0, row=5,pady=30,ipadx=300)
    
    def w_root4():
        w_4 = ttk.Frame(window)
        w_4.grid(row=6,column=0,sticky=W)

        w_4_1 = ttk.Frame(w_4)
        w_4_1.grid(column=1,row=1,sticky=W)

        lb5 = ttk.Label(w_4, text="小工具设置:")
        lb5.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        lb6 = ttk.Label(w_4, text="小六壬:")
        lb6.grid(column=0,row=1,padx=10,pady=10,ipadx=5)

        consider_var = ttk.IntVar()
        if v5 % 2 == 1:
            consider_var.set(1)
        else:
            consider_var.set(0)
        consider_checkbutton = ttk.Checkbutton(w_4_1, text="使用三宫定义", variable=consider_var, command=s5, bootstyle="round-toggle")
        consider_checkbutton.grid(column=0,row=0,padx=10,pady=10,sticky=W)

        consider_var2 = ttk.IntVar()
        if v6 % 2 == 1:
            consider_var2.set(1)
        else:
            consider_var2.set(0)
        consider_checkbutton2 = ttk.Checkbutton(w_4_1, text="不计算吉值", variable=consider_var2, command=s6, bootstyle="round-toggle")
        consider_checkbutton2.grid(column=0,row=1,padx=10,pady=10,sticky=W)
    
    w_root4()

    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    
    window.mainloop()

def quit_window(icon: pystray.Icon):
    icon.stop()
    icon.visible = False
    root.destroy()

def show_window():
    root.deiconify()

def on_exit():
    root.withdraw()

def 前_下拉框事件():
        if 下拉框.get() == "保存":
            save_t()
        elif 下拉框.get() == "设置":
            root_window()
        elif 下拉框.get() == "小工具":
            gadget()
def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()

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

def two_window():
    global window2
    def mySearch():
        text_widget.tag_remove("found","1.0",END)
        start = "1.0"
        key = entry.get()
        if (len(key.strip()) == 0):
            return
        while True:
            pos = text_widget.search(key,start,END)  
            if (pos == ""):
                break
            text_widget.tag_add("found",pos,"%s+%dc" %(pos,len(key)))
            start = "%s+%dc" % (pos,len(key))
    def focus2():
        entry2.focus_set()
    def focus1():
        entry.focus_set()
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
        window2.iconbitmap(icon_path)
        window2.resizable( width=False, height=False )
        window2.wm_attributes("-topmost", True)
        lbl = ttk.Label(window2, text="查找:").grid(row=0, column=0,padx=5,pady=5)
        entry = tk.Entry(window2, width=30)
        entry.grid(row=0, column=1,padx=5,pady=5)
        entry.bind("<Return>", lambda event: mySearch())
        entry.focus_set()
        lb2 = ttk.Label(window2, text="替换:").grid(row=1, column=0,padx=5,pady=5)
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
        window2.destroy()
        window2 = None
    else:
        two_window()

def save_2():
    def save_2t():
        file_path = filedialog.asksaveasfilename(parent=root, defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        
        with open(a_path, 'w',encoding='utf-8') as f:
             lines = text_widget.get("1.0","end")
             f.writelines(lines)

        if file_path:
            shutil.copy(a_path, file_path)

    thread = threading.Thread(target=save_2t)
    thread.start()
        

def read(filename, msg):
    def read_and_split():
        global index,index_,t_size
        with open(msg, 'r',encoding='utf-8',errors = 'ignore') as f:
            index = 0
            while True:
                f.seek(index * t_divide_up)
                data = f.read(t_divide_up)
                if not data:
                    folder = os.path.join(p, "text-temp")
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
                                
                                with open(folder_t, 'r',encoding='utf-8',errors = 'ignore') as f:
                                    a = f.read()
                                    progressbarOne['value'] += division08
                                    text_widget.insert(tk.END, a)
                                    window3.destroy()
                                    root.attributes("-disabled", 0)
                            break
                    break

                with open(f'{filename}_{index}', 'w',encoding='utf-8',errors = 'ignore') as f1:
                    f1.write(str(data))
                index += 1
                progressbarOne['value'] += 1


    thread = threading.Thread(target=read_and_split)
    thread.start()

def save_ff():

    global progressbarOne2

    def save_tf():
     
     def save_tt():
         folder = os.path.join(p, "text-temp")
         filename_ = os.path.join(folder, f'{filename}')
         index = 0
         while True:
             try:
                 folder_t = (folder + "\\" + f'{filename}_{index}')
                 with open(folder_t, 'r',encoding='utf-8',errors = 'ignore') as f:
                     a = f.read()
                     index += 1
                 with open(filename_,'a',encoding='utf-8',errors = 'ignore') as f:
                     f.write(a)
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
    window4.resizable(0, 0)
    window4.iconbitmap(icon_path)
    window4.minsize(400, 50)
    window4.maxsize(400, 50)
    window4.wm_attributes("-topmost", True)
    root.attributes("-disabled", 1)
    lbl = ttk.Label(window4, text="正在保存中").pack(padx=5,pady=5)
    def on2():
        messagebox.showerror("错误", message="正在保存中，请勿退出",parent=window4)
    progressbarOne2 = tkinter.ttk.Progressbar(window4,bootstyle="striped")
    progressbarOne2.pack(pady=5,fill=X)
    progressbarOne2['maximum'] = division
    progressbarOne2['value'] = 0
    window4.protocol("WM_DELETE_WINDOW", on2)
    save_tf()
    window4.mainloop()

def save_t():
    try:
     size = os.path.getsize(msg)
     filename = os.path.basename(msg)
     if os.path.exists(msg):
        if size < t_size:
            with open(msg, 'w', encoding='utf-8') as f:
                lines = text_widget.get("1.0","end")
                f.writelines(lines)
                icon.notify("文件已成功保存", "Lightweight text editor")
        else:
            if index_ ==  1:
                folder = os.path.join(p, "text-temp")
                folder_t = (folder + "\\" + f'{filename}_{index}')
                with open(folder_t, 'w',encoding='utf-8') as f:
                    lines = text_widget.get("1.0","end")
                    f.writelines(lines)
                    save_ff()
            else:
                pass
     else:
        save_2()
    except:
        save_2()          

def i(files):
    global progressbarOne,window3,filename,t_size,msg
    msg = '\n'.join((item.decode('gbk') for item in files))
    filename = os.path.basename(msg)
    size = os.path.getsize(msg)
    
    if size < t_size:
        with open(msg, 'r', encoding='utf-8') as f:
            data = f.read()
            text_widget.insert(tk.END, data)

    elif onandoff == ("关闭"):
        
        def save_ttt():
            icon.notify("正在导入文件，不建议操作当前窗口", "Lightweight text editor")
            with open(msg, 'r', encoding='utf-8') as f:
                
                while True:

                    data = f.readlines(circular_num)

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
        window3.resizable(0, 0)
        window3.iconbitmap(icon_path)
        window3.minsize(400, 50)
        window3.maxsize(400, 50)
        window3.wm_attributes("-topmost", True)
        root.attributes("-disabled", 1)
        lbl = ttk.Label(window3, text="正在导入中").pack(padx=5,pady=5)
        def on2():
            messagebox.showerror("错误", message="导入过程中，请勿退出",parent=window3)
        progressbarOne = tkinter.ttk.Progressbar(window3,bootstyle="striped")
        progressbarOne.pack(pady=5,fill=X)
        progressbarOne['maximum'] = division
        progressbarOne['value'] = 0
        window3.protocol("WM_DELETE_WINDOW", on2)
        read(filename, msg)
        window3.mainloop()
        
def next_page():
    global index,index_
    if index_ ==  1:
        try:
         index += 1
         folder = os.path.join(p, "text-temp")
         folder_t = (folder + "\\" + f'{filename}_{index}')
         with open(folder_t, 'r',encoding='utf-8') as f:
             text_widget.delete('1.0', tk.END)
             a = f.read()
             text_widget.insert(tk.END, a)
        except:
            messagebox.showerror("错误", message="已经是尾页",parent=root)
            index -= 1
            folder = os.path.join(p, "text-temp")
            folder_t = (folder + "\\" + f'{filename}_{index}')
            with open(folder_t, 'r',encoding='utf-8') as f:
             text_widget.delete('1.0', tk.END)
             a = f.read()
             text_widget.insert(tk.END, a)
    else:
        messagebox.showerror("错误", message="仅限大文件操作",parent=root)

def return_page():
    global index,index_
    if index_ ==  1:
        try:
         index -= 1
         folder = os.path.join(p, "text-temp")
         folder_t = (folder + "\\" + f'{filename}_{index}')
         with open(folder_t, 'r',encoding='utf-8') as f:
             text_widget.delete('1.0', tk.END)
             a = f.read()
             text_widget.insert(tk.END, a)
        except:
            messagebox.showerror("错误", message="已经是首页",parent=root)
            index += 1
            folder = os.path.join(p, "text-temp")
            folder_t = (folder + "\\" + f'{filename}_{index}')
            with open(folder_t, 'r',encoding='utf-8') as f:
             text_widget.delete('1.0', tk.END)
             a = f.read()
             text_widget.insert(tk.END, a)
    else:
        messagebox.showerror("错误", message="仅限大文件操作",parent=root)
def sever():
    w.grid_forget()
    window = tk.Toplevel(root)
    window.title("分离控制")
    window.resizable(0, 0)
    window.iconbitmap(icon_path)
    window.minsize(400, 50)
    window.maxsize(400, 50)
    b2 = ttk.Button(window, text="下一页", bootstyle="link", command=next_page)
    b2.pack(padx=5,pady=5,side='right')
    b3 = ttk.Button(window, text="上一页", bootstyle="link", command=return_page)
    b3.pack(padx=5,pady=5, side='right')
    def on2():
        window.destroy()
        w.grid(row=2,column=0,sticky=E)
    b4 = ttk.Button(window, text="取消分离", bootstyle="link", command=on2)
    b4.pack(padx=5,pady=5,side='left')
    window.protocol("WM_DELETE_WINDOW", on2)
    window.mainloop()

if __name__ == '__main__':
    p = os.path.dirname(__file__)
    a_path = os.path.join(p, "a")
    b_path = os.path.join(p, "b")
    c_path = os.path.join(p, "c")
    d_path = os.path.join(p, "d")
    e_path = os.path.join(p, "e")
    f_path = os.path.join(p, "f")
    h_path = os.path.join(p, "h")
    i_path = os.path.join(p, "i")
    j_path = os.path.join(p, "j")
    k_path = os.path.join(p, "k")
    l_path = os.path.join(p, "l")
    m_path = os.path.join(p, "m")
    n_path = os.path.join(p, "n")
    o_path = os.path.join(p, "o")
    p_path = os.path.join(p, "p")
    q_path = os.path.join(p, "q")
    icon_path = os.path.join(p, "aaa.ico")
    error_path = os.path.join(p,"error.png")
    v = int(load() or 0)
    v2 = int(load2() or 1)
    v3 = int(load3() or 0)
    v4 = int(load4() or 0)
    v5 = int(load9() or 0)
    v6 = int(load10() or 0)
    num_wv1 = int(load11() or 0)
    _size_ = (load5() or "70MB")
    divide_up = (load6() or "等于大文件定义")
    onandoff = (load7() or "开启")
    circular = (load8() or "30MB")
    t_rule_num = int(load12() or 1)
    t_rule_num2 = int(load13()or 2)
    menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
    image = Image.open(icon_path)
    icon = pystray.Icon("icon", image, "轻量记事本", menu)
    root = tk.Tk()
    root.title("轻量记事本")
    root.iconbitmap(icon_path)
    font_style1 = tkFont.Font(family="宋体", size=12)
    font_style2 = tkFont.Font(family="等线", size=12)
    font_style3 = tkFont.Font(family="黑体", size=12)
    font_style = None
    t_size = 0
    t_divide_up = 0
    circular_num = 31457280
    if v2 % 2 == 1:
        font_style = font_style1
    elif v3 % 2 == 1:
        font_style = font_style2
    elif v4 % 2 == 1:
        font_style = font_style3

    if _size_ == ("70MB"):
        if divide_up == ("等于大文件定义"):
            t_divide_up = 73400320
            t_size = 73400320
        else:
            t_size = 73400320
            if divide_up == ("5MB"):
                t_divide_up = 5242880
            elif divide_up == ("10MB"):
                t_divide_up = 10485760
            elif divide_up == ("15MB"):
                t_divide_up = 15728640 
            elif divide_up == ("30MB"):
                t_divide_up = 31457280
    elif _size_ == ("50MB"):
        if divide_up == ("等于大文件定义"):
            t_divide_up = 52428800
            t_size = 52428800
        else:
            t_size = 52428800
            if divide_up == ("5MB"):
                t_divide_up = 5242880
            elif divide_up == ("10MB"):
                t_divide_up = 10485760
            elif divide_up == ("15MB"):
                t_divide_up = 15728640 
            elif divide_up == ("30MB"):
                t_divide_up = 31457280
    elif _size_ == ("128MB"):
        if divide_up == ("等于大文件定义"):
            t_divide_up = 134217728
            t_size = 134217728
        else:
            t_size = 134217728
            if divide_up == ("5MB"):
                t_divide_up = 5242880
            elif divide_up == ("10MB"):
                t_divide_up = 10485760
            elif divide_up == ("15MB"):
                t_divide_up = 15728640 
            elif divide_up == ("30MB"):
                t_divide_up = 31457280
    elif _size_ == ("256MB"):
        if divide_up == ("等于大文件定义"):
            t_divide_up = 268435456
            t_size = 268435456
        else:
            t_size = 268435456
            if divide_up == ("5MB"):
                t_divide_up = 5242880
            elif divide_up == ("10MB"):
                t_divide_up = 10485760
            elif divide_up == ("15MB"):
                t_divide_up = 15728640 
            elif divide_up == ("30MB"):
                t_divide_up = 31457280
    elif _size_ == ("512MB"):
        if divide_up == ("等于大文件定义"):
            t_divide_up = 536870912
            t_size = 536870912
        else:
            t_size = 536870912
            if divide_up == ("5MB"):
                t_divide_up = 5242880
            elif divide_up == ("10MB"):
                t_divide_up = 10485760
            elif divide_up == ("15MB"):
                t_divide_up = 15728640 
            elif divide_up == ("30MB"):
                t_divide_up = 31457280

    match circular:
        case "5MB":
            circular_num = 5242880
        case "10MB":
            circular_num = 10485760
        case "30MB":
            circular_num = 31457280
        case "50MB":
            circular_num = 52428800
        case "70MB":
            circular_num = 73400320
        case "128MB":
            circular_num = 134217728
        case "256MB":
            circular_num = 268435456
        case "512MB":
            circular_num = 536870912
        case _:
            circular_num = 31457280

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
    scrollbar = ttk.Scrollbar(root, style="TScrollbar", bootstyle="round")
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_widget = tk.Text(root, wrap="word",
                          yscrollcommand=scrollbar.set, font=font_style)
    text_widget.grid(row=1, column=0, sticky="nsew")
    text_widget.tag_configure("found", background="yellow")
    t=text_widget.get("1.0",tk.END)
    text_widget.focus_set()
    w = ttk.Frame(root)
    w.grid(row=2,column=0,sticky=E)
    b1 = ttk.Button(w, text="分离控制", bootstyle="link", command=sever)
    b1.pack(padx=5,pady=5,side='left')
    b2 = ttk.Button(w, text="下一页", bootstyle="link", command=next_page)
    b2.pack(padx=5,pady=5,side='right')
    b3 = ttk.Button(w, text="上一页", bootstyle="link", command=return_page)
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

    match num_wv1%2:
        case 1:
            root.withdraw()
            x()
        case _:
            pass

    try:
        if v % 2 == 1:
            text_widget.delete('1.0', tk.END)
            with open(a_path, 'r',encoding='utf-8') as f:
                data = f.read()
                text_widget.insert(tk.END, data)
    except:
        pass
    root.mainloop()