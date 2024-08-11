import datetime
import tkinter as tk
import tkinter.font as tkFont
import numpy as np
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
import XiaoLliuren
import tkinter.ttk
import re
from tkinter import colorchooser
import ZiWeidoushu

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
def load_down_box():
    try:
        with open(r_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
            pass
def load_down_box2():
    try:
        with open(s_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
            pass
def load_down_box3():
    try:
        with open(t_path, 'r',encoding='utf-8') as f:
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

#关于小六壬###分割线
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
                def recover():
                    text_widget.delete(1.0, END)
                    text_widget.insert(tk.END,"已完成循环")
                    entry2.pack_forget()
                    text2.pack_forget()
                    entry.pack(padx=5,pady=5,side='right')
                    entry.config(font=font_style)
                    text.pack(padx=5,pady=5,side='right')
                    w3.grid_remove()
                    w.grid()
                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)

                match entry___:
                    case []:
                        text_widget.insert(tk.END,"已循环次数：0")
                        t_rule_num = int(load12() or 1)
                        t_rule_num2 = int(load13() or 2)
                        buffer = []

                        match t_rule_num:
                            case 0:
                                match t_rule_num2:
                                    case 1:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                                    f.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLliuren.numgua2_1())
                                            num = num + 1
                                            if num%200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END,"{}".format(num))
                                    case 0:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                                    f.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLliuren.numgua2_0())
                                            num = num + 1
                                            if num%200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END,"{}".format(num))
                                    case 2:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                                    f.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLliuren.numgua2_2())
                                            num = num + 1
                                            if num%200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END,"{}".format(num))
                            case 1:
                                while True:
                                    if num == int(entry_):
                                        with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                            f.write(''.join(buffer))
                                        recover()
                                        break
                                    buffer.append(XiaoLliuren.numgua2_3())
                                    num = num + 1
                                    if num%200 == 0:
                                        text_widget.delete(1.6, END)
                                        text_widget.insert(tk.END,"{}".format(num))
                            case 2:
                                while True:
                                    if num == int(entry_):
                                        with open(file_path_csv, 'a+',encoding='utf-8') as f:
                                            f.write(''.join(buffer))
                                        recover()
                                        break
                                    buffer.append(XiaoLliuren.numgua2_4())
                                    num = num + 1
                                    if num%200 == 0:
                                        text_widget.delete(1.6, END)
                                        text_widget.insert(tk.END,"{}".format(num))
                                        
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
            
            def x_x__():
                
                def combobox_save():
                    with open(u_path,"w",encoding='utf-8')as f:
                        f.write(str(combobox.get()))
                
                def combobox_load():
                    try:
                        with open(u_path, 'r',encoding='utf-8') as f:
                            return f.read()
                    except FileNotFoundError:
                        pass
                
                t = str(combobox_load() or "顺序数据【空亡定为6】")
                
                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                def entry_row_name_():
                    
                    t = str(combobox_load() or "顺序数据【空亡定为6】")

                    def x_x__x():
                        
                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()
                        
                        def entry_row_name__():
                            with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
                                                                                         entry_row_name2_.get(),
                                                                                         entry_row_name3_.get(),
                                                                                         entry_row_name4_.get(),
                                                                                         entry_row_name5_.get(),
                                                                                         entry_row_name6_.get(),
                                                                                         entry_row_name7_.get(),
                                                                                         entry_row_name8_.get(),
                                                                                         entry_row_name9_.get(),
                                                                                         entry_row_name10_.get()
                                                                                         ))
                            window_x_.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=LoopOutput_X)
                            thread.start()

                        window_x_ = ttk.Toplevel(window)
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(icon_path)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_ = ttk.Label(window_x_,text="列名一")
                        text2_ = ttk.Label(window_x_,text="列名二")
                        text3_ = ttk.Label(window_x_,text="列名三")
                        text4_ = ttk.Label(window_x_,text="列名四")
                        text5_ = ttk.Label(window_x_,text="列名五")
                        text6_ = ttk.Label(window_x_,text="列名六")
                        text7_ = ttk.Label(window_x_,text="列名七")
                        text8_ = ttk.Label(window_x_,text="列名八")
                        text9_ = ttk.Label(window_x_,text="列名九")
                        text10_ = ttk.Label(window_x_,text="列名十")
                        entry_row_name_ = ttk.Entry(window_x_)
                        entry_row_name2_ = ttk.Entry(window_x_)
                        entry_row_name3_ = ttk.Entry(window_x_)
                        entry_row_name4_ = ttk.Entry(window_x_)
                        entry_row_name5_ = ttk.Entry(window_x_)
                        entry_row_name6_ = ttk.Entry(window_x_)
                        entry_row_name7_ = ttk.Entry(window_x_)
                        entry_row_name8_ = ttk.Entry(window_x_)
                        entry_row_name9_ = ttk.Entry(window_x_)
                        entry_row_name10_ = ttk.Entry(window_x_)
                        text_.grid(row=0,column=0,padx=5,pady=5)
                        text2_.grid(row=0,column=1,padx=5,pady=5)
                        text3_.grid(row=0,column=2,padx=5,pady=5)
                        text4_.grid(row=2,column=0,padx=5,pady=5)
                        text5_.grid(row=2,column=1,padx=5,pady=5)
                        text6_.grid(row=2,column=2,padx=5,pady=5)
                        text7_.grid(row=4,column=0,padx=5,pady=5)
                        text8_.grid(row=4,column=1,padx=5,pady=5)
                        text9_.grid(row=4,column=2,padx=5,pady=5)
                        text10_.grid(row=6,column=0,padx=5,pady=5)
                        entry_row_name_.grid(row=1,column=0,padx=5,pady=5)
                        entry_row_name2_.grid(row=1,column=1,padx=5,pady=5)
                        entry_row_name3_.grid(row=1,column=2,padx=5,pady=5)
                        entry_row_name4_.grid(row=3,column=0,padx=5,pady=5)
                        entry_row_name5_.grid(row=3,column=1,padx=5,pady=5)
                        entry_row_name6_.grid(row=3,column=2,padx=5,pady=5)
                        entry_row_name7_.grid(row=5,column=0,padx=5,pady=5)
                        entry_row_name8_.grid(row=5,column=1,padx=5,pady=5)
                        entry_row_name9_.grid(row=5,column=2,padx=5,pady=5)
                        entry_row_name10_.grid(row=7,column=0,padx=5,pady=5)
                        entry_row_name_.insert(tk.END,entry_row_name.get()+"(1)")
                        entry_row_name2_.insert(tk.END,entry_row_name.get()+"(2)")
                        entry_row_name3_.insert(tk.END,entry_row_name.get()+"(3)")
                        entry_row_name4_.insert(tk.END,entry_row_name2.get()+"(1)")
                        entry_row_name5_.insert(tk.END,entry_row_name2.get()+"(2)")
                        entry_row_name6_.insert(tk.END,entry_row_name2.get()+"(3)")
                        entry_row_name7_.insert(tk.END,entry_row_name3.get()+"(1)")
                        entry_row_name8_.insert(tk.END,entry_row_name3.get()+"(2)")
                        entry_row_name9_.insert(tk.END,entry_row_name3.get()+"(3)")
                        entry_row_name10_.insert(tk.END,entry_row_name4.get())
                        entry_row_name_.bind('<Return>', lambda event: entry_row_name2_.focus_set())
                        entry_row_name2_.bind('<Return>', lambda event: entry_row_name3_.focus_set())
                        entry_row_name3_.bind('<Return>', lambda event: entry_row_name4_.focus_set())
                        entry_row_name4_.bind('<Return>', lambda event: entry_row_name5_.focus_set())
                        entry_row_name5_.bind('<Return>', lambda event: entry_row_name6_.focus_set())
                        entry_row_name6_.bind('<Return>', lambda event: entry_row_name7_.focus_set())
                        entry_row_name7_.bind('<Return>', lambda event: entry_row_name8_.focus_set())
                        entry_row_name8_.bind('<Return>', lambda event: entry_row_name9_.focus_set())
                        entry_row_name9_.bind('<Return>', lambda event: entry_row_name10_.focus_set())
                        entry_row_name10_.bind('<Return>', lambda event: entry_row_name_.focus_set())
                        entry_row_name_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name2_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name3_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name4_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name5_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name6_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name7_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name8_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name9_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name10_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name2_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name3_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name4_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name5_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name6_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name7_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name8_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name9_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name10_.bind('<Shift_R>', lambda event: entry_row_name__())

                    def x_x__x_():
                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()
                        def entry_row_name__():
                            with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
                                                                                         entry_row_name2_.get(),
                                                                                         entry_row_name3_.get(),
                                                                                         entry_row_name4_.get(),
                                                                                         entry_row_name5_.get(),
                                                                                         entry_row_name6_.get(),
                                                                                         entry_row_name7_.get(),
                                                                                         entry_row_name8_.get(),
                                                                                         entry_row_name9_.get(),
                                                                                         entry_row_name10_.get(),
                                                                                         entry_row_name11_.get(),
                                                                                         entry_row_name12_.get(),
                                                                                         entry_row_name13_.get(),
                                                                                         entry_row_name14_.get(),
                                                                                         entry_row_name15_.get(),
                                                                                         entry_row_name16_.get()
                                                                                         ))
                            window_x_.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=LoopOutput_X)
                            thread.start()
                        window_x_ = ttk.Toplevel(window)
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(icon_path)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_ = ttk.Label(window_x_,text="列名一【顺序数据】")
                        text2_ = ttk.Label(window_x_,text="列名二【顺序数据】")
                        text3_ = ttk.Label(window_x_,text="列名三【顺序数据】")
                        text4_ = ttk.Label(window_x_,text="列名四【值数据】")
                        text5_ = ttk.Label(window_x_,text="列名五【值数据】")
                        text6_ = ttk.Label(window_x_,text="列名六【值数据】")
                        text7_ = ttk.Label(window_x_,text="列名七【详细值数据】")
                        text8_ = ttk.Label(window_x_,text="列名八【详细值数据】")
                        text9_ = ttk.Label(window_x_,text="列名九【详细值数据】")
                        text10_ = ttk.Label(window_x_,text="列名十【详细值数据】")
                        text11_ = ttk.Label(window_x_,text="列名十一【详细值数据】")
                        text12_ = ttk.Label(window_x_,text="列名十二【详细值数据】")
                        text13_ = ttk.Label(window_x_,text="列名十三【详细值数据】")
                        text14_ = ttk.Label(window_x_,text="列名十四【详细值数据】")
                        text15_ = ttk.Label(window_x_,text="列名十五【详细值数据】")
                        text16_ = ttk.Label(window_x_,text="列名十六【吉值】")
                        
                        entry_row_name_ = ttk.Entry(window_x_)
                        entry_row_name2_ = ttk.Entry(window_x_)
                        entry_row_name3_ = ttk.Entry(window_x_)
                        entry_row_name4_ = ttk.Entry(window_x_)
                        entry_row_name5_ = ttk.Entry(window_x_)
                        entry_row_name6_ = ttk.Entry(window_x_)
                        entry_row_name7_ = ttk.Entry(window_x_)
                        entry_row_name8_ = ttk.Entry(window_x_)
                        entry_row_name9_ = ttk.Entry(window_x_)
                        entry_row_name10_ = ttk.Entry(window_x_)
                        entry_row_name11_ = ttk.Entry(window_x_)
                        entry_row_name12_ = ttk.Entry(window_x_)
                        entry_row_name13_ = ttk.Entry(window_x_)
                        entry_row_name14_ = ttk.Entry(window_x_)
                        entry_row_name15_ = ttk.Entry(window_x_)
                        entry_row_name16_ = ttk.Entry(window_x_)


                        text_.grid(row=0,column=0,padx=5,pady=5)
                        text2_.grid(row=0,column=1,padx=5,pady=5)
                        text3_.grid(row=0,column=2,padx=5,pady=5)
                        text4_.grid(row=2,column=0,padx=5,pady=5)
                        text5_.grid(row=2,column=1,padx=5,pady=5)
                        text6_.grid(row=2,column=2,padx=5,pady=5)
                        text7_.grid(row=4,column=0,padx=5,pady=5)
                        text8_.grid(row=4,column=1,padx=5,pady=5)
                        text9_.grid(row=4,column=2,padx=5,pady=5)
                        text10_.grid(row=6,column=0,padx=5,pady=5)
                        text11_.grid(row=6,column=1,padx=5,pady=5)
                        text12_.grid(row=6,column=2,padx=5,pady=5)
                        text13_.grid(row=8,column=0,padx=5,pady=5)
                        text14_.grid(row=8,column=1,padx=5,pady=5)
                        text15_.grid(row=8,column=2,padx=5,pady=5)
                        text16_.grid(row=10,column=0,padx=5,pady=5)

                        entry_row_name_.grid(row=1,column=0,padx=5,pady=5)
                        entry_row_name2_.grid(row=1,column=1,padx=5,pady=5)
                        entry_row_name3_.grid(row=1,column=2,padx=5,pady=5)
                        entry_row_name4_.grid(row=3,column=0,padx=5,pady=5)
                        entry_row_name5_.grid(row=3,column=1,padx=5,pady=5)
                        entry_row_name6_.grid(row=3,column=2,padx=5,pady=5)
                        entry_row_name7_.grid(row=5,column=0,padx=5,pady=5)
                        entry_row_name8_.grid(row=5,column=1,padx=5,pady=5)
                        entry_row_name9_.grid(row=5,column=2,padx=5,pady=5)
                        entry_row_name10_.grid(row=7,column=0,padx=5,pady=5)
                        entry_row_name11_.grid(row=7,column=1,padx=5,pady=5)
                        entry_row_name12_.grid(row=7,column=2,padx=5,pady=5)
                        entry_row_name13_.grid(row=9,column=0,padx=5,pady=5)
                        entry_row_name14_.grid(row=9,column=1,padx=5,pady=5)
                        entry_row_name15_.grid(row=9,column=2,padx=5,pady=5)
                        entry_row_name16_.grid(row=11,column=0,padx=5,pady=5)

                        entry_row_name_.insert(tk.END,entry_row_name.get()+"【顺序数据】")
                        entry_row_name2_.insert(tk.END,entry_row_name2.get()+"【顺序数据】")
                        entry_row_name3_.insert(tk.END,entry_row_name3.get()+"【顺序数据】")

                        entry_row_name4_.insert(tk.END,entry_row_name.get()+"【值数据】")
                        entry_row_name5_.insert(tk.END,entry_row_name2.get()+"【值数据】")
                        entry_row_name6_.insert(tk.END,entry_row_name3.get()+"【值数据】")

                        entry_row_name7_.insert(tk.END,entry_row_name.get()+"(1)【详细值数据】")
                        entry_row_name8_.insert(tk.END,entry_row_name.get()+"(2)【详细值数据】")
                        entry_row_name9_.insert(tk.END,entry_row_name.get()+"(3)【详细值数据】")
                        entry_row_name10_.insert(tk.END,entry_row_name2.get()+"(1)【详细值数据】")
                        entry_row_name11_.insert(tk.END,entry_row_name2.get()+"(2)【详细值数据】")
                        entry_row_name12_.insert(tk.END,entry_row_name2.get()+"(3)【详细值数据】")
                        entry_row_name13_.insert(tk.END,entry_row_name3.get()+"(1)【详细值数据】")
                        entry_row_name14_.insert(tk.END,entry_row_name3.get()+"(2)【详细值数据】")
                        entry_row_name15_.insert(tk.END,entry_row_name3.get()+"(3)【详细值数据】")

                        entry_row_name16_.insert(tk.END,entry_row_name4.get())

                        entry_row_name_.bind('<Return>', lambda event: entry_row_name2_.focus_set())
                        entry_row_name2_.bind('<Return>', lambda event: entry_row_name3_.focus_set())
                        entry_row_name3_.bind('<Return>', lambda event: entry_row_name4_.focus_set())
                        entry_row_name4_.bind('<Return>', lambda event: entry_row_name5_.focus_set())
                        entry_row_name5_.bind('<Return>', lambda event: entry_row_name6_.focus_set())
                        entry_row_name6_.bind('<Return>', lambda event: entry_row_name7_.focus_set())
                        entry_row_name7_.bind('<Return>', lambda event: entry_row_name8_.focus_set())
                        entry_row_name8_.bind('<Return>', lambda event: entry_row_name9_.focus_set())
                        entry_row_name9_.bind('<Return>', lambda event: entry_row_name10_.focus_set())
                        entry_row_name10_.bind('<Return>', lambda event: entry_row_name11_.focus_set())
                        entry_row_name11_.bind('<Return>', lambda event: entry_row_name12_.focus_set())
                        entry_row_name12_.bind('<Return>', lambda event: entry_row_name13_.focus_set())
                        entry_row_name13_.bind('<Return>', lambda event: entry_row_name14_.focus_set())
                        entry_row_name14_.bind('<Return>', lambda event: entry_row_name15_.focus_set())
                        entry_row_name15_.bind('<Return>', lambda event: entry_row_name16_.focus_set())
                        entry_row_name16_.bind('<Return>', lambda event: entry_row_name_.focus_set())
                        entry_row_name_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name2_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name3_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name4_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name5_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name6_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name7_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name8_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name9_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name10_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name11_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name12_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name13_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name14_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name15_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name16_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name2_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name3_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name4_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name5_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name6_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name7_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name8_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name9_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name10_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name11_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name12_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name13_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name14_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name15_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name16_.bind('<Shift_R>', lambda event: entry_row_name__())
                        
                    def x_x__x__():
                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()
                        def entry_row_name__():
                            with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
                                                                                         entry_row_name2_.get(),
                                                                                         entry_row_name3_.get(),
                                                                                         entry_row_name4_.get(),
                                                                                         entry_row_name5_.get(),
                                                                                         entry_row_name6_.get(),
                                                                                         entry_row_name7_.get(),
                                                                                         entry_row_name8_.get(),
                                                                                         entry_row_name9_.get(),
                                                                                         entry_row_name10_.get(),
                                                                                         entry_row_name11_.get(),
                                                                                         entry_row_name12_.get(),
                                                                                         entry_row_name13_.get(),
                                                                                         entry_row_name14_.get(),
                                                                                         entry_row_name15_.get(),
                                                                                         entry_row_name16_.get()
                                                                                         ))
                            window_x_.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=LoopOutput_X)
                            thread.start()
                        window_x_ = ttk.Toplevel(window)
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(icon_path)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_  = ttk.Label(window_x_,text="列名一【顺序数据】【空亡定为6】")
                        text2_ = ttk.Label(window_x_,text="列名二【顺序数据】【空亡定为6】")
                        text3_ = ttk.Label(window_x_,text="列名三【顺序数据】【空亡定为6】")
                        text4_ = ttk.Label(window_x_,text="列名四【顺序数据】【空亡定为0】")
                        text5_ = ttk.Label(window_x_,text="列名五【顺序数据】【空亡定为0】")
                        text6_ = ttk.Label(window_x_,text="列名六【顺序数据】【空亡定为0】")
                        text7_ = ttk.Label(window_x_,text="列名七【值数据】")
                        text8_ = ttk.Label(window_x_,text="列名八【值数据】")
                        text9_ = ttk.Label(window_x_,text="列名九【值数据】")
                        text10_ = ttk.Label(window_x_,text="列名十【详细值数据】")
                        text11_ = ttk.Label(window_x_,text="列名十一【详细值数据】")
                        text12_ = ttk.Label(window_x_,text="列名十二【详细值数据】")
                        text13_ = ttk.Label(window_x_,text="列名十三【详细值数据】")
                        text14_ = ttk.Label(window_x_,text="列名十四【详细值数据】")
                        text15_ = ttk.Label(window_x_,text="列名十五【详细值数据】")
                        text16_ = ttk.Label(window_x_,text="列名十六【详细值数据】")
                        text17_ = ttk.Label(window_x_,text="列名十七【详细值数据】")
                        text18_ = ttk.Label(window_x_,text="列名十八【详细值数据】")
                        text19_ = ttk.Label(window_x_,text="列名十九【吉值】")
                        
                        entry_row_name_ = ttk.Entry(window_x_)
                        entry_row_name2_ = ttk.Entry(window_x_)
                        entry_row_name3_ = ttk.Entry(window_x_)
                        entry_row_name4_ = ttk.Entry(window_x_)
                        entry_row_name5_ = ttk.Entry(window_x_)
                        entry_row_name6_ = ttk.Entry(window_x_)
                        entry_row_name7_ = ttk.Entry(window_x_)
                        entry_row_name8_ = ttk.Entry(window_x_)
                        entry_row_name9_ = ttk.Entry(window_x_)
                        entry_row_name10_ = ttk.Entry(window_x_)
                        entry_row_name11_ = ttk.Entry(window_x_)
                        entry_row_name12_ = ttk.Entry(window_x_)
                        entry_row_name13_ = ttk.Entry(window_x_)
                        entry_row_name14_ = ttk.Entry(window_x_)
                        entry_row_name15_ = ttk.Entry(window_x_)
                        entry_row_name16_ = ttk.Entry(window_x_)
                        entry_row_name17_ = ttk.Entry(window_x_)
                        entry_row_name18_ = ttk.Entry(window_x_)
                        entry_row_name19_ = ttk.Entry(window_x_)


                        text_.grid(row=0,column=0,padx=5,pady=5)
                        text2_.grid(row=0,column=1,padx=5,pady=5)
                        text3_.grid(row=0,column=2,padx=5,pady=5)
                        text4_.grid(row=2,column=0,padx=5,pady=5)
                        text5_.grid(row=2,column=1,padx=5,pady=5)
                        text6_.grid(row=2,column=2,padx=5,pady=5)
                        text7_.grid(row=4,column=0,padx=5,pady=5)
                        text8_.grid(row=4,column=1,padx=5,pady=5)
                        text9_.grid(row=4,column=2,padx=5,pady=5)
                        text10_.grid(row=6,column=0,padx=5,pady=5)
                        text11_.grid(row=6,column=1,padx=5,pady=5)
                        text12_.grid(row=6,column=2,padx=5,pady=5)
                        text13_.grid(row=8,column=0,padx=5,pady=5)
                        text14_.grid(row=8,column=1,padx=5,pady=5)
                        text15_.grid(row=8,column=2,padx=5,pady=5)
                        text16_.grid(row=10,column=0,padx=5,pady=5)
                        text17_.grid(row=10,column=1,padx=5,pady=5)
                        text18_.grid(row=10,column=2,padx=5,pady=5)
                        text19_.grid(row=12,column=0,padx=5,pady=5)

                        entry_row_name_.grid(row=1,column=0,padx=5,pady=5)
                        entry_row_name2_.grid(row=1,column=1,padx=5,pady=5)
                        entry_row_name3_.grid(row=1,column=2,padx=5,pady=5)
                        entry_row_name4_.grid(row=3,column=0,padx=5,pady=5)
                        entry_row_name5_.grid(row=3,column=1,padx=5,pady=5)
                        entry_row_name6_.grid(row=3,column=2,padx=5,pady=5)
                        entry_row_name7_.grid(row=5,column=0,padx=5,pady=5)
                        entry_row_name8_.grid(row=5,column=1,padx=5,pady=5)
                        entry_row_name9_.grid(row=5,column=2,padx=5,pady=5)
                        entry_row_name10_.grid(row=7,column=0,padx=5,pady=5)
                        entry_row_name11_.grid(row=7,column=1,padx=5,pady=5)
                        entry_row_name12_.grid(row=7,column=2,padx=5,pady=5)
                        entry_row_name13_.grid(row=9,column=0,padx=5,pady=5)
                        entry_row_name14_.grid(row=9,column=1,padx=5,pady=5)
                        entry_row_name15_.grid(row=9,column=2,padx=5,pady=5)
                        entry_row_name16_.grid(row=11,column=0,padx=5,pady=5)
                        entry_row_name17_.grid(row=11,column=1,padx=5,pady=5)
                        entry_row_name18_.grid(row=11,column=2,padx=5,pady=5)
                        entry_row_name19_.grid(row=13,column=0,padx=5,pady=5)

                        entry_row_name_.insert(tk.END,entry_row_name.get()+"【顺序数据】【空亡定为6】")
                        entry_row_name2_.insert(tk.END,entry_row_name2.get()+"【顺序数据】【空亡定为6】")
                        entry_row_name3_.insert(tk.END,entry_row_name3.get()+"【顺序数据】【空亡定为6】")

                        entry_row_name4_.insert(tk.END,entry_row_name.get()+"【顺序数据】【空亡定为0】")
                        entry_row_name5_.insert(tk.END,entry_row_name2.get()+"【顺序数据】【空亡定为0】")
                        entry_row_name6_.insert(tk.END,entry_row_name3.get()+"【顺序数据】【空亡定为0】")

                        entry_row_name7_.insert(tk.END,entry_row_name.get()+"【值数据】")
                        entry_row_name8_.insert(tk.END,entry_row_name2.get()+"【值数据】")
                        entry_row_name9_.insert(tk.END,entry_row_name3.get()+"【值数据】")

                        entry_row_name10_.insert(tk.END,entry_row_name.get()+"(1)【详细值数据】")
                        entry_row_name11_.insert(tk.END,entry_row_name.get()+"(2)【详细值数据】")
                        entry_row_name12_.insert(tk.END,entry_row_name.get()+"(3)【详细值数据】")
                        entry_row_name13_.insert(tk.END,entry_row_name2.get()+"(1)【详细值数据】")
                        entry_row_name14_.insert(tk.END,entry_row_name2.get()+"(2)【详细值数据】")
                        entry_row_name15_.insert(tk.END,entry_row_name2.get()+"(3)【详细值数据】")
                        entry_row_name16_.insert(tk.END,entry_row_name3.get()+"(1)【详细值数据】")
                        entry_row_name17_.insert(tk.END,entry_row_name3.get()+"(2)【详细值数据】")
                        entry_row_name18_.insert(tk.END,entry_row_name3.get()+"(3)【详细值数据】")
                        entry_row_name19_.insert(tk.END,entry_row_name4.get())

                        

                        entry_row_name_.bind('<Return>', lambda event: entry_row_name2_.focus_set())
                        entry_row_name2_.bind('<Return>', lambda event: entry_row_name3_.focus_set())
                        entry_row_name3_.bind('<Return>', lambda event: entry_row_name4_.focus_set())
                        entry_row_name4_.bind('<Return>', lambda event: entry_row_name5_.focus_set())
                        entry_row_name5_.bind('<Return>', lambda event: entry_row_name6_.focus_set())
                        entry_row_name6_.bind('<Return>', lambda event: entry_row_name7_.focus_set())
                        entry_row_name7_.bind('<Return>', lambda event: entry_row_name8_.focus_set())
                        entry_row_name8_.bind('<Return>', lambda event: entry_row_name9_.focus_set())
                        entry_row_name9_.bind('<Return>', lambda event: entry_row_name10_.focus_set())
                        entry_row_name10_.bind('<Return>', lambda event: entry_row_name11_.focus_set())
                        entry_row_name11_.bind('<Return>', lambda event: entry_row_name12_.focus_set())
                        entry_row_name12_.bind('<Return>', lambda event: entry_row_name13_.focus_set())
                        entry_row_name13_.bind('<Return>', lambda event: entry_row_name14_.focus_set())
                        entry_row_name14_.bind('<Return>', lambda event: entry_row_name15_.focus_set())
                        entry_row_name15_.bind('<Return>', lambda event: entry_row_name16_.focus_set())
                        entry_row_name16_.bind('<Return>', lambda event: entry_row_name17_.focus_set())
                        entry_row_name17_.bind('<Return>', lambda event: entry_row_name18_.focus_set())
                        entry_row_name18_.bind('<Return>', lambda event: entry_row_name19_.focus_set())
                        entry_row_name19_.bind('<Return>', lambda event: entry_row_name_.focus_set())
                        entry_row_name_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name2_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name3_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name4_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name5_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name6_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name7_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name8_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name9_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name10_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name11_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name12_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name13_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name14_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name15_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name16_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name17_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name18_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name19_.bind('<Shift_L>', lambda event: entry2_2_2())
                        entry_row_name_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name2_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name3_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name4_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name5_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name6_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name7_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name8_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name9_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name10_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name11_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name12_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name13_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name14_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name15_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name16_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name17_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name18_.bind('<Shift_R>', lambda event: entry_row_name__())
                        entry_row_name19_.bind('<Shift_R>', lambda event: entry_row_name__())


                    if entry_row_name.get() and entry_row_name2.get() and entry_row_name3.get() and entry_row_name4.get():
                        try:
                            match t:
                                case "顺序数据【空亡定为6】":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "顺序数据【空亡定为0】":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "值数据":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "详细值数据【四列】":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "详细值数据【十列】":
                                    x_x__x()
                                    window_x.destroy()
                                case "全部【空亡定为6】【十六列】":
                                    x_x__x_()
                                    window_x.destroy()
                                case "全部【空亡定为6】【四列】":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "全部【空亡定为0】【十六列】":
                                    x_x__x_()
                                    window_x.destroy()
                                case "全部【空亡定为0】【四列】":
                                    with open(file_path_csv, 'w',encoding='utf-8') as f:
                                        f.write('{},{},{},{}\n'.format(entry_row_name.get(),entry_row_name2.get(),entry_row_name3.get(),entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=LoopOutput_X)
                                    thread.start()
                                case "真全部【十九列】":
                                    x_x__x__()
                                    window_x.destroy()
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
                text5 = ttk.Label(window_x,text="输出细节")
                text5.grid(row=0,column=4,padx=5,pady=5)
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.grid(row=1,column=0,padx=5,pady=5)
                entry_row_name2 = ttk.Entry(window_x)
                entry_row_name2.grid(row=1,column=1,padx=5,pady=5)
                entry_row_name3 = ttk.Entry(window_x)
                entry_row_name3.grid(row=1,column=2,padx=5,pady=5)
                entry_row_name4 = ttk.Entry(window_x)
                entry_row_name4.grid(row=1,column=3,padx=5,pady=5)
                
                combobox = ttk.Combobox(master=window_x, values=["顺序数据【空亡定为6】","顺序数据【空亡定为0】",
                                                                 "值数据","详细值数据【四列】","详细值数据【十列】",
                                                                 "全部【空亡定为6】【十六列】","全部【空亡定为6】【四列】",
                                                                 "全部【空亡定为0】【十六列】","全部【空亡定为0】【四列】",
                                                                 "真全部【十九列】"
                                                                 ], state="readonly")
                combobox.grid(row=1,column=4,padx=5,pady=5,ipadx=10)
                match t:
                    case "顺序数据【空亡定为6】":
                        combobox.set("顺序数据【空亡定为6】")
                    case "顺序数据【空亡定为0】":
                        combobox.set("顺序数据【空亡定为0】")
                    case "值数据":
                        combobox.set("值数据")
                    case "详细值数据【四列】":
                        combobox.set("详细值数据【四列】")
                    case "详细值数据【十列】":
                        combobox.set("详细值数据【十列】")
                    case "全部【空亡定为6】【十六列】":
                        combobox.set("全部【空亡定为6】【十六列】")
                    case "全部【空亡定为6】【四列】":
                        combobox.set("全部【空亡定为6】【四列】")
                    case "全部【空亡定为0】【十六列】":
                        combobox.set("全部【空亡定为0】【十六列】")
                    case "全部【空亡定为0】【四列】":
                        combobox.set("全部【空亡定为0】【四列】")
                    case "真全部【十九列】":
                        combobox.set("真全部【十九列】")
                entry_row_name.insert(tk.END,"天宫")
                entry_row_name2.insert(tk.END,"地宫")
                entry_row_name3.insert(tk.END,"人宫")
                entry_row_name4.insert(tk.END,"吉值")
                entry_row_name.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name2.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name3.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name4.bind('<Shift_R>', lambda event: entry_row_name_())
                combobox.bind('<Shift_R>', lambda event: entry_row_name_())
                entry_row_name.bind('<Return>', lambda event: entry_row_name2.focus_set())
                entry_row_name2.bind('<Return>', lambda event: entry_row_name3.focus_set())
                entry_row_name3.bind('<Return>', lambda event: entry_row_name4.focus_set())
                entry_row_name4.bind('<Return>', lambda event: combobox.focus_set())
                combobox.bind('<Return>', lambda event: entry_row_name.focus_set())
                entry_row_name.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name2.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name3.bind('<Shift_L>', lambda event: entry2_2_1())
                entry_row_name4.bind('<Shift_L>', lambda event: entry2_2_1())
                combobox.bind('<Shift_L>', lambda event: entry2_2_1())
                combobox.bind("<<ComboboxSelected>>", lambda event: combobox_save())
            
            check_up_num = int(load12() or 1)


            if check_up_num == 0:
                x_x()
            elif check_up_num == 1:
                x_x_()
            elif check_up_num == 2:
                x_x__()
            
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
                b2 = ttk.Button(w3, text="常规文字循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
            elif t_rule_num == 2:
                b2 = ttk.Button(w3, text="常规数据循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
            elif t_rule_num == 3:
                icon.notify("选用的方法不适用于该文件", "Lightweight text editor")
                entry2_2()

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
        def entry2___():
            icon.notify("不可关闭该循环过程\n强制退出循环<右Shift>", "Lightweight text editor")
        def entry2_2():
            window.destroy()
            x()
        def T_LoopOutput_X():
            def LoopOutput_X():
                def recover():
                    text_widget.delete(1.0, END)
                    text_widget.insert(tk.END,"已完成循环")
                    entry2.pack_forget()
                    text2.pack_forget()
                    entry.pack(padx=5,pady=5,side='right')
                    entry.config(font=font_style)
                    text.pack(padx=5,pady=5,side='right')
                    w3.grid_remove()
                    w.grid()
                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)
                match entry___:
                    case []:
                        try:
                            text_widget.insert(tk.END,"已循环次数：0")
                            t_rule_num = int(load12() or 1)
                            t_rule_num2 = int(load13() or 2)
                            buffer = []

                            match t_rule_num:
                                case 0:
                                    match t_rule_num2:
                                        case 1:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+',encoding='utf-8') as f:
                                                        f.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLliuren.numgua2_1())
                                                num = num + 1
                                                if num%200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END,"{}".format(num))
                                        case 0:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+',encoding='utf-8') as f:
                                                        f.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLliuren.numgua2_0())
                                                num = num + 1
                                                if num%200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END,"{}".format(num))
                                        case 2:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+',encoding='utf-8') as f:
                                                        f.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLliuren.numgua2_2())
                                                num = num + 1
                                                if num%200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END,"{}".format(num))
                                case 1:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+',encoding='utf-8') as f:
                                                f.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLliuren.numgua2_3())
                                        num = num + 1
                                        if num%200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END,"{}".format(num))
                                case 2:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+',encoding='utf-8') as f:
                                                f.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLliuren.numgua2_5())
                                        num = num + 1
                                        if num%200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END,"{}".format(num))
                                case 3:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+',encoding='utf-8') as f:
                                                f.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLliuren.numgua())
                                        num = num + 1
                                        if num%200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END,"{}".format(num))
                        except:
                            icon.notify("未设置文件或其它原因，已退出循环", "Lightweight text editor")
                            entry2_2()
                    case _:
                        messagebox.showerror("错误", message="请只输入整数",parent=window)
                        entry2.pack_forget()
                        text2.pack_forget()
                        entry.pack(padx=5,pady=5,side='right')
                        entry.config(font=font_style)
                        text.pack(padx=5,pady=5,side='right')
                        w3.grid_remove()
                        w.grid()
            
            def x1_x():
                
                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                def combobox_save():
                    with open(v_path,"w",encoding='utf-8')as f:
                        f.write(str(combobox.get()))
                
                def combobox_load():
                    try:
                        with open(v_path, 'r',encoding='utf-8') as f:
                            return f.read()
                    except FileNotFoundError:
                        pass
                
                def combobox_():
                    try:
                        window_x.destroy()
                        window.wm_attributes('-disabled', 0)
                        window.wm_attributes('-topmost', 1)
                        window.wm_attributes('-topmost', 0)
                        thread = threading.Thread(target=LoopOutput_X)
                        thread.start()
                    except:
                        icon.notify("未设置文件，已退出循环", "Lightweight text editor")
                        entry2_2_1()

                window_x = ttk.Toplevel(window)
                window_x.title("小六壬")
                window_x.iconbitmap(icon_path)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text_ = ttk.Label(window_x,text="输出细节")
                text_.grid(row=0,column=0,padx=5,pady=5)
                combobox = ttk.Combobox(master=window_x, values=["顺序数据【空亡定为6】","顺序数据【空亡定为0】","值数据","详细值数据【四列】","详细值数据【十列】"], state="readonly")
                combobox.grid(row=1,column=0,padx=5,pady=5)
                t = str(combobox_load() or "顺序数据【空亡定为6】")
                match t:
                    case "顺序数据【空亡定为6】":
                        combobox.set("顺序数据【空亡定为6】")
                    case "顺序数据【空亡定为0】":
                        combobox.set("顺序数据【空亡定为0】")
                    case "值数据":
                        combobox.set("值数据")
                    case "详细值数据【四列】":
                        combobox.set("详细值数据【四列】")
                    case "详细值数据【十列】":
                        combobox.set("详细值数据【十列】")
                combobox.bind('<Shift_R>', lambda event: combobox_())
                window_x.bind('<Shift_R>', lambda event: combobox_())
                combobox.bind('<Shift_L>', lambda event: entry2_2_1())
                window_x.bind('<Shift_L>', lambda event: entry2_2_1())
                combobox.bind("<<ComboboxSelected>>", lambda event: combobox_save())
                
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
            t_rule_num = int(load12() or 1)
            

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
                b2 = ttk.Button(w3, text="常规文字循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
                thread = threading.Thread(target=LoopOutput_X)
                thread.start()
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
                thread = threading.Thread(target=LoopOutput_X)
                thread.start()
            elif t_rule_num == 2:
                b2 = ttk.Button(w3, text="常规数据循环输出", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
                x1_x()
            elif t_rule_num == 3:
                b2 = ttk.Button(w3, text="旧版循环输出【仅限txt文件】", bootstyle="outline", command=entry2__)
                b2.pack(padx=5,pady=5,side='right')
                thread = threading.Thread(target=LoopOutput_X)
                thread.start()

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

    def CountB2_4():
        rule_num = 3
        b2.config(text="旧版循环输出【仅限txt文件】",command=CountB2_2)
        x_save2(rule_num)

    def CountB2_3():
        rule_num = 2
        b2.config(text="常规数据循环输出",command=CountB2_4)
        x_save2(rule_num)

    def CountB2_2():
        rule_num = 1
        b2.config(text="常规文字循环输出",command=CountB2_1)
        x_save2(rule_num)

    def CountB2_1():
        rule_num = 0
        b2.config(text="只循环输出吉值",command=CountB2_3)
        x_save2(rule_num)

    
    def generate_and_display():
        text_widget.delete(1.0, END)
        if combo.get() == "算一卦":
            text_widget.insert(tk.END,XiaoLliuren.numgua())

    combo = ttk.Combobox(window, values=["算一卦"], state="readonly")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    combo.bind("<Button-3>", lambda event: generate_and_display())
    combo.set("算一卦")

    def event_t():
        if down_box.get() == "返回主页":
            window.destroy()
            root.deiconify()

    down_box = ttk.Combobox(window, values=["返回主页"], state="readonly")
    down_box.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    down_box.bind("<Button-3>", lambda event: event_t())
    down_box.set("返回主页")
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
        b2 = ttk.Button(w, text="常规文字循环输出", bootstyle="outline", command=CountB2_1)
        b2.pack(padx=5,pady=5,side='right')
    elif t_rule_num == 0:
        b2 = ttk.Button(w, text="只循环输出吉值", bootstyle="outline", command=CountB2_3)
        b2.pack(padx=5,pady=5,side='right')
    elif t_rule_num == 2:
        b2 = ttk.Button(w, text="常规数据循环输出", bootstyle="outline", command=CountB2_4)
        b2.pack(padx=5,pady=5,side='right')
    elif t_rule_num == 3:
        b2 = ttk.Button(w, text="旧版循环输出【仅限txt文件】", bootstyle="outline", command=CountB2_2)
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

    window.mainloop()
###分割线
#关于紫微斗数###分割线


def gadget():

    def z():
        t = str(load_down_box() or "横排样式")

        def z_judge():
            gain_entry1 = entry1.get()
            gain_entry2 = entry2.get()
            gain_entry3 = entry3.get()
            gain_entry4 = entry4.get()
            gain_combobox = combobox.get()
            r = re.sub(r'[^公元前\d]+', '', gain_entry1)
            r_ = re.sub(r'[^\d]+',"",gain_entry2)
            r__ = re.sub(r'[^\d]+',"",gain_entry3)
            r___ = re.sub(r'[^\d]+',"",gain_entry4)
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
                    date = datetime.datetime(int(re.sub(r'[^\d]+',"",r)), int(r_), int(r__)).date()
                    if not (0 < int(r___) <= 24):
                        messagebox.showerror("错误", message="错误的日期", parent=window)
                    else:
                        ziwei = ZiWeidoushu.ZiWeidoushu(r, r_, r__, r___)
                        nianGan,nianGanwuXing,nianGanyinYang\
            ,nianZhi,nianZhiwuXing,nianZhiyinYang,nianZhishengXiao\
                ,yueGan,yueGanwuXing,yueGanyinYang\
                    ,yueZhi,yueZhiwuXing,yueZhiyinYang,yueZhishengXiao\
                    ,shiChen,shiChenwuXing,shiChenyinYang,shiChenshengXiao\
                        ,Ming,Shen,wuXingju,ziWei\
                            ,JD,NOONJD,MJD\
                                ,riGan,riGanwuXing,ruGanyinYang\
                                    ,riZhi,riZhiwuXing,riZhiyinYang,ruZhishengXiao\
                                    ,shiGan,shiGanwuXing,shiGanyinYang\
                                    ,day\
                                                              = ziwei.ZiWeisoushu()
                        ganZhi = nianGan+nianZhi+yueGan+yueZhi+riGan+riZhi+shiGan+shiChen
                        wuXing = nianGanwuXing+nianZhiwuXing+yueGanwuXing+yueZhiwuXing+riGanwuXing+riZhiwuXing+shiGanwuXing+shiChenwuXing
                        yinYang = nianGanyinYang+nianZhiyinYang+yueGanyinYang+yueZhiyinYang+ruGanyinYang+riZhiyinYang+shiGanyinYang+shiChenyinYang
                        shengXiao = "无"+nianZhishengXiao+"无"+yueZhishengXiao+"无"+ruZhishengXiao+"无"+shiChenshengXiao
                        male_or_female = nianGanyinYang + r____

                        group_w13\
                             = "天干地支：{}\n干支五行：{}\n干支阴阳：{}\n干支生肖：{}\n儒略日【傍晚】：{}\n儒略日【正午】：{}\n简化儒略日：{}\n五行局：{}\n{}\n"\
                            .format(ganZhi,wuXing,yinYang,shengXiao,JD,NOONJD,MJD,wuXingju,male_or_female)

                        def z_t():
                            window_z = ttk.Toplevel()
                            window_z.title("轻量记事本-小工具-紫微斗数-三合派")
                            window_z.iconbitmap(icon_path)
                            w = ttk.Frame(window_z)
                            w.grid(row=0,column=0,padx=10,pady=10)
                            w2 = ttk.Frame(window_z)
                            w2.grid(row=0,column=1,padx=10,pady=10)
                            w3 = ttk.Frame(window_z)
                            w3.grid(row=0,column=2,padx=10,pady=10)
                            w4 = ttk.Frame(window_z)
                            w4.grid(row=0,column=3,padx=10,pady=10)
                            w5 = ttk.Frame(window_z)
                            w5.grid(row=1,column=0,padx=10,pady=10)
                            w6 = ttk.Frame(window_z)
                            w6.grid(row=2,column=0,padx=10,pady=10)
                            w7 = ttk.Frame(window_z)
                            w7.grid(row=3,column=0,padx=10,pady=10)
                            w8 = ttk.Frame(window_z)
                            w8.grid(row=3,column=1,padx=10,pady=10)
                            w9 = ttk.Frame(window_z)
                            w9.grid(row=3,column=2,padx=10,pady=10)
                            w10 = ttk.Frame(window_z)
                            w10.grid(row=3,column=3,padx=10,pady=10)
                            w11 = ttk.Frame(window_z)
                            w11.grid(row=2,column=3,padx=10,pady=10)
                            w12 = ttk.Frame(window_z)
                            w12.grid(row=1,column=3,padx=10,pady=10)
                            w13 = ttk.Frame(window_z)
                            w13.grid(row=1,column=1,rowspan=1,columnspan=1,padx=10,pady=10)
                            def Heavenly():
                                w_l = ttk.Label(w,text="巳",font=font_style)
                                w2_l = ttk.Label(w2,text="午",font=font_style)
                                w3_l = ttk.Label(w3,text="未",font=font_style)
                                w4_l = ttk.Label(w4,text="申",font=font_style)
                                w5_l = ttk.Label(w5,text="辰",font=font_style)
                                w6_l = ttk.Label(w6,text="卯",font=font_style)
                                w7_l = ttk.Label(w7,text="寅",font=font_style)
                                w8_l = ttk.Label(w8,text="丑",font=font_style)
                                w9_l = ttk.Label(w9,text="子",font=font_style)
                                w10_l = ttk.Label(w10,text="亥",font=font_style)
                                w11_l = ttk.Label(w11,text="戌",font=font_style)
                                w12_l = ttk.Label(w12,text="酉",font=font_style)
                                w13_l = ttk.Label(w13,text=group_w13,font=font_style)
                                w_l.grid(row=10,column=0)
                                w2_l.grid(row=10,column=0)
                                w3_l.grid(row=10,column=0)
                                w4_l.grid(row=10,column=0)
                                w5_l.grid(row=10,column=0)
                                w6_l.grid(row=10,column=0)
                                w7_l.grid(row=10,column=0)
                                w8_l.grid(row=10,column=0)
                                w9_l.grid(row=10,column=0)
                                w10_l.grid(row=10,column=0)
                                w11_l.grid(row=10,column=0)
                                w12_l.grid(row=10,column=0)
                                w13_l.grid(row=10,column=0)

                            def twelve_god():
                                match Ming:
                                    case "子":
                                        Ming_ = ttk.Label(w9,text="命",font=font_style)
                                        xiongDi = ttk.Label(w10,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w11,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w12,text="子女",font=font_style)
                                        caiBo = ttk.Label(w4,text="财帛",font=font_style)
                                        jiE = ttk.Label(w3,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w2,text="迁移",font=font_style)
                                        puYi = ttk.Label(w,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w5,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w6,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w7,text="福德",font=font_style)
                                        fuMu = ttk.Label(w8,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "丑":
                                        Ming_ = ttk.Label(w8,text="命",font=font_style)
                                        xiongDi = ttk.Label(w9,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w10,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w11,text="子女",font=font_style)
                                        caiBo = ttk.Label(w12,text="财帛",font=font_style)
                                        jiE = ttk.Label(w4,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w3,text="迁移",font=font_style)
                                        puYi = ttk.Label(w2,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w5,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w6,text="福德",font=font_style)
                                        fuMu = ttk.Label(w7,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "寅":
                                        Ming_ = ttk.Label(w7,text="命",font=font_style)
                                        xiongDi = ttk.Label(w8,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w9,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w10,text="子女",font=font_style)
                                        caiBo = ttk.Label(w11,text="财帛",font=font_style)
                                        jiE = ttk.Label(w12,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w4,text="迁移",font=font_style)
                                        puYi = ttk.Label(w3,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w2,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w5,text="福德",font=font_style)
                                        fuMu = ttk.Label(w6,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "卯":
                                        Ming_ = ttk.Label(w6,text="命",font=font_style)
                                        xiongDi = ttk.Label(w7,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w8,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w9,text="子女",font=font_style)
                                        caiBo = ttk.Label(w10,text="财帛",font=font_style)
                                        jiE = ttk.Label(w11,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w12,text="迁移",font=font_style)
                                        puYi = ttk.Label(w4,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w3,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w2,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w,text="福德",font=font_style)
                                        fuMu = ttk.Label(w5,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "辰":
                                        Ming_ = ttk.Label(w5,text="命",font=font_style)
                                        xiongDi = ttk.Label(w6,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w7,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w8,text="子女",font=font_style)
                                        caiBo = ttk.Label(w9,text="财帛",font=font_style)
                                        jiE = ttk.Label(w10,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w11,text="迁移",font=font_style)
                                        puYi = ttk.Label(w12,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w4,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w3,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w2,text="福德",font=font_style)
                                        fuMu = ttk.Label(w,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "巳":
                                        Ming_ = ttk.Label(w,text="命",font=font_style)
                                        xiongDi = ttk.Label(w5,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w6,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w7,text="子女",font=font_style)
                                        caiBo = ttk.Label(w8,text="财帛",font=font_style)
                                        jiE = ttk.Label(w9,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w10,text="迁移",font=font_style)
                                        puYi = ttk.Label(w11,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w12,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w4,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w3,text="福德",font=font_style)
                                        fuMu = ttk.Label(w2,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "午":
                                        Ming_ = ttk.Label(w2,text="命",font=font_style)
                                        xiongDi = ttk.Label(w,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w5,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w6,text="子女",font=font_style)
                                        caiBo = ttk.Label(w7,text="财帛",font=font_style)
                                        jiE = ttk.Label(w8,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w9,text="迁移",font=font_style)
                                        puYi = ttk.Label(w10,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w11,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w12,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w4,text="福德",font=font_style)
                                        fuMu = ttk.Label(w3,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "未":
                                        Ming_ = ttk.Label(w3,text="命",font=font_style)
                                        xiongDi = ttk.Label(w2,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w5,text="子女",font=font_style)
                                        caiBo = ttk.Label(w6,text="财帛",font=font_style)
                                        jiE = ttk.Label(w7,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w8,text="迁移",font=font_style)
                                        puYi = ttk.Label(w9,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w10,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w11,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w12,text="福德",font=font_style)
                                        fuMu = ttk.Label(w4,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "申":
                                        Ming_ = ttk.Label(w4,text="命",font=font_style)
                                        xiongDi = ttk.Label(w3,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w2,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w,text="子女",font=font_style)
                                        caiBo = ttk.Label(w5,text="财帛",font=font_style)
                                        jiE = ttk.Label(w6,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w7,text="迁移",font=font_style)
                                        puYi = ttk.Label(w8,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w9,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w10,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w11,text="福德",font=font_style)
                                        fuMu = ttk.Label(w12,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "酉":
                                        Ming_ = ttk.Label(w12,text="命",font=font_style)
                                        xiongDi = ttk.Label(w4,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w3,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w2,text="子女",font=font_style)
                                        caiBo = ttk.Label(w,text="财帛",font=font_style)
                                        jiE = ttk.Label(w5,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w6,text="迁移",font=font_style)
                                        puYi = ttk.Label(w7,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w8,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w9,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w10,text="福德",font=font_style)
                                        fuMu = ttk.Label(w11,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "戌":
                                        Ming_ = ttk.Label(w11,text="命",font=font_style)
                                        xiongDi = ttk.Label(w12,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w4,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w3,text="子女",font=font_style)
                                        caiBo = ttk.Label(w2,text="财帛",font=font_style)
                                        jiE = ttk.Label(w,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w5,text="迁移",font=font_style)
                                        puYi = ttk.Label(w6,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w7,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w8,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w9,text="福德",font=font_style)
                                        fuMu = ttk.Label(w10,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                    case "亥":
                                        Ming_ = ttk.Label(w10,text="命",font=font_style)
                                        xiongDi = ttk.Label(w11,text="兄弟",font=font_style)
                                        fuQi = ttk.Label(w12,text="夫妻",font=font_style)
                                        ziNu = ttk.Label(w4,text="子女",font=font_style)
                                        caiBo = ttk.Label(w3,text="财帛",font=font_style)
                                        jiE = ttk.Label(w2,text="疾厄",font=font_style)
                                        qianYi = ttk.Label(w,text="迁移",font=font_style)
                                        puYi = ttk.Label(w5,text="仆役",font=font_style)
                                        guanLu = ttk.Label(w6,text="官禄",font=font_style)
                                        tianZhai = ttk.Label(w7,text="田宅",font=font_style)
                                        fuDe = ttk.Label(w8,text="福德",font=font_style)
                                        fuMu = ttk.Label(w9,text="父母",font=font_style)
                                        Ming_.grid(row=10,column=1)
                                        xiongDi.grid(row=10,column=1)
                                        fuQi.grid(row=10,column=1)
                                        ziNu.grid(row=10,column=1)
                                        caiBo.grid(row=10,column=1)
                                        jiE.grid(row=10,column=1)
                                        qianYi.grid(row=10,column=1)
                                        puYi.grid(row=10,column=1)
                                        guanLu.grid(row=10,column=1)
                                        tianZhai.grid(row=10,column=1)
                                        fuDe.grid(row=10,column=1)
                                        fuMu.grid(row=10,column=1)
                                match Shen:
                                    case "子":
                                        Shen_ = ttk.Label(w9,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "丑":
                                        Shen_ = ttk.Label(w8,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "寅":
                                        Shen_ = ttk.Label(w7,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "卯":
                                        Shen_ = ttk.Label(w6,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "辰":
                                        Shen_ = ttk.Label(w5,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "巳":
                                        Shen_ = ttk.Label(w,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "午":
                                        Shen_ = ttk.Label(w2,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "未":
                                        Shen_ = ttk.Label(w3,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "申":
                                        Shen_ = ttk.Label(w4,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "酉":
                                        Shen_ = ttk.Label(w12,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "戌":
                                        Shen_ = ttk.Label(w11,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)
                                    case "亥":
                                        Shen_ = ttk.Label(w10,text="身",font=font_style)
                                        Shen_.grid(row=9,column=1)

                            def person():
                                match nianGan:
                                    case "甲"|"己":
                                        _ = ttk.Label(w7,text="丙",font=font_style)
                                        __ = ttk.Label(w6,text="丁",font=font_style)
                                        ___ = ttk.Label(w5,text="戊",font=font_style)
                                        ____ = ttk.Label(w,text="己",font=font_style)
                                        _____ = ttk.Label(w2,text="庚",font=font_style)
                                        ______ = ttk.Label(w3,text="庚",font=font_style)
                                        _______ = ttk.Label(w4,text="壬",font=font_style)
                                        ________ = ttk.Label(w12,text="癸",font=font_style)
                                        _________ = ttk.Label(w11,text="甲",font=font_style)
                                        __________ = ttk.Label(w10,text="乙",font=font_style)
                                        ___________ = ttk.Label(w9,text="丙",font=font_style)
                                        ____________ = ttk.Label(w8,text="丁",font=font_style)
                                        _.grid(row=9,column=0)
                                        __.grid(row=9,column=0)
                                        ___.grid(row=9,column=0)
                                        ____.grid(row=9,column=0)
                                        _____.grid(row=9,column=0)
                                        ______.grid(row=9,column=0)
                                        _______.grid(row=9,column=0)
                                        ________.grid(row=9,column=0)
                                        _________.grid(row=9,column=0)
                                        __________.grid(row=9,column=0)
                                        ___________.grid(row=9,column=0)
                                        ____________.grid(row=9,column=0)
                                    case "乙"|"庚":
                                        _ = ttk.Label(w7,text="戊",font=font_style)
                                        __ = ttk.Label(w6,text="己",font=font_style)
                                        ___ = ttk.Label(w5,text="庚",font=font_style)
                                        ____ = ttk.Label(w,text="辛",font=font_style)
                                        _____ = ttk.Label(w2,text="壬",font=font_style)
                                        ______ = ttk.Label(w3,text="癸",font=font_style)
                                        _______ = ttk.Label(w4,text="甲",font=font_style)
                                        ________ = ttk.Label(w12,text="乙",font=font_style)
                                        _________ = ttk.Label(w11,text="丙",font=font_style)
                                        __________ = ttk.Label(w10,text="丁",font=font_style)
                                        ___________ = ttk.Label(w9,text="戊",font=font_style)
                                        ____________ = ttk.Label(w8,text="己",font=font_style)
                                        _.grid(row=9,column=0)
                                        __.grid(row=9,column=0)
                                        ___.grid(row=9,column=0)
                                        ____.grid(row=9,column=0)
                                        _____.grid(row=9,column=0)
                                        ______.grid(row=9,column=0)
                                        _______.grid(row=9,column=0)
                                        ________.grid(row=9,column=0)
                                        _________.grid(row=9,column=0)
                                        __________.grid(row=9,column=0)
                                        ___________.grid(row=9,column=0)
                                        ____________.grid(row=9,column=0)
                                    case "丙"|"辛":
                                        _ = ttk.Label(w7,text="庚",font=font_style)
                                        __ = ttk.Label(w6,text="辛",font=font_style)
                                        ___ = ttk.Label(w5,text="壬",font=font_style)
                                        ____ = ttk.Label(w,text="癸",font=font_style)
                                        _____ = ttk.Label(w2,text="甲",font=font_style)
                                        ______ = ttk.Label(w3,text="乙",font=font_style)
                                        _______ = ttk.Label(w4,text="丙",font=font_style)
                                        ________ = ttk.Label(w12,text="丁",font=font_style)
                                        _________ = ttk.Label(w11,text="戊",font=font_style)
                                        __________ = ttk.Label(w10,text="己",font=font_style)
                                        ___________ = ttk.Label(w9,text="庚",font=font_style)
                                        ____________ = ttk.Label(w8,text="辛",font=font_style)
                                        _.grid(row=9,column=0)
                                        __.grid(row=9,column=0)
                                        ___.grid(row=9,column=0)
                                        ____.grid(row=9,column=0)
                                        _____.grid(row=9,column=0)
                                        ______.grid(row=9,column=0)
                                        _______.grid(row=9,column=0)
                                        ________.grid(row=9,column=0)
                                        _________.grid(row=9,column=0)
                                        __________.grid(row=9,column=0)
                                        ___________.grid(row=9,column=0)
                                        ____________.grid(row=9,column=0)
                                    case "丁"|"壬":
                                        _ = ttk.Label(w7,text="壬",font=font_style)
                                        __ = ttk.Label(w6,text="癸",font=font_style)
                                        ___ = ttk.Label(w5,text="甲",font=font_style)
                                        ____ = ttk.Label(w,text="乙",font=font_style)
                                        _____ = ttk.Label(w2,text="丙",font=font_style)
                                        ______ = ttk.Label(w3,text="丁",font=font_style)
                                        _______ = ttk.Label(w4,text="戊",font=font_style)
                                        ________ = ttk.Label(w12,text="己",font=font_style)
                                        _________ = ttk.Label(w11,text="庚",font=font_style)
                                        __________ = ttk.Label(w10,text="辛",font=font_style)
                                        ___________ = ttk.Label(w9,text="壬")
                                        ____________ = ttk.Label(w8,text="癸",font=font_style)
                                        _.grid(row=9,column=0)
                                        __.grid(row=9,column=0)
                                        ___.grid(row=9,column=0)
                                        ____.grid(row=9,column=0)
                                        _____.grid(row=9,column=0)
                                        ______.grid(row=9,column=0)
                                        _______.grid(row=9,column=0)
                                        ________.grid(row=9,column=0)
                                        _________.grid(row=9,column=0)
                                        __________.grid(row=9,column=0)
                                        ___________.grid(row=9,column=0)
                                        ____________.grid(row=9,column=0)
                                    case "戊"|"癸":
                                        _ = ttk.Label(w7,text="甲",font=font_style)
                                        __ = ttk.Label(w6,text="乙",font=font_style)
                                        ___ = ttk.Label(w5,text="丙",font=font_style)
                                        ____ = ttk.Label(w,text="丁",font=font_style)
                                        _____ = ttk.Label(w2,text="戊",font=font_style)
                                        ______ = ttk.Label(w3,text="己",font=font_style)
                                        _______ = ttk.Label(w4,text="庚",font=font_style)
                                        ________ = ttk.Label(w12,text="辛",font=font_style)
                                        _________ = ttk.Label(w11,text="壬",font=font_style)
                                        __________ = ttk.Label(w10,text="癸",font=font_style)
                                        ___________ = ttk.Label(w9,text="甲",font=font_style)
                                        ____________ = ttk.Label(w8,text="乙",font=font_style)
                                        _.grid(row=9,column=0)
                                        __.grid(row=9,column=0)
                                        ___.grid(row=9,column=0)
                                        ____.grid(row=9,column=0)
                                        _____.grid(row=9,column=0)
                                        ______.grid(row=9,column=0)
                                        _______.grid(row=9,column=0)
                                        ________.grid(row=9,column=0)
                                        _________.grid(row=9,column=0)
                                        __________.grid(row=9,column=0)
                                        ___________.grid(row=9,column=0)
                                        ____________.grid(row=9,column=0)

                            def confirm_ziWei_and_ziWei_five():
                                match ziWei:
                                    case "子":
                                        ziWei_ = ttk.Label(w9,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w10,text="天机",font=font_style)
                                        taiYang = ttk.Label(w12,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w4,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w3,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w5,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w5,text="天府",font=font_style)
                                        taiYin = ttk.Label(w,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w2,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w3,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w4,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w12,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w11,text="七杀",font=font_style)
                                        poJun = ttk.Label(w7,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w5,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w7,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w4,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w12,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w10,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w12,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w9,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w3,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w10,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w5,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w3,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w10,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w3,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w2,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w10,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w4,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w2,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w12,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w12,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w4,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w3,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w3,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w12,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w12,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w9,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w4,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w7,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w3,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w2,text="贪狼【忌】",font=font_style)          
                                    case "丑":
                                        ziWei_ = ttk.Label(w8,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w9,text="天机",font=font_style)
                                        taiYang = ttk.Label(w11,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w12,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w4,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w6,text="天府",font=font_style)
                                        taiYin = ttk.Label(w5,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w2,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w3,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w4,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w12,text="七杀",font=font_style)
                                        poJun = ttk.Label(w8,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w8,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w12,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w5,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w9,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w4,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w8,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w5,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w4,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w9,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w5,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w4,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w9,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w2,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w5,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w9,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w12,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w4,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w11,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w12,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w5,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w4,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w2,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w11,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w4,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w8,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w12,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w8,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w2,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w5,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w,text="贪狼【忌】",font=font_style)
                                    case "寅":
                                        ziWei_ = ttk.Label(w7,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w8,text="天机",font=font_style)
                                        taiYang = ttk.Label(w10,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w11,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w12,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w2,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w7,text="天府",font=font_style)
                                        taiYin = ttk.Label(w6,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w5,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w2,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w3,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w4,text="七杀",font=font_style)
                                        poJun = ttk.Label(w9,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w2,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w9,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w11,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w10,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w8,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w3,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w7,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w6,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w12,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w8,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w2,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w6,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w12,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w8,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w5,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w6,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w8,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w11,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w5,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w3,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w10,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w11,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w6,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w12,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w10,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w3,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w7,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w11,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w9,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w6,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w5,text="贪狼【忌】",font=font_style)
                                    case "卯":
                                        ziWei_ = ttk.Label(w6,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w7,text="天机",font=font_style)
                                        taiYang = ttk.Label(w9,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w10,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w11,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w3,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w8,text="天府",font=font_style)
                                        taiYin = ttk.Label(w7,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w6,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w5,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w2,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w3,text="七杀",font=font_style)
                                        poJun = ttk.Label(w10,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w3,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w10,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w10,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w9,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w7,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w2,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w6,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w7,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w11,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w7,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w3,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w7,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w11,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w7,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w5,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w6,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w7,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w7,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w10,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w6,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w2,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w9,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w10,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w7,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w11,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w5,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w9,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w2,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w6,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w10,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w10,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w5,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w7,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w6,text="贪狼【忌】",font=font_style)
                                    case "辰":
                                        ziWei_ = ttk.Label(w5,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w6,text="天机",font=font_style)
                                        taiYang = ttk.Label(w8,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w9,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w10,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w4,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w9,text="天府",font=font_style)
                                        taiYin = ttk.Label(w8,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w7,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w6,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w5,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w2,text="七杀",font=font_style)
                                        poJun = ttk.Label(w11,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w4,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w11,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w9,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w8,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w6,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w5,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w8,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w10,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w6,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w4,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w8,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w10,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w6,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w6,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w7,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w8,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w6,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w9,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w7,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w8,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w9,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w8,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w10,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w6,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w8,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w5,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w9,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w11,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w6,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w8,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w7,text="贪狼【忌】",font=font_style)
                                    case "巳":
                                        ziWei_ = ttk.Label(w,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w5,text="天机",font=font_style)
                                        taiYang = ttk.Label(w7,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w8,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w9,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w12,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w10,text="天府",font=font_style)
                                        taiYin = ttk.Label(w9,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w8,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w7,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w6,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w5,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w,text="七杀",font=font_style)
                                        poJun = ttk.Label(w12,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w12,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w12,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w8,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w7,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w5,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w5,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w9,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w9,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w5,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w12,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w9,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w9,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w5,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w7,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w8,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w9,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w5,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w9,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w8,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w5,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w7,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w8,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w9,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w9,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w7,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w7,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w5,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w8,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w12,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w7,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w9,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w8,text="贪狼【忌】",font=font_style)
                                    case "午":
                                        ziWei_ = ttk.Label(w2,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w,text="天机",font=font_style)
                                        taiYang = ttk.Label(w6,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w7,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w8,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w11,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w11,text="天府",font=font_style)
                                        taiYin = ttk.Label(w10,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w9,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w8,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w7,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w6,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w5,text="七杀",font=font_style)
                                        poJun = ttk.Label(w4,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w11,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w4,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w7,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w6,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w6,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w2,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w10,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w8,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w11,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w10,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w8,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w8,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w9,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w10,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w7,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w9,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w6,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w6,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w7,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w10,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w8,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w8,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w6,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w6,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w2,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w7,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w4,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w8,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w10,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w9,text="贪狼【忌】",font=font_style)
                                    case "未":
                                        ziWei_ = ttk.Label(w3,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w2,text="天机",font=font_style)
                                        taiYang = ttk.Label(w5,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w6,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w7,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w10,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w12,text="天府",font=font_style)
                                        taiYin = ttk.Label(w11,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w10,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w9,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w8,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w7,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w6,text="七杀",font=font_style)
                                        poJun = ttk.Label(w3,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w10,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w3,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w6,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w5,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w2,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w7,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w3,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w11,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w7,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w2,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w10,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w11,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w7,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w2,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w9,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w10,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w11,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w2,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w6,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w10,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w7,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w5,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w6,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w11,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w7,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w9,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w5,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w7,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w3,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w6,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w3,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w9,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w11,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w10,text="贪狼【忌】",font=font_style)
                                    case "申":
                                        ziWei_ = ttk.Label(w4,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w3,text="天机",font=font_style)
                                        taiYang = ttk.Label(w,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w5,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w6,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w9,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w4,text="天府",font=font_style)
                                        taiYin = ttk.Label(w12,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w11,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w10,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w9,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w8,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w7,text="七杀",font=font_style)
                                        poJun = ttk.Label(w2,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w9,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w2,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w5,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w3,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w8,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w4,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w12,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w6,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w3,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w9,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w12,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w6,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w3,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w10,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w11,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w12,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w3,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w5,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w11,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w8,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w5,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w12,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w6,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w10,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w8,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w4,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w5,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w2,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w10,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w12,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w11,text="贪狼【忌】",font=font_style)
                                    case "酉":
                                        ziWei_ = ttk.Label(w12,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w4,text="天机",font=font_style)
                                        taiYang = ttk.Label(w2,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w5,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w8,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w3,text="天府",font=font_style)
                                        taiYin = ttk.Label(w4,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w12,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w11,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w10,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w9,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w8,text="七杀",font=font_style)
                                        poJun = ttk.Label(w,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w8,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w2,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w4,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w9,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w12,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w4,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w5,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w4,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w8,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w4,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w5,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w4,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w11,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w12,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w4,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w4,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w12,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w9,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w2,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w4,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w5,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w11,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w2,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w9,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w12,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w11,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w4,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w12,text="贪狼【忌】",font=font_style)
                                    case "戌":
                                        ziWei_ = ttk.Label(w11,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w12,text="天机",font=font_style)
                                        taiYang = ttk.Label(w3,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w2,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w7,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w2,text="天府",font=font_style)
                                        taiYin = ttk.Label(w3,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w4,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w12,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w11,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w10,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w9,text="七杀",font=font_style)
                                        poJun = ttk.Label(w5,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w7,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w5,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w2,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w3,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w12,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w10,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w11,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w3,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w12,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w7,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w3,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w12,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w12,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w4,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w3,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w12,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w2,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w4,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w10,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w3,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w2,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w3,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w12,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w3,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w10,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w11,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w2,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w5,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w12,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w3,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w4,text="贪狼【忌】",font=font_style)
                                    case "亥":
                                        ziWei_ = ttk.Label(w10,text="紫微",font=font_style)
                                        tianJi = ttk.Label(w11,text="天机",font=font_style)
                                        taiYang = ttk.Label(w4,text="太阳",font=font_style)
                                        wuQu = ttk.Label(w3,text="武曲",font=font_style)
                                        tianTong = ttk.Label(w2,text="天同",font=font_style)
                                        lianZhen = ttk.Label(w6,text="廉贞",font=font_style)
                                        tianFu = ttk.Label(w,text="天府",font=font_style)
                                        taiYin = ttk.Label(w2,text="太阴",font=font_style)
                                        tanLang = ttk.Label(w3,text="贪狼",font=font_style)
                                        juMen = ttk.Label(w4,text="巨门",font=font_style)
                                        taiXiang = ttk.Label(w12,text="天相",font=font_style)
                                        tianLiang = ttk.Label(w11,text="天梁",font=font_style)
                                        qiSha = ttk.Label(w10,text="七杀",font=font_style)
                                        poJun = ttk.Label(w6,text="破军",font=font_style)
                                        match nianGan:
                                            case "甲":
                                                禄存 = ttk.Label(w7,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w6,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w8,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w3,text="天官",font=font_style)
                                                天福 = ttk.Label(w12,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                lianZhen = ttk.Label(w6,text="廉贞【禄】",font=font_style)
                                                poJun = ttk.Label(w6,text="破军【权】",font=font_style)
                                                wuQu = ttk.Label(w3,text="武曲【科】",font=font_style)
                                                taiYang = ttk.Label(w4,text="太阳【忌】",font=font_style)
                                            case "乙":
                                                禄存 = ttk.Label(w6,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w5,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w7,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w5,text="天官",font=font_style)
                                                天福 = ttk.Label(w4,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tianJi = ttk.Label(w11,text="天机【禄】",font=font_style)
                                                tianLiang = ttk.Label(w11,text="天梁【权】",font=font_style)
                                                ziWei_ = ttk.Label(w10,text="紫微【科】",font=font_style)
                                                taiYin = ttk.Label(w2,text="太阴【忌】",font=font_style)
                                            case "丙":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w,text="天官",font=font_style)
                                                天福 = ttk.Label(w9,text="天福",font=font_style)
                                                天厨 = ttk.Label(w9,text="天厨",font=font_style)
                                                tianTong = ttk.Label(w2,text="天同【禄】",font=font_style)
                                                tianJi = ttk.Label(w11,text="天机【权】",font=font_style)
                                                lianZhen = ttk.Label(w6,text="廉贞【忌】",font=font_style)
                                            case "丁":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w10,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w12,text="天钺",font=font_style)
                                                天官 = ttk.Label(w7,text="天官",font=font_style)
                                                天福 = ttk.Label(w10,text="天福",font=font_style)
                                                天厨 = ttk.Label(w,text="天厨",font=font_style)
                                                taiYin = ttk.Label(w2,text="太阴【禄】",font=font_style)
                                                tianTong = ttk.Label(w2,text="天同【权】",font=font_style)
                                                tianJi = ttk.Label(w11,text="天机【科】",font=font_style)
                                                juMen = ttk.Label(w4,text="巨门【忌】",font=font_style)
                                            case "戊":
                                                禄存 = ttk.Label(w,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w2,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w5,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w6,text="天官",font=font_style)
                                                天福 = ttk.Label(w6,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                tanLang = ttk.Label(w3,text="贪狼【禄】",font=font_style)
                                                taiYin = ttk.Label(w2,text="太阴【权】",font=font_style)
                                                tianJi = ttk.Label(w11,text="天机【忌】",font=font_style)
                                            case "己":
                                                禄存 = ttk.Label(w2,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w3,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w9,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w4,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w7,text="天福",font=font_style)
                                                天厨 = ttk.Label(w4,text="天厨",font=font_style)
                                                wuQu = ttk.Label(w3,text="武曲【禄】",font=font_style)
                                                tanLang = ttk.Label(w3,text="贪狼【权】",font=font_style)
                                                tianLiang = ttk.Label(w11,text="天梁【科】",font=font_style)
                                            case "庚":
                                                禄存 = ttk.Label(w4,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w12,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w3,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w8,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w3,text="天钺",font=font_style)
                                                天官 = ttk.Label(w10,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w7,text="天厨",font=font_style)
                                                taiYang = ttk.Label(w4,text="太阳【禄】",font=font_style)
                                                wuQu = ttk.Label(w3,text="武曲【权】",font=font_style)
                                                taiYin = ttk.Label(w2,text="太阴【科】",font=font_style)
                                                tianTong = ttk.Label(w2,text="天同【忌】",font=font_style)
                                            case "辛":
                                                禄存 = ttk.Label(w12,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w11,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w4,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w2,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w7,text="天钺",font=font_style)
                                                天官 = ttk.Label(w12,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w2,text="天厨",font=font_style)
                                                juMen = ttk.Label(w4,text="巨门【禄】",font=font_style)
                                                taiYang = ttk.Label(w4,text="太阳【权】",font=font_style)
                                            case "壬":
                                                禄存 = ttk.Label(w10,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w9,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w11,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w11,text="天官",font=font_style)
                                                天福 = ttk.Label(w2,text="天福",font=font_style)
                                                天厨 = ttk.Label(w12,text="天厨",font=font_style)
                                                tianLiang = ttk.Label(w11,text="天梁【禄】",font=font_style)
                                                ziWei_ = ttk.Label(w10,text="紫微【权】",font=font_style)
                                                wuQu = ttk.Label(w3,text="武曲【忌】",font=font_style)
                                            case "癸":
                                                禄存 = ttk.Label(w9,text="禄存",font=font_style)
                                                擎羊 = ttk.Label(w8,text="擎羊",font=font_style)
                                                陀罗 = ttk.Label(w10,text="陀罗",font=font_style)
                                                天魁 = ttk.Label(w6,text="天魁",font=font_style)
                                                天钺 = ttk.Label(w,text="天钺",font=font_style)
                                                天官 = ttk.Label(w2,text="天官",font=font_style)
                                                天福 = ttk.Label(w,text="天福",font=font_style)
                                                天厨 = ttk.Label(w10,text="天厨",font=font_style)
                                                poJun = ttk.Label(w6,text="破军【禄】",font=font_style)
                                                juMen = ttk.Label(w4,text="巨门【权】",font=font_style)
                                                taiYin = ttk.Label(w2,text="太阴【科】",font=font_style)
                                                tanLang = ttk.Label(w3,text="贪狼【忌】",font=font_style)

                                match male_or_female:
                                    case "阳男"|"阴女":
                                        match nianGan:
                                            case "甲":
                                                博士 = ttk.Label(w7,text="博士",font=font_style)
                                                力士 = ttk.Label(w6,text="力士",font=font_style)
                                                青龙 = ttk.Label(w5,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w,text="小耗",font=font_style)
                                                将军 = ttk.Label(w2,text="将军",font=font_style)
                                                奏书 = ttk.Label(w3,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w4,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w12,text="喜神",font=font_style)
                                                病符 = ttk.Label(w11,text="病符",font=font_style)
                                                大耗 = ttk.Label(w10,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w9,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w8,text="官府",font=font_style)
                                            case "乙":
                                                博士 = ttk.Label(w6,text="博士",font=font_style)
                                                力士 = ttk.Label(w5,text="力士",font=font_style)
                                                青龙 = ttk.Label(w,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w2,text="小耗",font=font_style)
                                                将军 = ttk.Label(w3,text="将军",font=font_style)
                                                奏书 = ttk.Label(w4,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w12,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w11,text="喜神",font=font_style)
                                                病符 = ttk.Label(w10,text="病符",font=font_style)
                                                大耗 = ttk.Label(w9,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w8,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w7,text="官府",font=font_style)
                                            case "丙":
                                                博士 = ttk.Label(w,text="博士",font=font_style)
                                                力士 = ttk.Label(w2,text="力士",font=font_style)
                                                青龙 = ttk.Label(w3,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w4,text="小耗",font=font_style)
                                                将军 = ttk.Label(w12,text="将军",font=font_style)
                                                奏书 = ttk.Label(w11,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w10,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w9,text="喜神",font=font_style)
                                                病符 = ttk.Label(w8,text="病符",font=font_style)
                                                大耗 = ttk.Label(w7,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w6,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w5,text="官府",font=font_style)
                                            case "丁":
                                                博士 = ttk.Label(w2,text="博士",font=font_style)
                                                力士 = ttk.Label(w3,text="力士",font=font_style)
                                                青龙 = ttk.Label(w4,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w12,text="小耗",font=font_style)
                                                将军 = ttk.Label(w11,text="将军",font=font_style)
                                                奏书 = ttk.Label(w10,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w9,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w8,text="喜神",font=font_style)
                                                病符 = ttk.Label(w7,text="病符",font=font_style)
                                                大耗 = ttk.Label(w6,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w5,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w,text="官府",font=font_style)
                                            case "戊":
                                                博士 = ttk.Label(w,text="博士",font=font_style)
                                                力士 = ttk.Label(w2,text="力士",font=font_style)
                                                青龙 = ttk.Label(w3,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w4,text="小耗",font=font_style)
                                                将军 = ttk.Label(w12,text="将军",font=font_style)
                                                奏书 = ttk.Label(w11,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w10,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w9,text="喜神",font=font_style)
                                                病符 = ttk.Label(w8,text="病符",font=font_style)
                                                大耗 = ttk.Label(w7,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w6,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w5,text="官府",font=font_style)
                                            case "己":
                                                博士 = ttk.Label(w2,text="博士",font=font_style)
                                                力士 = ttk.Label(w3,text="力士",font=font_style)
                                                青龙 = ttk.Label(w4,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w12,text="小耗",font=font_style)
                                                将军 = ttk.Label(w11,text="将军",font=font_style)
                                                奏书 = ttk.Label(w10,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w9,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w8,text="喜神",font=font_style)
                                                病符 = ttk.Label(w7,text="病符",font=font_style)
                                                大耗 = ttk.Label(w6,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w5,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w,text="官府",font=font_style)
                                            case "庚":
                                                博士 = ttk.Label(w4,text="博士",font=font_style)
                                                力士 = ttk.Label(w12,text="力士",font=font_style)
                                                青龙 = ttk.Label(w11,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w10,text="小耗",font=font_style)
                                                将军 = ttk.Label(w9,text="将军",font=font_style)
                                                奏书 = ttk.Label(w8,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w7,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w6,text="喜神",font=font_style)
                                                病符 = ttk.Label(w5,text="病符",font=font_style)
                                                大耗 = ttk.Label(w,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w2,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w3,text="官府",font=font_style)
                                            case "辛":
                                                博士 = ttk.Label(w12,text="博士",font=font_style)
                                                力士 = ttk.Label(w11,text="力士",font=font_style)
                                                青龙 = ttk.Label(w10,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w9,text="小耗",font=font_style)
                                                将军 = ttk.Label(w8,text="将军",font=font_style)
                                                奏书 = ttk.Label(w7,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w6,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w5,text="喜神",font=font_style)
                                                病符 = ttk.Label(w,text="病符",font=font_style)
                                                大耗 = ttk.Label(w2,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w3,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w4,text="官府",font=font_style)
                                            case "壬":
                                                博士 = ttk.Label(w10,text="博士",font=font_style)
                                                力士 = ttk.Label(w9,text="力士",font=font_style)
                                                青龙 = ttk.Label(w8,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w7,text="小耗",font=font_style)
                                                将军 = ttk.Label(w6,text="将军",font=font_style)
                                                奏书 = ttk.Label(w5,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w2,text="喜神",font=font_style)
                                                病符 = ttk.Label(w3,text="病符",font=font_style)
                                                大耗 = ttk.Label(w4,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w12,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w11,text="官府",font=font_style)
                                            case "癸":
                                                博士 = ttk.Label(w9,text="博士",font=font_style)
                                                力士 = ttk.Label(w8,text="力士",font=font_style)
                                                青龙 = ttk.Label(w7,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w6,text="小耗",font=font_style)
                                                将军 = ttk.Label(w5,text="将军",font=font_style)
                                                奏书 = ttk.Label(w,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w2,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w3,text="喜神",font=font_style)
                                                病符 = ttk.Label(w4,text="病符",font=font_style)
                                                大耗 = ttk.Label(w12,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w11,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w10,text="官府",font=font_style)
                                    case "阴男"|"阳女":
                                        match nianGan:
                                            case "甲":
                                                博士 = ttk.Label(w7,text="博士",font=font_style)
                                                力士 = ttk.Label(w8,text="力士",font=font_style)
                                                青龙 = ttk.Label(w9,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w10,text="小耗",font=font_style)
                                                将军 = ttk.Label(w11,text="将军",font=font_style)
                                                奏书 = ttk.Label(w12,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w4,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w3,text="喜神",font=font_style)
                                                病符 = ttk.Label(w2,text="病符",font=font_style)
                                                大耗 = ttk.Label(w,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w5,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w6,text="官府",font=font_style)
                                            case "乙":
                                                博士 = ttk.Label(w6,text="博士",font=font_style)
                                                力士 = ttk.Label(w7,text="力士",font=font_style)
                                                青龙 = ttk.Label(w8,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w9,text="小耗",font=font_style)
                                                将军 = ttk.Label(w10,text="将军",font=font_style)
                                                奏书 = ttk.Label(w11,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w12,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w4,text="喜神",font=font_style)
                                                病符 = ttk.Label(w3,text="病符",font=font_style)
                                                大耗 = ttk.Label(w2,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w5,text="官府",font=font_style)
                                            case "丙":
                                                博士 = ttk.Label(w,text="博士",font=font_style)
                                                力士 = ttk.Label(w5,text="力士",font=font_style)
                                                青龙 = ttk.Label(w6,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w7,text="小耗",font=font_style)
                                                将军 = ttk.Label(w8,text="将军",font=font_style)
                                                奏书 = ttk.Label(w9,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w10,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w11,text="喜神",font=font_style)
                                                病符 = ttk.Label(w12,text="病符",font=font_style)
                                                大耗 = ttk.Label(w4,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w3,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w2,text="官府",font=font_style)
                                            case "丁":
                                                博士 = ttk.Label(w2,text="博士",font=font_style)
                                                力士 = ttk.Label(w,text="力士",font=font_style)
                                                青龙 = ttk.Label(w5,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w6,text="小耗",font=font_style)
                                                将军 = ttk.Label(w7,text="将军",font=font_style)
                                                奏书 = ttk.Label(w8,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w9,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w10,text="喜神",font=font_style)
                                                病符 = ttk.Label(w11,text="病符",font=font_style)
                                                大耗 = ttk.Label(w12,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w4,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w3,text="官府",font=font_style)
                                            case "戊":
                                                博士 = ttk.Label(w,text="博士",font=font_style)
                                                力士 = ttk.Label(w5,text="力士",font=font_style)
                                                青龙 = ttk.Label(w6,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w7,text="小耗",font=font_style)
                                                将军 = ttk.Label(w8,text="将军",font=font_style)
                                                奏书 = ttk.Label(w9,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w10,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w11,text="喜神",font=font_style)
                                                病符 = ttk.Label(w12,text="病符",font=font_style)
                                                大耗 = ttk.Label(w4,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w3,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w2,text="官府",font=font_style)
                                            case "己":
                                                博士 = ttk.Label(w2,text="博士",font=font_style)
                                                力士 = ttk.Label(w,text="力士",font=font_style)
                                                青龙 = ttk.Label(w5,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w6,text="小耗",font=font_style)
                                                将军 = ttk.Label(w7,text="将军",font=font_style)
                                                奏书 = ttk.Label(w8,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w9,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w10,text="喜神",font=font_style)
                                                病符 = ttk.Label(w11,text="病符",font=font_style)
                                                大耗 = ttk.Label(w12,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w4,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w3,text="官府",font=font_style)
                                            case "庚":
                                                博士 = ttk.Label(w4,text="博士",font=font_style)
                                                力士 = ttk.Label(w3,text="力士",font=font_style)
                                                青龙 = ttk.Label(w2,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w,text="小耗",font=font_style)
                                                将军 = ttk.Label(w5,text="将军",font=font_style)
                                                奏书 = ttk.Label(w6,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w7,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w8,text="喜神",font=font_style)
                                                病符 = ttk.Label(w9,text="病符",font=font_style)
                                                大耗 = ttk.Label(w10,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w11,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w12,text="官府",font=font_style)
                                            case "辛":
                                                博士 = ttk.Label(w12,text="博士",font=font_style)
                                                力士 = ttk.Label(w4,text="力士",font=font_style)
                                                青龙 = ttk.Label(w3,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w2,text="小耗",font=font_style)
                                                将军 = ttk.Label(w,text="将军",font=font_style)
                                                奏书 = ttk.Label(w5,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w6,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w7,text="喜神",font=font_style)
                                                病符 = ttk.Label(w8,text="病符",font=font_style)
                                                大耗 = ttk.Label(w9,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w10,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w11,text="官府",font=font_style)
                                            case "壬":
                                                博士 = ttk.Label(w10,text="博士",font=font_style)
                                                力士 = ttk.Label(w11,text="力士",font=font_style)
                                                青龙 = ttk.Label(w12,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w4,text="小耗",font=font_style)
                                                将军 = ttk.Label(w3,text="将军",font=font_style)
                                                奏书 = ttk.Label(w2,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w5,text="喜神",font=font_style)
                                                病符 = ttk.Label(w6,text="病符",font=font_style)
                                                大耗 = ttk.Label(w7,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w8,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w9,text="官府",font=font_style)
                                            case "癸":
                                                博士 = ttk.Label(w9,text="博士",font=font_style)
                                                力士 = ttk.Label(w10,text="力士",font=font_style)
                                                青龙 = ttk.Label(w11,text="青龙",font=font_style)
                                                小耗 = ttk.Label(w12,text="小耗",font=font_style)
                                                将军 = ttk.Label(w4,text="将军",font=font_style)
                                                奏书 = ttk.Label(w3,text="奏书",font=font_style)
                                                飞廉 = ttk.Label(w2,text="飞廉",font=font_style)
                                                喜神 = ttk.Label(w,text="喜神",font=font_style)
                                                病符 = ttk.Label(w5,text="病符",font=font_style)
                                                大耗 = ttk.Label(w6,text="大耗",font=font_style)
                                                伏兵 = ttk.Label(w7,text="伏兵",font=font_style)
                                                官府 = ttk.Label(w8,text="官府",font=font_style)

                                        


                                def grid_deploy():
                                    ziWei_.grid(row=8,column=0)
                                    tianJi.grid(row=8,column=0)
                                    taiYang.grid(row=8,column=0)
                                    wuQu.grid(row=8,column=0)
                                    tianTong.grid(row=8,column=0)
                                    lianZhen.grid(row=8,column=0)
                                    tianFu.grid(row=8,column=1)
                                    taiYin.grid(row=8,column=1)
                                    tanLang.grid(row=8,column=1)
                                    juMen.grid(row=8,column=1)
                                    taiXiang.grid(row=8,column=1)
                                    tianLiang.grid(row=8,column=1)
                                    qiSha.grid(row=8,column=1)
                                    poJun.grid(row=8,column=1)
                                    禄存.grid(row=8,column=10)
                                    擎羊.grid(row=8,column=11)
                                    陀罗.grid(row=8,column=12)
                                    天魁.grid(row=8,column=13)
                                    天钺.grid(row=8,column=14)

                                    天官.grid(row=7,column=13)
                                    天福.grid(row=7,column=14)
                                    天厨.grid(row=7,column=15)

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



                                grid_deploy()

                            def confirm_ziWei_time_and_month_and_day_group():
                                
                                match nianZhi:
                                    case "戌"|"午"|"寅":
                                        match shiChen:
                                            case "子":
                                                wenChang = ttk.Label(w11,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w5,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w8,text="火星",font=font_style)
                                                lingXing = ttk.Label(w6,text="铃星",font=font_style)
                                                diJie = ttk.Label(w10,text="地劫",font=font_style)
                                                dikong = ttk.Label(w10,text="地空",font=font_style)
                                                taiFu = ttk.Label(w2,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w7,text="封诰",font=font_style)
                                            case "丑":
                                                wenChang = ttk.Label(w12,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w7,text="火星",font=font_style)
                                                lingXing = ttk.Label(w5,text="铃星",font=font_style)
                                                diJie = ttk.Label(w9,text="地劫",font=font_style)
                                                dikong = ttk.Label(w11,text="地空",font=font_style)
                                                taiFu = ttk.Label(w3,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w6,text="封诰",font=font_style)
                                            case "寅":
                                                wenChang = ttk.Label(w4,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w2,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w6,text="火星",font=font_style)
                                                lingXing = ttk.Label(w,text="铃星",font=font_style)
                                                diJie = ttk.Label(w8,text="地劫",font=font_style)
                                                dikong = ttk.Label(w12,text="地空",font=font_style)
                                                taiFu = ttk.Label(w4,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w5,text="封诰",font=font_style)
                                            case "卯":
                                                wenChang = ttk.Label(w3,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w3,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w5,text="火星",font=font_style)
                                                lingXing = ttk.Label(w2,text="铃星",font=font_style)
                                                diJie = ttk.Label(w7,text="地劫",font=font_style)
                                                dikong = ttk.Label(w4,text="地空",font=font_style)
                                                taiFu = ttk.Label(w12,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w,text="封诰",font=font_style)
                                            case "辰":
                                                wenChang = ttk.Label(w2,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w4,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w,text="火星",font=font_style)
                                                lingXing = ttk.Label(w3,text="铃星",font=font_style)
                                                diJie = ttk.Label(w6,text="地劫",font=font_style)
                                                dikong = ttk.Label(w3,text="地空",font=font_style)
                                                taiFu = ttk.Label(w11,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w2,text="封诰",font=font_style)
                                            case "巳":
                                                wenChang = ttk.Label(w,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w12,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w2,text="火星",font=font_style)
                                                lingXing = ttk.Label(w4,text="铃星",font=font_style)
                                                diJie = ttk.Label(w5,text="地劫",font=font_style)
                                                dikong = ttk.Label(w2,text="地空",font=font_style)
                                                taiFu = ttk.Label(w10,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w3,text="封诰",font=font_style)
                                            case "午":
                                                wenChang = ttk.Label(w5,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w11,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w3,text="火星",font=font_style)
                                                lingXing = ttk.Label(w12,text="铃星",font=font_style)
                                                diJie = ttk.Label(w,text="地劫",font=font_style)
                                                dikong = ttk.Label(w,text="地空",font=font_style)
                                                taiFu = ttk.Label(w9,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w4,text="封诰",font=font_style)
                                            case "未":
                                                wenChang = ttk.Label(w6,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w10,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w4,text="火星",font=font_style)
                                                lingXing = ttk.Label(w11,text="铃星",font=font_style)
                                                diJie = ttk.Label(w2,text="地劫",font=font_style)
                                                dikong = ttk.Label(w5,text="地空",font=font_style)
                                                taiFu = ttk.Label(w8,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w12,text="封诰",font=font_style)
                                            case "申":
                                                wenChang = ttk.Label(w7,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w9,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w12,text="火星",font=font_style)
                                                lingXing = ttk.Label(w10,text="铃星",font=font_style)
                                                diJie = ttk.Label(w3,text="地劫",font=font_style)
                                                dikong = ttk.Label(w6,text="地空",font=font_style)
                                                taiFu = ttk.Label(w7,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w11,text="封诰",font=font_style)
                                            case "酉":
                                                wenChang = ttk.Label(w8,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w8,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w11,text="火星",font=font_style)
                                                lingXing = ttk.Label(w9,text="铃星",font=font_style)
                                                diJie = ttk.Label(w4,text="地劫",font=font_style)
                                                dikong = ttk.Label(w7,text="地空",font=font_style)
                                                taiFu = ttk.Label(w6,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w10,text="封诰",font=font_style)
                                            case "戌":
                                                wenChang = ttk.Label(w9,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w7,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w10,text="火星",font=font_style)
                                                lingXing = ttk.Label(w8,text="铃星",font=font_style)
                                                diJie = ttk.Label(w12,text="地劫",font=font_style)
                                                dikong = ttk.Label(w8,text="地空",font=font_style)
                                                taiFu = ttk.Label(w5,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w9,text="封诰",font=font_style)
                                            case "亥":
                                                wenChang = ttk.Label(w10,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w6,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w9,text="火星",font=font_style)
                                                lingXing = ttk.Label(w7,text="铃星",font=font_style)
                                                diJie = ttk.Label(w11,text="地劫",font=font_style)
                                                dikong = ttk.Label(w9,text="地空",font=font_style)
                                                taiFu = ttk.Label(w,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w8,text="封诰",font=font_style)       
                                    case "辰"|"子"|"申":
                                        match shiChen:
                                            case "子":
                                                wenChang = ttk.Label(w11,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w5,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w7,text="火星",font=font_style)
                                                lingXing = ttk.Label(w11,text="铃星",font=font_style)
                                                diJie = ttk.Label(w10,text="地劫",font=font_style)
                                                dikong = ttk.Label(w10,text="地空",font=font_style)
                                                taiFu = ttk.Label(w2,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w7,text="封诰",font=font_style)
                                            case "丑":
                                                wenChang = ttk.Label(w12,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w6,text="火星",font=font_style)
                                                lingXing = ttk.Label(w10,text="铃星",font=font_style)
                                                diJie = ttk.Label(w9,text="地劫",font=font_style)
                                                dikong = ttk.Label(w11,text="地空",font=font_style)
                                                taiFu = ttk.Label(w3,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w6,text="封诰",font=font_style)
                                            case "寅":
                                                wenChang = ttk.Label(w4,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w2,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w5,text="火星",font=font_style)
                                                lingXing = ttk.Label(w9,text="铃星",font=font_style)
                                                diJie = ttk.Label(w8,text="地劫",font=font_style)
                                                dikong = ttk.Label(w12,text="地空",font=font_style)
                                                taiFu = ttk.Label(w4,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w5,text="封诰",font=font_style)
                                            case "卯":
                                                wenChang = ttk.Label(w3,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w3,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w,text="火星",font=font_style)
                                                lingXing = ttk.Label(w8,text="铃星",font=font_style)
                                                diJie = ttk.Label(w7,text="地劫",font=font_style)
                                                dikong = ttk.Label(w4,text="地空",font=font_style)
                                                taiFu = ttk.Label(w12,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w,text="封诰",font=font_style)
                                            case "辰":
                                                wenChang = ttk.Label(w2,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w4,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w2,text="火星",font=font_style)
                                                lingXing = ttk.Label(w7,text="铃星",font=font_style)
                                                diJie = ttk.Label(w6,text="地劫",font=font_style)
                                                dikong = ttk.Label(w3,text="地空",font=font_style)
                                                taiFu = ttk.Label(w11,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w2,text="封诰",font=font_style)
                                            case "巳":
                                                wenChang = ttk.Label(w,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w12,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w3,text="火星",font=font_style)
                                                lingXing = ttk.Label(w6,text="铃星",font=font_style)
                                                diJie = ttk.Label(w5,text="地劫",font=font_style)
                                                dikong = ttk.Label(w2,text="地空",font=font_style)
                                                taiFu = ttk.Label(w10,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w3,text="封诰",font=font_style)
                                            case "午":
                                                wenChang = ttk.Label(w5,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w11,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w4,text="火星",font=font_style)
                                                lingXing = ttk.Label(w5,text="铃星",font=font_style)
                                                diJie = ttk.Label(w,text="地劫",font=font_style)
                                                dikong = ttk.Label(w,text="地空",font=font_style)
                                                taiFu = ttk.Label(w9,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w4,text="封诰",font=font_style)
                                            case "未":
                                                wenChang = ttk.Label(w6,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w10,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w12,text="火星",font=font_style)
                                                lingXing = ttk.Label(w,text="铃星",font=font_style)
                                                diJie = ttk.Label(w2,text="地劫",font=font_style)
                                                dikong = ttk.Label(w5,text="地空",font=font_style)
                                                taiFu = ttk.Label(w8,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w12,text="封诰",font=font_style)
                                            case "申":
                                                wenChang = ttk.Label(w7,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w9,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w11,text="火星",font=font_style)
                                                lingXing = ttk.Label(w2,text="铃星",font=font_style)
                                                diJie = ttk.Label(w3,text="地劫",font=font_style)
                                                dikong = ttk.Label(w6,text="地空",font=font_style)
                                                taiFu = ttk.Label(w7,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w11,text="封诰",font=font_style)
                                            case "酉":
                                                wenChang = ttk.Label(w8,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w8,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w10,text="火星",font=font_style)
                                                lingXing = ttk.Label(w3,text="铃星",font=font_style)
                                                diJie = ttk.Label(w4,text="地劫",font=font_style)
                                                dikong = ttk.Label(w7,text="地空",font=font_style)
                                                taiFu = ttk.Label(w6,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w10,text="封诰",font=font_style)
                                            case "戌":
                                                wenChang = ttk.Label(w9,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w7,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w9,text="火星",font=font_style)
                                                lingXing = ttk.Label(w4,text="铃星",font=font_style)
                                                diJie = ttk.Label(w12,text="地劫",font=font_style)
                                                dikong = ttk.Label(w8,text="地空",font=font_style)
                                                taiFu = ttk.Label(w5,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w9,text="封诰",font=font_style)
                                            case "亥":
                                                wenChang = ttk.Label(w10,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w6,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w8,text="火星",font=font_style)
                                                lingXing = ttk.Label(w12,text="铃星",font=font_style)
                                                diJie = ttk.Label(w11,text="地劫",font=font_style)
                                                dikong = ttk.Label(w9,text="地空",font=font_style)
                                                taiFu = ttk.Label(w,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w8,text="封诰",font=font_style)
                                    case "丑"|"酉"|"巳":
                                        match shiChen:
                                            case "子":
                                                wenChang = ttk.Label(w11,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w5,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w6,text="火星",font=font_style)
                                                lingXing = ttk.Label(w11,text="铃星",font=font_style)
                                                diJie = ttk.Label(w10,text="地劫",font=font_style)
                                                dikong = ttk.Label(w10,text="地空",font=font_style)
                                                taiFu = ttk.Label(w2,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w7,text="封诰",font=font_style)
                                            case "丑":
                                                wenChang = ttk.Label(w12,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w5,text="火星",font=font_style)
                                                lingXing = ttk.Label(w10,text="铃星",font=font_style)
                                                diJie = ttk.Label(w9,text="地劫",font=font_style)
                                                dikong = ttk.Label(w11,text="地空",font=font_style)
                                                taiFu = ttk.Label(w3,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w6,text="封诰",font=font_style)
                                            case "寅":
                                                wenChang = ttk.Label(w4,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w2,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w,text="火星",font=font_style)
                                                lingXing = ttk.Label(w9,text="铃星",font=font_style)
                                                diJie = ttk.Label(w8,text="地劫",font=font_style)
                                                dikong = ttk.Label(w12,text="地空",font=font_style)
                                                taiFu = ttk.Label(w4,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w5,text="封诰",font=font_style)
                                            case "卯":
                                                wenChang = ttk.Label(w3,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w3,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w2,text="火星",font=font_style)
                                                lingXing = ttk.Label(w8,text="铃星",font=font_style)
                                                diJie = ttk.Label(w7,text="地劫",font=font_style)
                                                dikong = ttk.Label(w4,text="地空",font=font_style)
                                                taiFu = ttk.Label(w12,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w,text="封诰",font=font_style)
                                            case "辰":
                                                wenChang = ttk.Label(w2,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w4,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w3,text="火星",font=font_style)
                                                lingXing = ttk.Label(w7,text="铃星",font=font_style)
                                                diJie = ttk.Label(w6,text="地劫",font=font_style)
                                                dikong = ttk.Label(w3,text="地空",font=font_style)
                                                taiFu = ttk.Label(w11,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w2,text="封诰",font=font_style)
                                            case "巳":
                                                wenChang = ttk.Label(w,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w12,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w4,text="火星",font=font_style)
                                                lingXing = ttk.Label(w6,text="铃星",font=font_style)
                                                diJie = ttk.Label(w5,text="地劫",font=font_style)
                                                dikong = ttk.Label(w2,text="地空",font=font_style)
                                                taiFu = ttk.Label(w10,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w3,text="封诰",font=font_style)
                                            case "午":
                                                wenChang = ttk.Label(w5,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w11,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w12,text="火星",font=font_style)
                                                lingXing = ttk.Label(w5,text="铃星",font=font_style)
                                                diJie = ttk.Label(w,text="地劫",font=font_style)
                                                dikong = ttk.Label(w,text="地空",font=font_style)
                                                taiFu = ttk.Label(w9,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w4,text="封诰",font=font_style)
                                            case "未":
                                                wenChang = ttk.Label(w6,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w10,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w11,text="火星",font=font_style)
                                                lingXing = ttk.Label(w,text="铃星",font=font_style)
                                                diJie = ttk.Label(w2,text="地劫",font=font_style)
                                                dikong = ttk.Label(w5,text="地空",font=font_style)
                                                taiFu = ttk.Label(w8,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w12,text="封诰",font=font_style)
                                            case "申":
                                                wenChang = ttk.Label(w7,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w9,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w10,text="火星",font=font_style)
                                                lingXing = ttk.Label(w2,text="铃星",font=font_style)
                                                diJie = ttk.Label(w3,text="地劫",font=font_style)
                                                dikong = ttk.Label(w6,text="地空",font=font_style)
                                                taiFu = ttk.Label(w7,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w11,text="封诰",font=font_style)
                                            case "酉":
                                                wenChang = ttk.Label(w8,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w8,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w9,text="火星",font=font_style)
                                                lingXing = ttk.Label(w3,text="铃星",font=font_style)
                                                diJie = ttk.Label(w4,text="地劫",font=font_style)
                                                dikong = ttk.Label(w7,text="地空",font=font_style)
                                                taiFu = ttk.Label(w6,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w10,text="封诰",font=font_style)
                                            case "戌":
                                                wenChang = ttk.Label(w9,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w7,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w8,text="火星",font=font_style)
                                                lingXing = ttk.Label(w4,text="铃星",font=font_style)
                                                diJie = ttk.Label(w12,text="地劫",font=font_style)
                                                dikong = ttk.Label(w8,text="地空",font=font_style)
                                                taiFu = ttk.Label(w5,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w9,text="封诰",font=font_style)
                                            case "亥":
                                                wenChang = ttk.Label(w10,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w6,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w7,text="火星",font=font_style)
                                                lingXing = ttk.Label(w12,text="铃星",font=font_style)
                                                diJie = ttk.Label(w11,text="地劫",font=font_style)
                                                dikong = ttk.Label(w9,text="地空",font=font_style)
                                                taiFu = ttk.Label(w,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w8,text="封诰",font=font_style)
                                    case "未"|"卯"|"亥":
                                        match shiChen:
                                            case "子":
                                                wenChang = ttk.Label(w11,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w5,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w12,text="火星",font=font_style)
                                                lingXing = ttk.Label(w11,text="铃星",font=font_style)
                                                diJie = ttk.Label(w10,text="地劫",font=font_style)
                                                dikong = ttk.Label(w10,text="地空",font=font_style)
                                                taiFu = ttk.Label(w2,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w7,text="封诰",font=font_style)
                                            case "丑":
                                                wenChang = ttk.Label(w12,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w11,text="火星",font=font_style)
                                                lingXing = ttk.Label(w10,text="铃星",font=font_style)
                                                diJie = ttk.Label(w9,text="地劫",font=font_style)
                                                dikong = ttk.Label(w11,text="地空",font=font_style)
                                                taiFu = ttk.Label(w3,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w6,text="封诰",font=font_style)
                                            case "寅":
                                                wenChang = ttk.Label(w4,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w2,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w10,text="火星",font=font_style)
                                                lingXing = ttk.Label(w9,text="铃星",font=font_style)
                                                diJie = ttk.Label(w8,text="地劫",font=font_style)
                                                dikong = ttk.Label(w12,text="地空",font=font_style)
                                                taiFu = ttk.Label(w4,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w5,text="封诰",font=font_style)
                                            case "卯":
                                                wenChang = ttk.Label(w3,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w3,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w9,text="火星",font=font_style)
                                                lingXing = ttk.Label(w8,text="铃星",font=font_style)
                                                diJie = ttk.Label(w7,text="地劫",font=font_style)
                                                dikong = ttk.Label(w4,text="地空",font=font_style)
                                                taiFu = ttk.Label(w12,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w,text="封诰",font=font_style)
                                            case "辰":
                                                wenChang = ttk.Label(w2,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w4,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w8,text="火星",font=font_style)
                                                lingXing = ttk.Label(w7,text="铃星",font=font_style)
                                                diJie = ttk.Label(w6,text="地劫",font=font_style)
                                                dikong = ttk.Label(w3,text="地空",font=font_style)
                                                taiFu = ttk.Label(w11,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w2,text="封诰",font=font_style)
                                            case "巳":
                                                wenChang = ttk.Label(w,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w12,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w7,text="火星",font=font_style)
                                                lingXing = ttk.Label(w6,text="铃星",font=font_style)
                                                diJie = ttk.Label(w5,text="地劫",font=font_style)
                                                dikong = ttk.Label(w2,text="地空",font=font_style)
                                                taiFu = ttk.Label(w10,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w3,text="封诰",font=font_style)
                                            case "午":
                                                wenChang = ttk.Label(w5,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w11,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w6,text="火星",font=font_style)
                                                lingXing = ttk.Label(w5,text="铃星",font=font_style)
                                                diJie = ttk.Label(w,text="地劫",font=font_style)
                                                dikong = ttk.Label(w,text="地空",font=font_style)
                                                taiFu = ttk.Label(w9,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w4,text="封诰",font=font_style)
                                            case "未":
                                                wenChang = ttk.Label(w6,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w10,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w5,text="火星",font=font_style)
                                                lingXing = ttk.Label(w,text="铃星",font=font_style)
                                                diJie = ttk.Label(w2,text="地劫",font=font_style)
                                                dikong = ttk.Label(w5,text="地空",font=font_style)
                                                taiFu = ttk.Label(w8,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w12,text="封诰",font=font_style)
                                            case "申":
                                                wenChang = ttk.Label(w7,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w9,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w,text="火星",font=font_style)
                                                lingXing = ttk.Label(w2,text="铃星",font=font_style)
                                                diJie = ttk.Label(w3,text="地劫",font=font_style)
                                                dikong = ttk.Label(w6,text="地空",font=font_style)
                                                taiFu = ttk.Label(w7,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w11,text="封诰",font=font_style)
                                            case "酉":
                                                wenChang = ttk.Label(w8,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w8,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w2,text="火星",font=font_style)
                                                lingXing = ttk.Label(w3,text="铃星",font=font_style)
                                                diJie = ttk.Label(w4,text="地劫",font=font_style)
                                                dikong = ttk.Label(w7,text="地空",font=font_style)
                                                taiFu = ttk.Label(w6,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w10,text="封诰",font=font_style)
                                            case "戌":
                                                wenChang = ttk.Label(w9,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w7,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w3,text="火星",font=font_style)
                                                lingXing = ttk.Label(w4,text="铃星",font=font_style)
                                                diJie = ttk.Label(w12,text="地劫",font=font_style)
                                                dikong = ttk.Label(w8,text="地空",font=font_style)
                                                taiFu = ttk.Label(w5,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w9,text="封诰",font=font_style)
                                            case "亥":
                                                wenChang = ttk.Label(w10,text="文昌",font=font_style)
                                                wenQu = ttk.Label(w6,text="文曲",font=font_style)
                                                huoXing = ttk.Label(w4,text="火星",font=font_style)
                                                lingXing = ttk.Label(w12,text="铃星",font=font_style)
                                                diJie = ttk.Label(w11,text="地劫",font=font_style)
                                                dikong = ttk.Label(w9,text="地空",font=font_style)
                                                taiFu = ttk.Label(w,text="台辅",font=font_style)
                                                fengGao = ttk.Label(w8,text="封诰",font=font_style)
                                match yueZhi:
                                    case "寅":
                                        zuofu_num = 5
                                        youbi_num = 11
                                        zuofu = ttk.Label(w5,text="左辅",font=font_style)
                                        youbi = ttk.Label(w11,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w12,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w8,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w11,text="天月",font=font_style)
                                        tiansha = ttk.Label(w7,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w11,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w5,text="左辅【科】",font=font_style)
                                    case "卯":
                                        zuofu_num = 6
                                        youbi_num = 10
                                        zuofu = ttk.Label(w,text="左辅",font=font_style)
                                        youbi = ttk.Label(w12,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w11,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w7,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w4,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w11,text="天月",font=font_style)
                                        tiansha = ttk.Label(w9,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w12,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w,text="左辅【科】",font=font_style)
                                    case "辰":
                                        zuofu_num = 7
                                        youbi_num = 9
                                        zuofu = ttk.Label(w2,text="左辅",font=font_style)
                                        youbi = ttk.Label(w4,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w10,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w6,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w7,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w5,text="天月",font=font_style)
                                        tiansha = ttk.Label(w11,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w4,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w2,text="左辅【科】",font=font_style)
                                    case "巳":
                                        zuofu_num = 8
                                        youbi_num = 8
                                        zuofu = ttk.Label(w3,text="左辅",font=font_style)
                                        youbi = ttk.Label(w3,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w9,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w5,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w10,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w7,text="天月",font=font_style)
                                        tiansha = ttk.Label(w4,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w3,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w3,text="左辅【科】",font=font_style)
                                    case "午":
                                        zuofu_num = 9
                                        youbi_num = 7
                                        zuofu = ttk.Label(w4,text="左辅",font=font_style)
                                        youbi = ttk.Label(w2,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w8,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w3,text="天月",font=font_style)
                                        tiansha = ttk.Label(w2,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w2,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w4,text="左辅【科】",font=font_style)
                                    case "未":
                                        zuofu_num = 10
                                        youbi_num = 6
                                        zuofu = ttk.Label(w12,text="左辅",font=font_style)
                                        youbi = ttk.Label(w,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w7,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w2,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w4,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w6,text="天月",font=font_style)
                                        tiansha = ttk.Label(w5,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w12,text="左辅【科】",font=font_style)
                                    case "申":
                                        zuofu_num = 11
                                        youbi_num = 5
                                        zuofu = ttk.Label(w11,text="左辅",font=font_style)
                                        youbi = ttk.Label(w5,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w6,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w3,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w7,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w10,text="天月",font=font_style)
                                        tiansha = ttk.Label(w7,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w5,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w11,text="左辅【科】",font=font_style)
                                    case "酉":
                                        zuofu_num = 12
                                        youbi_num = 4
                                        zuofu = ttk.Label(w10,text="左辅",font=font_style)
                                        youbi = ttk.Label(w6,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w5,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w4,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w10,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w3,text="天月",font=font_style)
                                        tiansha = ttk.Label(w9,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w6,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w10,text="左辅【科】",font=font_style)
                                    case "戌":
                                        zuofu_num = 1
                                        youbi_num = 3
                                        zuofu = ttk.Label(w9,text="左辅",font=font_style)
                                        youbi = ttk.Label(w7,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w12,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w7,text="天月",font=font_style)
                                        tiansha = ttk.Label(w11,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w7,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w9,text="左辅【科】",font=font_style)
                                    case "亥":
                                        zuofu_num = 2
                                        youbi_num = 2
                                        zuofu = ttk.Label(w8,text="左辅",font=font_style)
                                        youbi = ttk.Label(w8,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w2,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w11,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w4,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w2,text="天月",font=font_style)
                                        tiansha = ttk.Label(w4,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w8,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w8,text="左辅【科】",font=font_style)
                                    case "子":
                                        zuofu_num = 3
                                        youbi_num = 1
                                        zuofu = ttk.Label(w7,text="左辅",font=font_style)
                                        youbi = ttk.Label(w9,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w3,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w10,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w7,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w11,text="天月",font=font_style)
                                        tiansha = ttk.Label(w2,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w9,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w7,text="左辅【科】",font=font_style)
                                    case "丑":
                                        zuofu_num = 4
                                        youbi_num = 12
                                        zuofu = ttk.Label(w6,text="左辅",font=font_style)
                                        youbi = ttk.Label(w10,text="右弼",font=font_style)
                                        tianxing = ttk.Label(w4,text="天刑",font=font_style)
                                        tianyao = ttk.Label(w9,text="天姚",font=font_style)
                                        tianwu = ttk.Label(w10,text="天巫",font=font_style)
                                        tianyue = ttk.Label(w7,text="天月",font=font_style)
                                        tiansha = ttk.Label(w5,text="阴煞",font=font_style)
                                        if nianGan == "戊":
                                            youbi = ttk.Label(w10,text="右弼【科】",font=font_style)
                                        if nianGan == "壬":
                                            zuofu = ttk.Label(w6,text="左辅【科】",font=font_style)
                                match shiChen:
                                    case "子":
                                        wenchang_num = 11
                                        wenqu_num = 5
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w11,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w11,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w5,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w5,text="文曲【忌】",font=font_style)
                                    case "丑":
                                        wenchang_num = 10
                                        wenqu_num = 6
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w12,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w12,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w,text="文曲【忌】",font=font_style)
                                    case "寅":
                                        wenchang_num = 9
                                        wenqu_num = 7
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w4,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w4,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w2,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w2,text="文曲【忌】",font=font_style)
                                    case "卯":
                                        wenchang_num = 8
                                        wenqu_num = 8
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w3,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w3,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w3,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w3,text="文曲【忌】",font=font_style)
                                    case "辰":
                                        wenchang_num = 7
                                        wenqu_num = 9
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w2,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w2,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w4,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w4,text="文曲【忌】",font=font_style)
                                    case "巳":
                                        wenchang_num = 6
                                        wenqu_num = 10
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w12,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w12,text="文曲【忌】",font=font_style)
                                    case "午":
                                        wenchang_num = 5
                                        wenqu_num = 11
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w5,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w5,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w11,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w11,text="文曲【忌】",font=font_style)
                                    case "未":
                                        wenchang_num = 4
                                        wenqu_num = 12
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w6,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w6,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w10,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w10,text="文曲【忌】",font=font_style)
                                    case "申":
                                        wenchang_num = 3
                                        wenqu_num = 1
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w7,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w7,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w9,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w9,text="文曲【忌】",font=font_style)
                                    case "酉":
                                        wenchang_num = 2
                                        wenqu_num = 2
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w8,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w8,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w8,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w8,text="文曲【忌】",font=font_style)
                                    case "戌":
                                        wenchang_num = 1
                                        wenqu_num = 3
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w9,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w9,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w7,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w7,text="文曲【忌】",font=font_style)
                                    case "亥":
                                        wenchang_num = 12
                                        wenqu_num = 4
                                        if nianGan == "丙":
                                            wenChang = ttk.Label(w10,text="文昌【科】",font=font_style)
                                        elif nianGan == "辛":
                                            wenChang = ttk.Label(w10,text="文昌【忌】",font=font_style)
                                            wenQu = ttk.Label(w6,text="文曲【科】",font=font_style)
                                        elif nianGan == "己":
                                            wenQu = ttk.Label(w6,text="文曲【忌】",font=font_style)

                                zuofu_num = (zuofu_num - 1 + day)%12
                                youbi_num = ((youbi_num - 1 - day) % 12 + 2)%12
                                wenchang_num = ((wenchang_num - 1 - day)%12 + 1)%12
                                wenqu_num = ((wenqu_num - 1 - day) % 12 + 1)%12

                                match zuofu_num:
                                    case 1:
                                        santai = ttk.Label(w9,text="三台",font=font_style)
                                    case 2:
                                        santai = ttk.Label(w8,text="三台",font=font_style)
                                    case 3:
                                        santai = ttk.Label(w7,text="三台",font=font_style)
                                    case 4:
                                        santai = ttk.Label(w6,text="三台",font=font_style)
                                    case 5:
                                        santai = ttk.Label(w5,text="三台",font=font_style)
                                    case 6:
                                        santai = ttk.Label(w,text="三台",font=font_style)
                                    case 7:
                                        santai = ttk.Label(w2,text="三台",font=font_style)
                                    case 8:
                                        santai = ttk.Label(w3,text="三台",font=font_style)
                                    case 9:
                                        santai = ttk.Label(w4,text="三台",font=font_style)
                                    case 10:
                                        santai = ttk.Label(w12,text="三台",font=font_style)
                                    case 11:
                                        santai = ttk.Label(w11,text="三台",font=font_style)
                                    case 0:
                                        santai = ttk.Label(w10,text="三台",font=font_style)
                                
                                match youbi_num:
                                    case 1:
                                        bazuo = ttk.Label(w9,text="八座",font=font_style)
                                    case 2:
                                        bazuo = ttk.Label(w8,text="八座",font=font_style)
                                    case 3:
                                        bazuo = ttk.Label(w7,text="八座",font=font_style)
                                    case 4:
                                        bazuo = ttk.Label(w6,text="八座",font=font_style)
                                    case 5:
                                        bazuo = ttk.Label(w5,text="八座",font=font_style)
                                    case 6:
                                        bazuo = ttk.Label(w,text="八座",font=font_style)
                                    case 7:
                                        bazuo = ttk.Label(w2,text="八座",font=font_style)
                                    case 8:
                                        bazuo = ttk.Label(w3,text="八座",font=font_style)
                                    case 9:
                                        bazuo = ttk.Label(w4,text="八座",font=font_style)
                                    case 10:
                                        bazuo = ttk.Label(w12,text="八座",font=font_style)
                                    case 11:
                                        bazuo = ttk.Label(w11,text="八座",font=font_style)
                                    case 0:
                                        bazuo = ttk.Label(w10,text="八座",font=font_style)

                                match wenchang_num:
                                    case 1:
                                        enguang = ttk.Label(w9,text="恩光",font=font_style)
                                    case 2:
                                        enguang = ttk.Label(w8,text="恩光",font=font_style)
                                    case 3:
                                        enguang = ttk.Label(w7,text="恩光",font=font_style)
                                    case 4:
                                        enguang = ttk.Label(w6,text="恩光",font=font_style)
                                    case 5:
                                        enguang = ttk.Label(w5,text="恩光",font=font_style)
                                    case 6:
                                        enguang = ttk.Label(w,text="恩光",font=font_style)
                                    case 7:
                                        enguang = ttk.Label(w2,text="恩光",font=font_style)
                                    case 8:
                                        enguang = ttk.Label(w3,text="恩光",font=font_style)
                                    case 9:
                                        enguang = ttk.Label(w4,text="恩光",font=font_style)
                                    case 10:
                                        enguang = ttk.Label(w12,text="恩光",font=font_style)
                                    case 11:
                                        enguang = ttk.Label(w11,text="恩光",font=font_style)
                                    case 0:
                                        enguang = ttk.Label(w10,text="恩光",font=font_style)

                                match wenqu_num:
                                    case 1:
                                        tiangui = ttk.Label(w9,text="天贵",font=font_style)
                                    case 2:
                                        tiangui = ttk.Label(w8,text="天贵",font=font_style)
                                    case 3:
                                        tiangui = ttk.Label(w7,text="天贵",font=font_style)
                                    case 4:
                                        tiangui = ttk.Label(w6,text="天贵",font=font_style)
                                    case 5:
                                        tiangui = ttk.Label(w5,text="天贵",font=font_style)
                                    case 6:
                                        tiangui = ttk.Label(w,text="天贵",font=font_style)
                                    case 7:
                                        tiangui = ttk.Label(w2,text="天贵",font=font_style)
                                    case 8:
                                        tiangui = ttk.Label(w3,text="天贵",font=font_style)
                                    case 9:
                                        tiangui = ttk.Label(w4,text="天贵",font=font_style)
                                    case 10:
                                        tiangui = ttk.Label(w12,text="天贵",font=font_style)
                                    case 11:
                                        tiangui = ttk.Label(w11,text="天贵",font=font_style)
                                    case 0:
                                        tiangui = ttk.Label(w10,text="天贵",font=font_style)
                                


                                
                                def grid_deploy():
                                    wenChang.grid(row=8,column=2)
                                    wenQu.grid(row=8,column=3)
                                    huoXing.grid(row=8,column=4)
                                    lingXing.grid(row=8,column=5)
                                    zuofu.grid(row=8,column=6)
                                    youbi.grid(row=8,column=7)
                                    
                                    diJie.grid(row=7,column=0)
                                    dikong.grid(row=7,column=1)
                                    taiFu.grid(row=7,column=2)
                                    fengGao.grid(row=7,column=3)
                                    tianxing.grid(row=7,column=4)
                                    tianyao.grid(row=7,column=5)
                                    tianwu.grid(row=7,column=6)
                                    tianyue.grid(row=7,column=7)
                                    tiansha.grid(row=7,column=8)
                                    santai.grid(row=7,column=9)
                                    bazuo.grid(row=7,column=10)
                                    enguang.grid(row=7,column=11)
                                    tiangui.grid(row=7,column=12)
                                
                                grid_deploy()

                            Heavenly()
                            twelve_god()
                            person()
                            confirm_ziWei_and_ziWei_five()
                            confirm_ziWei_time_and_month_and_day_group()
                            
                            window_z.grid_rowconfigure(1, weight=1)
                            window_z.grid_columnconfigure(1, weight=1)
                        z_t()
                        '''
                            [ w  巳 ][ w2 午 ][ w3 未 ][ w4 申 ]
                            [ w5 辰 ][ w13][     ][ w12  酉 ]
                            [ w6 卯 ][     ][     ][ w11 戌]
                            [ w7 寅 ][ w8 丑 ][ w9 子 ][ w10  亥]
                        '''


        match t:
            case "横排样式":
                window = ttk.Toplevel(root)
                window.title("紫微斗数")
                window.iconbitmap(icon_path)
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
                combobox = ttk.Combobox(master=window, values=["男","女","其它"])
                combobox.grid(row=0, column=9,padx=10,pady=10)
                entry1.focus_set()
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry3.focus_set())
                entry3.bind("<Return>", lambda event: entry4.focus_set())
                entry4.bind("<Return>", lambda event: combobox.focus_set())
                combobox.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_R>', lambda event: z_judge())
                entry2.bind('<Shift_R>', lambda event: z_judge())
                entry3.bind('<Shift_R>', lambda event: z_judge())
                entry4.bind('<Shift_R>', lambda event: z_judge())
                combobox.bind('<Shift_R>', lambda event: z_judge())
                '''
                values = ["算一卦"]
                combo = ttk.Combobox(window, values=values, state="readonly")
                combo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
                combo.bind("<Button-3>", ())
                combo.set("算一卦")
                '''
            case "竖排样式":
                window = ttk.Toplevel(root)
                window.title("紫微斗数")
                window.iconbitmap(icon_path)
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
                combobox = ttk.Combobox(master=window, values=["男","女","其它"])
                combobox.grid(row=4, column=1,padx=10,pady=10)
                entry1.focus_set()
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry3.focus_set())
                entry3.bind("<Return>", lambda event: entry4.focus_set())
                entry4.bind("<Return>", lambda event: combobox.focus_set())
                combobox.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_R>', lambda event: z_judge())
                entry2.bind('<Shift_R>', lambda event: z_judge())
                entry3.bind('<Shift_R>', lambda event: z_judge())
                entry4.bind('<Shift_R>', lambda event: z_judge())
                combobox.bind('<Shift_R>', lambda event: z_judge())


    def regression():
        window_ = ttk.Toplevel(window)
        window_.title("小六壬")
        window_.iconbitmap(icon_path)
        wb1 = ttk.Button(window_, text="数据导入", bootstyle="outline", command=x)
        wb1.grid(column=0,row=0,padx=10,pady=10)
        data_path = filedialog.asksaveasfilename(parent=window_, defaultextension="d",
                                                 filetypes=[("csv-utf-8", "*.csv")])
        print(data_path)
    
    def Triangle():
        pass
    
    def Sprites():
        def color():

            rgb = None
            rgb_ = None
            
            def root_w_4_3_load():
                try:
                    with open(w_path, 'r',encoding='utf-8') as f:
                        return f.read()
                except FileNotFoundError:
                    pass
            
            def root_w_4_3_load_2():
                try:
                    with open(x_path, 'r',encoding='utf-8') as f:
                        return f.read()
                except FileNotFoundError:
                    pass
            
            def choose_color():
                nonlocal rgb
                color = colorchooser.askcolor(parent=window__)
                rgb = color[0]

            def choose_color_():
                nonlocal rgb_
                color = colorchooser.askcolor(parent=window__)
                rgb_ = color[0]
            
            def color_RGB():
                if rgb is None or rgb_ is None:
                    messagebox.showerror("错误", message="没有值", parent=window__)
                if not PNG_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                else:
                    try:
                        icon.notify("已开始", "Lightweight text editor")
                        for path in PNG_path:
                            img = Image.open(path).convert("RGB")
                            datas = np.array(img)

                            # 创建掩码，确定需要转换的颜色
                            mask = np.all(datas == rgb, axis=-1)

                            # 执行颜色转换
                            datas[mask] = rgb_

                            # 保存处理后的图像
                            img = Image.fromarray(datas, 'RGB')
                            img.save(path, "PNG")
                        icon.notify("已完成", "Lightweight text editor")
                    except Exception as e:
                        messagebox.showerror("错误", message=f"处理图像时出错: {e}", parent=window__)


            def color_RGBA():
                if re.sub(r"保留原本|(?<!\d)(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?!\d)", "", entry1.get()) != "":
                    messagebox.showerror("错误", message="请输入0~255的值，或输入保留原本", parent=window__)
                else:
                    if re.sub(r"(?<!\d)(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(?!\d)", "", entry2.get()) != "":
                        messagebox.showerror("错误", message="请输入0~255的值", parent=window__)
                    else:
                        if rgb is None or rgb_ is None:
                            messagebox.showerror("错误", message="没有值", parent=window__)
                        if not PNG_path:
                            messagebox.showerror("错误", message="没有路径", parent=window__)
                        else:
                            if entry1.get() == "保留原本" and entry2.get() == "255":
                                pass
                            for _ in PNG_path:#获取路径
                                img = Image.open(_).convert("RGBA")
                                datas = img.getdata()
                                new_data = []
                                for item in datas:
                                    # 颜色转换
                                    if item[0] == rgb[0] and item[1] == rgb[1] and item[2] == rgb[2]:
                                        new_data.append((rgb_[0], rgb_[1], rgb_[2], item[3]))
                                    else:
                                        new_data.append(item)
                                img.putdata(new_data)
                                img.save(PNG_path, "PNG")
    

            PNG_path = filedialog.askopenfilenames(title='请选择需要颜色转换的图片',filetypes=[("PNG", "*.PNG")])

            window__ = ttk.Toplevel(window_)
            window__.title("图片操作")
            window__.iconbitmap(icon_path)

            t = str(root_w_4_3_load() or "颜色选择器")
            t_ = str(root_w_4_3_load_2() or "RBGA")

            match t:
                case "颜色选择器":
                    wb1_ = ttk.Button(window__, text="颜色选择器", bootstyle="outline", command=choose_color)
                    wb1_.grid(column=1,row=0,padx=10,pady=10)
                    wb2_ = ttk.Button(window__, text="颜色选择器", bootstyle="outline", command=choose_color_)
                    wb2_.grid(column=1,row=1,padx=10,pady=10)
                    match t_:
                        case "RGBA":
                            text3 = ttk.Label(window__,text="整张透明度：")
                            text3.grid(column=0,row=2,padx=10,pady=10)
                            entry1 = tk.Entry(window__)
                            entry1.grid(column=1,row=2,padx=5,pady=5)
                            entry1.insert(tk.END,"保留原本")
                            text4 = ttk.Label(window__,text="转换颜色透明度：")
                            text4.grid(column=0,row=3,padx=10,pady=10)
                            entry2 = tk.Entry(window__)
                            entry2.grid(column=1,row=3,padx=5,pady=5)
                            entry2.insert(tk.END,"255")
                            entry1.bind("<Return>", lambda event: entry2.focus_set())
                            entry2.bind("<Return>", lambda event: entry1.focus_set())
                            entry1.bind('<Shift_L>', lambda event: ())
                            entry2.bind('<Shift_L>', lambda event: ())
                        case "RGB":
                            wb1_.bind("<Button-3>", lambda event: color_RGB())
                            wb2_.bind("<Button-3>", lambda event: color_RGB())
                
                case "十六进制":
                    entry1_1 = tk.Entry(window__)
                    entry1_1.grid(column=1,row=0,padx=5,pady=5)
                    entry2_1 = tk.Entry(window__)
                    entry2_1.grid(column=1,row=1,padx=5,pady=5)
                    entry1_1.bind("<Return>", lambda event: entry2_1.focus_set())
                    entry2_1.bind("<Return>", lambda event: entry1_1.focus_set())
                case "RGB值":
                    entry1_2 = tk.Entry(window__)
                    entry1_2.grid(column=1,row=0,padx=5,pady=5)
                    entry2_2 = tk.Entry(window__)
                    entry2_2.grid(column=1,row=1,padx=5,pady=5)
                    entry1_2.bind("<Return>", lambda event: entry2_2.focus_set())
                    entry2_2.bind("<Return>", lambda event: entry1_2.focus_set())

            text = ttk.Label(window__,text="需要转换的颜色：")
            text.grid(column=0,row=0,padx=10,pady=10)

            text2 = ttk.Label(window__,text="转换成的颜色：")
            text2.grid(column=0,row=1,padx=10,pady=10)
            

            
        window_ = ttk.Toplevel(window)
        window_.title("图片操作")
        window_.iconbitmap(icon_path)
        wb1 = ttk.Button(window_, text="颜色转换", bootstyle="outline", command=color)
        wb1.grid(column=0,row=0,padx=10,pady=10)


    window = ttk.Toplevel(root)
    window.title("轻量记事本-小工具")
    window.iconbitmap(icon_path)
    b1 = ttk.Button(window, text="小六壬", bootstyle="outline", command=x)
    b1.grid(column=0,row=0,padx=10,pady=10)
    b2 = ttk.Button(window, text="紫微斗数", bootstyle="outline", command=z)
    b2.grid(column=1,row=0,padx=10,pady=10)
    b3 = ttk.Button(window, text="机器学习-回归问题", bootstyle="outline", command=regression)
    b3.grid(column=2,row=0,padx=10,pady=10)
    b4 = ttk.Button(window,text="三角形计算", bootstyle="outline", command=Triangle)
    b4.grid(column=3,row=0,padx=10,pady=10)
    b5 = ttk.Button(window,text="图片操作", bootstyle="outline", command=Sprites)
    b5.grid(column=4,row=0,padx=10,pady=10)
###分割线




#关于设置界面###分割线
def root_window():
    child_windows = []

    window = ttk.Toplevel()
    window.resizable(0,0)
    window.title("轻量记事本-设置")
    window.iconbitmap(icon_path)

    def window_close():
        for win in child_windows:
            try:
                win.destroy()
            except:
                pass
        window.destroy()

    def window_close_():
        for win in child_windows:
            try:
                win.destroy()
            except:
                pass

    def w_root1():

        global theme_cbo

        def bao_chun():
            global v2,v3,v4
            p1=v2%2
            p2=v3%2
            p3=v4%2
            window_close_()
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

        window_Button_two = ttk.Button(w_, text="返回", bootstyle="outline", command=window_close)
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

    sep = Separator(window, orient='horizontal')
    sep.grid(column=0, row=1,pady=30,sticky='ew',columnspan=1)

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

    sep2 = Separator(window, orient='horizontal')
    sep2.grid(column=0, row=3,pady=30,sticky='ew',columnspan=1)

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

    sep3 = Separator(window, orient='horizontal')
    sep3.grid(column=0, row=5,pady=30,sticky='ew',columnspan=1)

    def w_root4():

        w_4 = ttk.Frame(window)
        w_4.grid(row=6,column=0,sticky=W)

        w_4_1 = ttk.Frame(w_4)
        w_4_1.grid(column=1,row=1,sticky=W)

        w_4_2 = ttk.Frame(w_4)
        w_4_2.grid(column=1,row=2,sticky=W)

        w_4_3 = ttk.Frame(w_4)
        w_4_3.grid(column=1,row=3,sticky=W)

        lb5 = ttk.Label(w_4, text="小工具设置:")
        lb5.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        lb6 = ttk.Label(w_4, text="小六壬:")
        lb6.grid(column=0,row=1,padx=10,pady=10,ipadx=5)

        lb7 = ttk.Label(w_4, text="紫微斗数:")
        lb7.grid(column=0,row=2,padx=10,pady=10,ipadx=5)

        lb8 = ttk.Label(w_4,text="图片操作:")
        lb8.grid(column=0,row=3,padx=10,pady=10,ipadx=5)

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

        w_4_2_lb1 = ttk.Label(w_4_2,text="界面样式：")
        w_4_2_lb1.grid(column=0,row=0,padx=5,pady=5)

        W_4_2_lb2 = ttk.Label(w_4_2,text="闰月问题：")
        W_4_2_lb2.grid(column=0,row=1,padx=5,pady=5)

        W_4_2_lb3 = ttk.Label(w_4_2,text="时辰问题：")
        W_4_2_lb3.grid(column=0,row=2,padx=5,pady=5)

        w_4_3_lb1 = ttk.Label(w_4_3,text="颜色输入：")
        w_4_3_lb1.grid(column=0,row=0,padx=5,pady=5)

        w_4_3_lb2 = ttk.Label(w_4_3,text="色彩空间：")
        w_4_3_lb2.grid(column=0,row=1,padx=5,pady=5)


        def w_4_3_():

            def down_box_save_1():
                with open(w_path, 'w',encoding='utf-8') as file:
                    file.write(str(down_box.get()))

            def down_box_save_2():
                with open(x_path, 'w',encoding='utf-8') as file:
                    file.write(str(down_box2.get()))
            
            def w_4_3_load():
                try:
                    with open(w_path, 'r',encoding='utf-8') as f:
                        return f.read()
                except FileNotFoundError:
                    pass

            def w_4_3_load_2():
                try:
                    with open(x_path, 'r',encoding='utf-8') as f:
                        return f.read()
                except FileNotFoundError:
                    pass



            down_box = ttk.Combobox(w_4_3, values=["颜色选择器","十六进制","RGB值"], state="readonly")
            down_box.grid(row=0, column=1, padx=5, pady=5)
            down_box.bind("<<ComboboxSelected>>", lambda event: down_box_save_1())
            t = str(w_4_3_load() or "颜色选择器")
            match t:
                case "颜色选择器":
                    down_box.set("颜色选择器")
                case "十六进制":
                    down_box.set("十六进制")
                case "RGB值":
                    down_box.set("RGB值")

            down_box2 = ttk.Combobox(w_4_3, values=["RGBA","RGB"], state="readonly")
            down_box2.grid(row=1, column=1, padx=5, pady=5)
            down_box2.bind("<<ComboboxSelected>>", lambda event: down_box_save_2())
            t_ = str(w_4_3_load_2() or "RGBA")
            match t_:
                case "RGBA":
                    down_box2.set("RBGA")
                case "RGB":
                    down_box2.set("RGB")

        def w_4_2_():

            def event_t():
                with open(r_path, 'w',encoding='utf-8') as file:
                    file.write(str(down_box.get()))
                w_root5()

            def down_box2_save():
                with open(s_path, 'w',encoding='utf-8') as file:
                    file.write(str(down_box2.get()))

            def down_box3_save():
                with open(t_path, 'w',encoding='utf-8') as file:
                    file.write(str(down_box3.get()))

            down_box = ttk.Combobox(w_4_2, values=["横排样式","竖排样式","自定义样式【未完成】"], state="readonly")
            down_box.grid(row=0, column=1, padx=5, pady=5)
            down_box.bind("<<ComboboxSelected>>", lambda event: event_t())
            t = str(load_down_box() or "横排样式")
            match t:
                case "横排样式":
                    down_box.set("横排样式")
                case "竖排样式":
                    down_box.set("竖排样式")

            down_box2 = ttk.Combobox(w_4_2, values=["作本月","作下月","月中为界"], state="readonly")
            down_box2.grid(row=1, column=1, padx=5, pady=5)
            down_box2.bind("<<ComboboxSelected>>", lambda event: down_box2_save())
            t2 = str(load_down_box2() or "作下月")
            match t2:
                case "作下月":
                    down_box2.set("作下月")
                case "作本月":
                    down_box2.set("作本月")
                case "月中为界":
                    down_box2.set("月中为界")

            down_box3 = ttk.Combobox(w_4_2, values=["子时视明日","子时视本日","子时中而分界"], state="readonly")
            down_box3.grid(row=2, column=1, padx=5, pady=5)
            down_box3.bind("<<ComboboxSelected>>", lambda event: down_box3_save())
            t3 = str(load_down_box3() or "子时视明日")
            match t3:
                case "子时视明日":
                    down_box3.set("子时视明日")
                case "子时视本日":
                    down_box3.set("子时视本日")
                case "子时中而分界":
                    down_box3.set("子时中而分界")
        
        w_4_3_()

        w_4_2_()

    w_root4()

    def w_root5():

        t = str(load_down_box() or "横排样式")

        def w_root5_window1_():
                w_root5_window1 = ttk.Toplevel(window)
                child_windows.append(w_root5_window1)
                w_root5_window1.resizable(0,0)
                w_root5_window1.title("轻量记事本-界面示例")
                w_root5_window1.iconbitmap(icon_path)
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
                combobox = ttk.Combobox(master=w_root5_window1, values=["男","女","其它"])
                combobox.grid(row=0, column=9,padx=10,pady=10)

        def w_root5_window2_():
                w_root5_window2 = ttk.Toplevel(window)
                child_windows.append(w_root5_window2)
                w_root5_window2.resizable(0,0)
                w_root5_window2.title("轻量记事本-界面示例")
                w_root5_window2.iconbitmap(icon_path)
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
                combobox = ttk.Combobox(master=w_root5_window2, values=["男","女","其它"])
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
    r_path = os.path.join(p, "r")
    s_path = os.path.join(p,"s")
    t_path = os.path.join(p,"t")
    u_path = os.path.join(p,"u")
    v_path = os.path.join(p,"v")
    w_path = os.path.join(p,"w")
    x_path = os.path.join(p,"x")
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