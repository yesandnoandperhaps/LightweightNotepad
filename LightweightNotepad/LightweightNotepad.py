import ctypes
import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import pystray
import ttkbootstrap as ttk
import windnd
from PIL import Image
from pystray import MenuItem, Menu
from ttkbootstrap.constants import *

from OldXiaoLiuRenWindow import xiao_liu_ren_window
from PictureWindow import picture
from ProjectCapabilityVariables import font_set
from ProjectFunctions import window_init, load_theme
from ProjectInitialVariables import t_divide_up, circular_num, num_wv1, v, onandoff
from ProjectPathVariables import A_PATH, DATA_FILE_PATH, ICON_PATH
from RegressionWindow import regression
from SetWindow import set_window
from ZiWeiDouShuWindow import zi_wei_dou_shu_window


###分割线
#关于紫微斗数###分割线

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def gadget():

    def triangle():
        pass

    window = ttk.Toplevel(str(root))
    window_init(window, root, "轻量记事本-小工具")
    window.resizable(None, None)

    b1 = ttk.Button(window, text="小六壬", style=OUTLINE, command=lambda: xiao_liu_ren_window(root, icon, FONT_STYLE))
    b1.grid(column=0,row=0,padx=10,pady=10)
    b2 = ttk.Button(window, text="紫微斗数", style=OUTLINE, command=lambda: zi_wei_dou_shu_window(root, FONT_STYLE))
    b2.grid(column=1,row=0,padx=10,pady=10)
    b3 = ttk.Button(window, text="机器学习-回归问题", style=OUTLINE, command=lambda: regression(root))
    b3.grid(column=2,row=0,padx=10,pady=10)
    b4 = ttk.Button(window, text="三角形计算", style=OUTLINE, command=triangle)
    b4.grid(column=3,row=0,padx=10,pady=10)
    b5 = ttk.Button(window, text="图片操作", style=OUTLINE, command=lambda: picture(root, icon))
    b5.grid(column=4,row=0,padx=10,pady=10)
###分割线

#关于主界面###分割线
def quit_window():
    root.destroy()

def show_window():
    root.deiconify()

def on_exit():
    root.withdraw()


# noinspection PyPep8Naming
def Before_drop_down_box_events():
        if drop_down_box.get() == "保存":
            save_t()
        elif drop_down_box.get() == "设置":
            set_window(root)
        elif drop_down_box.get() == "小工具":
            gadget()

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def drop_down_box_event(event):
        x, y = event.x_root, event.y_root
        if drop_down_box.winfo_rootx() < x < drop_down_box.winfo_rootx() + drop_down_box.winfo_width() and \
                drop_down_box.winfo_rooty() < y < drop_down_box.winfo_rooty() + drop_down_box.winfo_height():
            Before_drop_down_box_events()


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
    global index, index_

    if index_ != 1:
        messagebox.showerror("错误", message="仅限大文件操作", parent=root)
        return

    folder = os.path.join(DATA_FILE_PATH, "text-temp")
    try:
        index += 1
        folder_t = os.path.join(folder, f'{filename}_{index}')
        _update_text_widget(folder_t)
    except FileNotFoundError:
        messagebox.showerror("错误", message="已经是尾页", parent=root)
        index -= 1  # 恢复index为上一页
    except Exception as e:
        messagebox.showerror("错误", message=f"读取文件出错: {str(e)}", parent=root)


# noinspection PyBroadException
def return_page():
    global index, index_

    if index_ != 1:
        messagebox.showerror("错误", message="仅限大文件操作", parent=root)
        return

    folder = os.path.join(DATA_FILE_PATH, "text-temp")
    try:
        index -= 1
        folder_t = os.path.join(folder, f'{filename}_{index}')
        _update_text_widget(folder_t)
    except FileNotFoundError:
        messagebox.showerror("错误", message="已经是首页", parent=root)
        index += 1  # 恢复index为下一页
    except Exception as e:
        messagebox.showerror("错误", message=f"读取文件出错: {str(e)}", parent=root)


def _update_text_widget(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, file.read())


# noinspection DuplicatedCode
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
    menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
    image = Image.open(ICON_PATH)
    icon = pystray.Icon("icon", image, "轻量记事本", menu)
    root = tk.Tk()
    root.title("轻量记事本")
    root.iconbitmap(ICON_PATH)
    FONT_STYLE, v2, v3, v4 = font_set()
    style = ttk.Style()
    current_theme = load_theme()
    if current_theme in style.theme_names():
        style.theme_use(current_theme)
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    root.tk.call('tk', 'scaling', ScaleFactor / 75)
    drop_down_box = ttk.Combobox(root, values=["保存", "设置", "小工具"], state="readonly")
    drop_down_box.grid(row=0, column=0, sticky="e", pady=5)
    drop_down_box.bind("<Button-3>", drop_down_box_event)
    drop_down_box.set("保存")
    # noinspection DuplicatedCode
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
    # noinspection DuplicatedCode
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

    root.mainloop()