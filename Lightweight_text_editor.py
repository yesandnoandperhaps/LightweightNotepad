import tkinter as tk
import tkinter.font as tkFont
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
from tkinter import filedialog
from tkinter import font
import ctypes
from pathlib import Path
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
import time
p = os.path.dirname(__file__)
a_path = os.path.join(p, "a")
b_path = os.path.join(p, "b")
c_path = os.path.join(p,"c")
d_path = os.path.join(p,"d")
e_path = os.path.join(p,"e")
f_path = os.path.join(p,"f")
icon_path = os.path.join(p, "aaa.ico")
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
v = int(load() or 0)
v2 = int(load2() or 1)
v3 = int(load3() or 0)
v4 = int(load4() or 0)
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


def x():
    window = tk.Toplevel(root)
    window.title("小六壬")
    window.iconbitmap(icon_path)
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
        if 下拉框.get() == "返回":
            window.destroy()
        if 下拉框.get() == "保存数据":
            save_data()
        if 下拉框.get() == "上传数据":
            window.destroy()

    def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()

    下拉菜单组 = ["返回", "保存数据", "上传数据"]
    下拉框 = ttk.Combobox(window, values=下拉菜单组, state="readonly")
    下拉框.grid(row=0, column=0, sticky="e")
    下拉框.bind("<Button-3>", 下拉框事件)
    下拉框.set("返回")
    scrollbar = ttk.Scrollbar(window, style="TScrollbar", bootstyle="round")
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_widget = tk.Text(window, wrap="word",
                          yscrollcommand=scrollbar.set, font=font_style)
    text_widget.grid(row=1, column=0, sticky="nsew")
    scrollbar.config(command=text_widget.yview)
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
    global theme_cbo
    window = ttk.Toplevel()
    def bao_chun(): 
        global v2,v3,v4
        p1=v2%2
        p2=v3%2
        p3=v4%2
        if p1+p2+p3==1:
            save(theme_cbo.get())    
        else:
            messagebox.showerror("错误", message="不支持多字体或无字体选择",parent=window)
    window.title("轻量记事本-设置")
    window.iconbitmap(icon_path)
    window_Button_two = ttk.Button(
        window, text="返回", bootstyle="outline", command=window.destroy)
    window_Button_two.grid(column=4,row=0,padx=10,pady=10)
    window_Button = ttk.Button(
        window, text="保存当前设置", bootstyle="outline", command=bao_chun)
    window_Button.grid(column=3,row=0,padx=10,pady=10)
    consider_var = ttk.IntVar()
    if v % 2 == 1:
        consider_var.set(1)
    else:
        consider_var.set(0)
    consider_checkbutton = ttk.Checkbutton(
        window, text="是否关联上一次保存的文件", variable=consider_var, command=s, bootstyle="round-toggle")
    consider_checkbutton.grid(column=1,row=3,padx=10,pady=10)
    style = ttk.Style()
    theme_names = style.theme_names()

    lbl = ttk.Label(window, text="选择主题:")
    lbl.grid(column=0,row=0,padx=10,pady=10,ipadx=5)
    lb2 = ttk.Label(window, text="选择字体:")
    lb2.grid(column=0,row=1,padx=10,pady=10,ipadx=5)
    lb3 = ttk.Label(window, text="各项设置:")
    lb3.grid(column=0,row=3,padx=10,pady=10,ipadx=5)
    sep = Separator(window)
    sep.grid(column=0, row=2,pady=50)
    theme_cbo = ttk.Combobox(master=window, values=theme_names)
    theme_cbo.grid(column=1,row=0,padx=10,pady=10)
    theme_cbo.current(theme_names.index(style.theme_use()))
    theme_cbo.bind('<<ComboboxSelected>>', change_theme)
    consider_var_2 = ttk.IntVar()
    if v2 % 2 == 1:
        consider_var_2.set(1)
    else:
        consider_var_2.set(0)
    consider_checkbutton2 = ttk.Checkbutton(window, text="宋体", variable=consider_var_2, command=s2, bootstyle="round-toggle")
    consider_checkbutton2.grid(column=1,row=1,padx=10,pady=10)

    consider_var_3 = ttk.IntVar()
    if v3 % 2 == 1:
        consider_var_3.set(1)
    else:
        consider_var_3.set(0)
    consider_checkbutton3 = ttk.Checkbutton(window, text="等线", variable=consider_var_3, command=s3, bootstyle="round-toggle")
    consider_checkbutton3.grid(column=2,row=1,padx=10,pady=10)

    consider_var_4 = ttk.IntVar()
    if v4 % 2 == 1:
        consider_var_4.set(1)
    else:
        consider_var_4.set(0)
    consider_checkbutton4 = ttk.Checkbutton(window, text="黑体", variable=consider_var_4, command=s4, bootstyle="round-toggle")
    consider_checkbutton4.grid(column=3,row=1,padx=10,pady=10)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.mainloop()

def change_theme(event):
    theme_cbo_value = theme_cbo.get()
    style.theme_use(theme_cbo_value)
    theme_cbo.selection_clear()

def quit_window(icon: pystray.Icon):
    icon.stop()
    icon.visible = False
    root.destroy()

def show_window():
    root.deiconify()

def on_exit():
    root.withdraw()
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
if v2 % 2 == 1:
    font_style = font_style1
elif v3 % 2 == 1:
    font_style = font_style2
elif v4 % 2 == 1:
    font_style = font_style3
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor / 75)
style = ttk.Style()
current_theme = load_theme()
if current_theme in style.theme_names():
    style.theme_use(current_theme)
def 前_下拉框事件():
        if 下拉框.get() == "保存":
            save_2()
        elif 下拉框.get() == "设置":
            root_window()
        elif 下拉框.get() == "小工具":
            gadget()
def 下拉框事件(event):
        x, y = event.x_root, event.y_root
        if 下拉框.winfo_rootx() < x < 下拉框.winfo_rootx() + 下拉框.winfo_width() and \
                下拉框.winfo_rooty() < y < 下拉框.winfo_rooty() + 下拉框.winfo_height():
            前_下拉框事件()
下拉菜单组 = ["保存", "设置","小工具"]
下拉框 = ttk.Combobox(root, values=下拉菜单组, state="readonly")
下拉框.grid(row=0, column=0, sticky="e")
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
def a(event):
     deleted_text.append(text_widget.get('1.0', tk.END))
     text_widget.delete('1.0', tk.END)
deleted_text = []
def b():
    if deleted_text:
        deleted_content = deleted_text.pop()
        text_widget.insert(tk.END, deleted_content)
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

root.bind("<Shift_L> ", a)
root.bind("<Control_L>", lambda event: b())
root.bind("<Control-f> ", lambda event:toggle_window())
scrollbar.config(command=text_widget.yview)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


try:
    if v % 2 == 1:
        text_widget.delete('1.0', tk.END)
        with open(a_path, 'r',encoding='utf-8') as f:
            data = f.read()
            text_widget.insert(tk.END, data)
except:
    pass

def save_2():
        file_path = filedialog.asksaveasfilename(parent=root, defaultextension=".txt", filetypes=[
            ("Text files", "*.txt"), ("All files", "*.*")])
        
        with open(a_path, 'w',encoding='utf-8') as f:
             lines = text_widget.get("1.0","end")
             f.writelines(lines)

        if file_path:
            shutil.copy(a_path, file_path)

def i(files):
     msg = '\n'.join((item.decode('gbk') for item in files))
     size = os.path.getsize(msg)
     if size < 262144000:
         with open(msg, 'r',encoding='utf-8') as f:
             data = f.read()
             text_widget.insert(tk.END, data)
     else:
         filename = os.path.basename(msg)
         with open(msg, 'r',encoding='utf-8') as f:
             with open(filename, 'rb') as f:
                 index = 0
                 while True:
                     f.seek(index * 10 * 1024 * 1024)
                     data = f.read(10 * 1024 * 1024)
                     if not data:
                         folder = os.path.join(p, "text-temp")
                         try:
                            os.mkdir("text-temp")
                         except:
                            shutil.rmtree(folder)
                            os.mkdir("text-temp")
                         index -= 1
                         while True:
                             try:
                                shutil.move(f'{filename}_{index}', folder)
                                index -= 1
                             except:
                                try:
                                    os.remove(f'{filename}_{index}')
                                except:
                                    pass
                                break
                         break
                     with open(f'{filename}_{index}', 'wb') as f1:
                         f1.write(data)
                     index += 1


window2 = None
windnd.hook_dropfiles(root,func=i)
root.protocol('WM_DELETE_WINDOW', on_exit)
threading.Thread(target=icon.run, daemon=True).start()
root.mainloop()