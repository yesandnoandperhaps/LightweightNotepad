import re
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Separator

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from LightweightNotepad.window_module.OldXiaoLiuRenWindowPatch import LabelManager
from LightweightNotepad.window_module.NewXiaoLiuRenWindow import NewX
from LightweightNotepad.function.ProjectFunctions import t_save, t_load
from LightweightNotepad.function.ProjectPathVariables import N_PATH, P_PATH, Q_PATH, U_PATH, V_PATH, ICON_PATH
from LightweightNotepad.module import XiaoLiuRen as XiaoLiuren

num_wv1 = int(t_load(N_PATH) or 0)
t_rule_num = int(t_load(P_PATH) or 1)
t_rule_num2 = int(t_load(Q_PATH) or 2)

def wv_1():
    global num_wv1
    num_wv1 = num_wv1 + 1
    t_save(N_PATH, num_wv1)

# 关于小六壬###分割线

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,DuplicatedCode
def xiao_liu_ren_window(root_main, icon, font_style):
    window = ttk.Toplevel(str(root_main))
    window.title("小六壬")
    window.iconbitmap(ICON_PATH)

    # noinspection DuplicatedCode
    def loop_output2():


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
            xiao_liu_ren_window(root_main, icon, font_style)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
        def t_loop_output_x():

            # noinspection DuplicatedCode
            def loop_output_x():
                # noinspection DuplicatedCode
                def recover():
                    text_widget.delete(1.0, END)
                    text_widget.insert(tk.END, "已完成循环")
                    entry2.pack_forget()
                    text2.pack_forget()
                    entry.pack(padx=5, pady=5, side='right')
                    entry.config(font=font_style)
                    text.pack(padx=5, pady=5, side='right')
                    w3.grid_remove()
                    w.grid()

                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)

                match entry___:
                    case []:
                        text_widget.insert(tk.END, "已循环次数：0")
                        loop_t_rule_num = int(t_load(P_PATH) or 1)
                        loop_t_rule_num2 = int(t_load(Q_PATH) or 2)
                        buffer = []

                        match loop_t_rule_num:
                            case 0:
                                match loop_t_rule_num2:
                                    case 1:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+', encoding='utf-8') as file:
                                                    file.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLiuren.numgua2_1())
                                            num = num + 1
                                            if num % 200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END, "{}".format(num))
                                    case 0:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+', encoding='utf-8') as file:
                                                    file.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLiuren.numgua2_0())
                                            num = num + 1
                                            if num % 200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END, "{}".format(num))
                                    case 2:
                                        while True:
                                            if num == int(entry_):
                                                with open(file_path_csv, 'a+', encoding='utf-8') as file:
                                                    file.write(''.join(buffer))
                                                recover()
                                                break
                                            buffer.append(XiaoLiuren.numgua2_2())
                                            num = num + 1
                                            if num % 200 == 0:
                                                text_widget.delete(1.6, END)
                                                text_widget.insert(tk.END, "{}".format(num))
                            case 1:
                                while True:
                                    if num == int(entry_):
                                        with open(file_path_csv, 'a+', encoding='utf-8') as file:
                                            file.write(''.join(buffer))
                                        recover()
                                        break
                                    buffer.append(XiaoLiuren.numgua2_3())
                                    num = num + 1
                                    if num % 200 == 0:
                                        text_widget.delete(1.6, END)
                                        text_widget.insert(tk.END, "{}".format(num))
                            case 2:
                                while True:
                                    if num == int(entry_):
                                        with open(file_path_csv, 'a+', encoding='utf-8') as file:
                                            file.write(''.join(buffer))
                                        recover()
                                        break
                                    buffer.append(XiaoLiuren.numgua2_4())
                                    num = num + 1
                                    if num % 200 == 0:
                                        text_widget.delete(1.6, END)
                                        text_widget.insert(tk.END, "{}".format(num))

                    case _:
                        messagebox.showerror("错误", message="请只输入整数", parent=window)
                        entry2.pack_forget()
                        text2.pack_forget()
                        entry.pack(padx=5, pady=5, side='right')
                        entry.config(font=font_style)
                        text.pack(padx=5, pady=5, side='right')
                        w3.grid_remove()
                        w.grid()

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
            def x_x():
                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                def entry_row_name_():
                    if entry_row_name.get():
                        try:
                            with open(file_path_csv, 'w', encoding='utf-8') as file:
                                file.write("{}\n".format(entry_row_name.get()))
                            window_x.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=loop_output_x)
                            thread.start()
                        except Exception as e:
                            messagebox.showerror("错误，已退出循环", f"发生错误: {e}\n可能与文件是否设置有关",
                                                 parent=window)
                            entry2_2_1()
                    else:
                        messagebox.showerror("错误", f"必须有列名", parent=window_x)

                window_x = ttk.Toplevel()
                window_x.title("小六壬")
                window_x.iconbitmap(ICON_PATH)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text = ttk.Label(window_x, text="列名：")
                text.pack(padx=5, pady=5, side="left")
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.pack(padx=5, pady=5, side="right")
                entry_row_name.insert(tk.END, "吉值")
                entry_row_name.bind('<Return>', lambda event: entry_row_name_())
                entry_row_name.bind('<Shift_L>', lambda event: entry2_2_1())

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
            def x_x_():

                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                # noinspection DuplicatedCode
                def entry_row_name_():
                    if entry_row_name.get() and entry_row_name2.get() and entry_row_name3.get() and entry_row_name4.get():
                        try:
                            with open(file_path_csv, 'w', encoding='utf-8') as file:
                                file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                  entry_row_name3.get(), entry_row_name4.get()))
                            window_x.destroy()
                            window.wm_attributes('-disabled', 0)
                            window.wm_attributes('-topmost', 1)
                            window.wm_attributes('-topmost', 0)
                            thread = threading.Thread(target=loop_output_x)
                            thread.start()
                        except Exception as e:
                            messagebox.showerror("错误，已退出循环", f"发生错误: {e}\n可能与文件是否设置有关",
                                                 parent=window)
                            entry2_2_1()
                    else:
                        messagebox.showerror("错误", f"必须有列名", parent=window_x)

                window_x = ttk.Toplevel()
                window_x.title("小六壬")
                window_x.iconbitmap(ICON_PATH)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text = ttk.Label(window_x, text="列名一")
                text.grid(row=0, column=0, padx=5, pady=5)
                text2 = ttk.Label(window_x, text="列名二")
                text2.grid(row=0, column=1, padx=5, pady=5)
                text3 = ttk.Label(window_x, text="列名三")
                text3.grid(row=0, column=2, padx=5, pady=5)
                text4 = ttk.Label(window_x, text="列名四")
                text4.grid(row=0, column=3, padx=5, pady=5)
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.grid(row=1, column=0, padx=5, pady=5)
                entry_row_name2 = ttk.Entry(window_x)
                entry_row_name2.grid(row=1, column=1, padx=5, pady=5)
                entry_row_name3 = ttk.Entry(window_x)
                entry_row_name3.grid(row=1, column=2, padx=5, pady=5)
                entry_row_name4 = ttk.Entry(window_x)
                entry_row_name4.grid(row=1, column=3, padx=5, pady=5)
                entry_row_name.insert(tk.END, "天宫")
                entry_row_name2.insert(tk.END, "地宫")
                entry_row_name3.insert(tk.END, "人宫")
                entry_row_name4.insert(tk.END, "吉值")
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

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
            def x_x__():

                def combobox_save():
                    with open(U_PATH, "w", encoding='utf-8') as file:
                        file.write(str(combobox.get()))

                def combobox_load():
                    try:
                        with open(U_PATH, 'r', encoding='utf-8') as file:
                            return file.read()
                    except FileNotFoundError:
                        pass

                t = str(combobox_load() or "顺序数据【空亡定为6】")

                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
                def entry_row_name_():

                    t = str(combobox_load() or "顺序数据【空亡定为6】")

                    # noinspection PyShadowingNames,DuplicatedCode
                    def x_x__x():

                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()

                        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
                        def entry_row_name__():
                            with open(file_path_csv, 'w', encoding='utf-8') as file:
                                file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
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
                            thread = threading.Thread(target=loop_output_x)
                            thread.start()

                        window_x_ = ttk.Toplevel()
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(ICON_PATH)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_ = ttk.Label(window_x_, text="列名一")
                        text2_ = ttk.Label(window_x_, text="列名二")
                        text3_ = ttk.Label(window_x_, text="列名三")
                        text4_ = ttk.Label(window_x_, text="列名四")
                        text5_ = ttk.Label(window_x_, text="列名五")
                        text6_ = ttk.Label(window_x_, text="列名六")
                        text7_ = ttk.Label(window_x_, text="列名七")
                        text8_ = ttk.Label(window_x_, text="列名八")
                        text9_ = ttk.Label(window_x_, text="列名九")
                        text10_ = ttk.Label(window_x_, text="列名十")
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
                        text_.grid(row=0, column=0, padx=5, pady=5)
                        text2_.grid(row=0, column=1, padx=5, pady=5)
                        text3_.grid(row=0, column=2, padx=5, pady=5)
                        text4_.grid(row=2, column=0, padx=5, pady=5)
                        text5_.grid(row=2, column=1, padx=5, pady=5)
                        text6_.grid(row=2, column=2, padx=5, pady=5)
                        text7_.grid(row=4, column=0, padx=5, pady=5)
                        text8_.grid(row=4, column=1, padx=5, pady=5)
                        text9_.grid(row=4, column=2, padx=5, pady=5)
                        text10_.grid(row=6, column=0, padx=5, pady=5)
                        entry_row_name_.grid(row=1, column=0, padx=5, pady=5)
                        entry_row_name2_.grid(row=1, column=1, padx=5, pady=5)
                        entry_row_name3_.grid(row=1, column=2, padx=5, pady=5)
                        entry_row_name4_.grid(row=3, column=0, padx=5, pady=5)
                        entry_row_name5_.grid(row=3, column=1, padx=5, pady=5)
                        entry_row_name6_.grid(row=3, column=2, padx=5, pady=5)
                        entry_row_name7_.grid(row=5, column=0, padx=5, pady=5)
                        entry_row_name8_.grid(row=5, column=1, padx=5, pady=5)
                        entry_row_name9_.grid(row=5, column=2, padx=5, pady=5)
                        entry_row_name10_.grid(row=7, column=0, padx=5, pady=5)
                        entry_row_name_.insert(tk.END, entry_row_name.get() + "(1)")
                        entry_row_name2_.insert(tk.END, entry_row_name.get() + "(2)")
                        entry_row_name3_.insert(tk.END, entry_row_name.get() + "(3)")
                        entry_row_name4_.insert(tk.END, entry_row_name2.get() + "(1)")
                        entry_row_name5_.insert(tk.END, entry_row_name2.get() + "(2)")
                        entry_row_name6_.insert(tk.END, entry_row_name2.get() + "(3)")
                        entry_row_name7_.insert(tk.END, entry_row_name3.get() + "(1)")
                        entry_row_name8_.insert(tk.END, entry_row_name3.get() + "(2)")
                        entry_row_name9_.insert(tk.END, entry_row_name3.get() + "(3)")
                        entry_row_name10_.insert(tk.END, entry_row_name4.get())
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

                    # noinspection PyShadowingNames,DuplicatedCode
                    def x_x__x_():
                        # noinspection DuplicatedCode
                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()

                        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
                        def entry_row_name__():
                            with open(file_path_csv, 'w', encoding='utf-8') as file:
                                file.write(
                                    '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
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
                            thread = threading.Thread(target=loop_output_x)
                            thread.start()

                        window_x_ = ttk.Toplevel()
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(ICON_PATH)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_ = ttk.Label(window_x_, text="列名一【顺序数据】")
                        text2_ = ttk.Label(window_x_, text="列名二【顺序数据】")
                        text3_ = ttk.Label(window_x_, text="列名三【顺序数据】")
                        text4_ = ttk.Label(window_x_, text="列名四【值数据】")
                        text5_ = ttk.Label(window_x_, text="列名五【值数据】")
                        text6_ = ttk.Label(window_x_, text="列名六【值数据】")
                        text7_ = ttk.Label(window_x_, text="列名七【详细值数据】")
                        text8_ = ttk.Label(window_x_, text="列名八【详细值数据】")
                        text9_ = ttk.Label(window_x_, text="列名九【详细值数据】")
                        text10_ = ttk.Label(window_x_, text="列名十【详细值数据】")
                        text11_ = ttk.Label(window_x_, text="列名十一【详细值数据】")
                        text12_ = ttk.Label(window_x_, text="列名十二【详细值数据】")
                        text13_ = ttk.Label(window_x_, text="列名十三【详细值数据】")
                        text14_ = ttk.Label(window_x_, text="列名十四【详细值数据】")
                        text15_ = ttk.Label(window_x_, text="列名十五【详细值数据】")
                        text16_ = ttk.Label(window_x_, text="列名十六【吉值】")

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

                        text_.grid(row=0, column=0, padx=5, pady=5)
                        text2_.grid(row=0, column=1, padx=5, pady=5)
                        text3_.grid(row=0, column=2, padx=5, pady=5)
                        text4_.grid(row=2, column=0, padx=5, pady=5)
                        text5_.grid(row=2, column=1, padx=5, pady=5)
                        text6_.grid(row=2, column=2, padx=5, pady=5)
                        text7_.grid(row=4, column=0, padx=5, pady=5)
                        text8_.grid(row=4, column=1, padx=5, pady=5)
                        text9_.grid(row=4, column=2, padx=5, pady=5)
                        text10_.grid(row=6, column=0, padx=5, pady=5)
                        text11_.grid(row=6, column=1, padx=5, pady=5)
                        text12_.grid(row=6, column=2, padx=5, pady=5)
                        text13_.grid(row=8, column=0, padx=5, pady=5)
                        text14_.grid(row=8, column=1, padx=5, pady=5)
                        text15_.grid(row=8, column=2, padx=5, pady=5)
                        text16_.grid(row=10, column=0, padx=5, pady=5)

                        entry_row_name_.grid(row=1, column=0, padx=5, pady=5)
                        entry_row_name2_.grid(row=1, column=1, padx=5, pady=5)
                        entry_row_name3_.grid(row=1, column=2, padx=5, pady=5)
                        entry_row_name4_.grid(row=3, column=0, padx=5, pady=5)
                        entry_row_name5_.grid(row=3, column=1, padx=5, pady=5)
                        entry_row_name6_.grid(row=3, column=2, padx=5, pady=5)
                        entry_row_name7_.grid(row=5, column=0, padx=5, pady=5)
                        entry_row_name8_.grid(row=5, column=1, padx=5, pady=5)
                        entry_row_name9_.grid(row=5, column=2, padx=5, pady=5)
                        entry_row_name10_.grid(row=7, column=0, padx=5, pady=5)
                        entry_row_name11_.grid(row=7, column=1, padx=5, pady=5)
                        entry_row_name12_.grid(row=7, column=2, padx=5, pady=5)
                        entry_row_name13_.grid(row=9, column=0, padx=5, pady=5)
                        entry_row_name14_.grid(row=9, column=1, padx=5, pady=5)
                        entry_row_name15_.grid(row=9, column=2, padx=5, pady=5)
                        entry_row_name16_.grid(row=11, column=0, padx=5, pady=5)

                        entry_row_name_.insert(tk.END, entry_row_name.get() + "【顺序数据】")
                        entry_row_name2_.insert(tk.END, entry_row_name2.get() + "【顺序数据】")
                        entry_row_name3_.insert(tk.END, entry_row_name3.get() + "【顺序数据】")

                        entry_row_name4_.insert(tk.END, entry_row_name.get() + "【值数据】")
                        entry_row_name5_.insert(tk.END, entry_row_name2.get() + "【值数据】")
                        entry_row_name6_.insert(tk.END, entry_row_name3.get() + "【值数据】")

                        entry_row_name7_.insert(tk.END, entry_row_name.get() + "(1)【详细值数据】")
                        entry_row_name8_.insert(tk.END, entry_row_name.get() + "(2)【详细值数据】")
                        entry_row_name9_.insert(tk.END, entry_row_name.get() + "(3)【详细值数据】")
                        entry_row_name10_.insert(tk.END, entry_row_name2.get() + "(1)【详细值数据】")
                        entry_row_name11_.insert(tk.END, entry_row_name2.get() + "(2)【详细值数据】")
                        entry_row_name12_.insert(tk.END, entry_row_name2.get() + "(3)【详细值数据】")
                        entry_row_name13_.insert(tk.END, entry_row_name3.get() + "(1)【详细值数据】")
                        entry_row_name14_.insert(tk.END, entry_row_name3.get() + "(2)【详细值数据】")
                        entry_row_name15_.insert(tk.END, entry_row_name3.get() + "(3)【详细值数据】")

                        entry_row_name16_.insert(tk.END, entry_row_name4.get())

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

                    # noinspection PyShadowingNames,DuplicatedCode
                    def x_x__x__():
                        # noinspection DuplicatedCode
                        def entry2_2_2():
                            window_x_.destroy()
                            entry2_2()

                        # noinspection PyShadowingNames
                        def entry_row_name__():
                            with open(file_path_csv, 'w', encoding='utf-8') as file:
                                file.write(
                                    '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(entry_row_name_.get(),
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
                            thread = threading.Thread(target=loop_output_x)
                            thread.start()

                        window_x_ = ttk.Toplevel()
                        window_x_.title("小六壬")
                        window_x_.iconbitmap(ICON_PATH)
                        window_x_.protocol("WM_DELETE_WINDOW", entry2___)
                        window_x_.wm_attributes('-topmost', 1)
                        window.wm_attributes('-disabled', 1)
                        text_ = ttk.Label(window_x_, text="列名一【顺序数据】【空亡定为6】")
                        text2_ = ttk.Label(window_x_, text="列名二【顺序数据】【空亡定为6】")
                        text3_ = ttk.Label(window_x_, text="列名三【顺序数据】【空亡定为6】")
                        text4_ = ttk.Label(window_x_, text="列名四【顺序数据】【空亡定为0】")
                        text5_ = ttk.Label(window_x_, text="列名五【顺序数据】【空亡定为0】")
                        text6_ = ttk.Label(window_x_, text="列名六【顺序数据】【空亡定为0】")
                        text7_ = ttk.Label(window_x_, text="列名七【值数据】")
                        text8_ = ttk.Label(window_x_, text="列名八【值数据】")
                        text9_ = ttk.Label(window_x_, text="列名九【值数据】")
                        text10_ = ttk.Label(window_x_, text="列名十【详细值数据】")
                        text11_ = ttk.Label(window_x_, text="列名十一【详细值数据】")
                        text12_ = ttk.Label(window_x_, text="列名十二【详细值数据】")
                        text13_ = ttk.Label(window_x_, text="列名十三【详细值数据】")
                        text14_ = ttk.Label(window_x_, text="列名十四【详细值数据】")
                        text15_ = ttk.Label(window_x_, text="列名十五【详细值数据】")
                        text16_ = ttk.Label(window_x_, text="列名十六【详细值数据】")
                        text17_ = ttk.Label(window_x_, text="列名十七【详细值数据】")
                        text18_ = ttk.Label(window_x_, text="列名十八【详细值数据】")
                        text19_ = ttk.Label(window_x_, text="列名十九【吉值】")

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

                        text_.grid(row=0, column=0, padx=5, pady=5)
                        text2_.grid(row=0, column=1, padx=5, pady=5)
                        text3_.grid(row=0, column=2, padx=5, pady=5)
                        text4_.grid(row=2, column=0, padx=5, pady=5)
                        text5_.grid(row=2, column=1, padx=5, pady=5)
                        text6_.grid(row=2, column=2, padx=5, pady=5)
                        text7_.grid(row=4, column=0, padx=5, pady=5)
                        text8_.grid(row=4, column=1, padx=5, pady=5)
                        text9_.grid(row=4, column=2, padx=5, pady=5)
                        text10_.grid(row=6, column=0, padx=5, pady=5)
                        text11_.grid(row=6, column=1, padx=5, pady=5)
                        text12_.grid(row=6, column=2, padx=5, pady=5)
                        text13_.grid(row=8, column=0, padx=5, pady=5)
                        text14_.grid(row=8, column=1, padx=5, pady=5)
                        text15_.grid(row=8, column=2, padx=5, pady=5)
                        text16_.grid(row=10, column=0, padx=5, pady=5)
                        text17_.grid(row=10, column=1, padx=5, pady=5)
                        text18_.grid(row=10, column=2, padx=5, pady=5)
                        text19_.grid(row=12, column=0, padx=5, pady=5)

                        entry_row_name_.grid(row=1, column=0, padx=5, pady=5)
                        entry_row_name2_.grid(row=1, column=1, padx=5, pady=5)
                        entry_row_name3_.grid(row=1, column=2, padx=5, pady=5)
                        entry_row_name4_.grid(row=3, column=0, padx=5, pady=5)
                        entry_row_name5_.grid(row=3, column=1, padx=5, pady=5)
                        entry_row_name6_.grid(row=3, column=2, padx=5, pady=5)
                        entry_row_name7_.grid(row=5, column=0, padx=5, pady=5)
                        entry_row_name8_.grid(row=5, column=1, padx=5, pady=5)
                        entry_row_name9_.grid(row=5, column=2, padx=5, pady=5)
                        entry_row_name10_.grid(row=7, column=0, padx=5, pady=5)
                        entry_row_name11_.grid(row=7, column=1, padx=5, pady=5)
                        entry_row_name12_.grid(row=7, column=2, padx=5, pady=5)
                        entry_row_name13_.grid(row=9, column=0, padx=5, pady=5)
                        entry_row_name14_.grid(row=9, column=1, padx=5, pady=5)
                        entry_row_name15_.grid(row=9, column=2, padx=5, pady=5)
                        entry_row_name16_.grid(row=11, column=0, padx=5, pady=5)
                        entry_row_name17_.grid(row=11, column=1, padx=5, pady=5)
                        entry_row_name18_.grid(row=11, column=2, padx=5, pady=5)
                        entry_row_name19_.grid(row=13, column=0, padx=5, pady=5)

                        entry_row_name_.insert(tk.END, entry_row_name.get() + "【顺序数据】【空亡定为6】")
                        entry_row_name2_.insert(tk.END, entry_row_name2.get() + "【顺序数据】【空亡定为6】")
                        entry_row_name3_.insert(tk.END, entry_row_name3.get() + "【顺序数据】【空亡定为6】")

                        entry_row_name4_.insert(tk.END, entry_row_name.get() + "【顺序数据】【空亡定为0】")
                        entry_row_name5_.insert(tk.END, entry_row_name2.get() + "【顺序数据】【空亡定为0】")
                        entry_row_name6_.insert(tk.END, entry_row_name3.get() + "【顺序数据】【空亡定为0】")

                        entry_row_name7_.insert(tk.END, entry_row_name.get() + "【值数据】")
                        entry_row_name8_.insert(tk.END, entry_row_name2.get() + "【值数据】")
                        entry_row_name9_.insert(tk.END, entry_row_name3.get() + "【值数据】")

                        entry_row_name10_.insert(tk.END, entry_row_name.get() + "(1)【详细值数据】")
                        entry_row_name11_.insert(tk.END, entry_row_name.get() + "(2)【详细值数据】")
                        entry_row_name12_.insert(tk.END, entry_row_name.get() + "(3)【详细值数据】")
                        entry_row_name13_.insert(tk.END, entry_row_name2.get() + "(1)【详细值数据】")
                        entry_row_name14_.insert(tk.END, entry_row_name2.get() + "(2)【详细值数据】")
                        entry_row_name15_.insert(tk.END, entry_row_name2.get() + "(3)【详细值数据】")
                        entry_row_name16_.insert(tk.END, entry_row_name3.get() + "(1)【详细值数据】")
                        entry_row_name17_.insert(tk.END, entry_row_name3.get() + "(2)【详细值数据】")
                        entry_row_name18_.insert(tk.END, entry_row_name3.get() + "(3)【详细值数据】")
                        entry_row_name19_.insert(tk.END, entry_row_name4.get())

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
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "顺序数据【空亡定为0】":
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "值数据":
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "详细值数据【四列】":
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "详细值数据【十列】":
                                    x_x__x()
                                    window_x.destroy()
                                case "全部【空亡定为6】【十六列】":
                                    x_x__x_()
                                    window_x.destroy()
                                case "全部【空亡定为6】【四列】":
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "全部【空亡定为0】【十六列】":
                                    x_x__x_()
                                    window_x.destroy()
                                case "全部【空亡定为0】【四列】":
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                                case "真全部【十九列】":
                                    x_x__x__()
                                    window_x.destroy()
                                case _:
                                    with open(file_path_csv, 'w', encoding='utf-8') as file:
                                        file.write('{},{},{},{}\n'.format(entry_row_name.get(), entry_row_name2.get(),
                                                                          entry_row_name3.get(), entry_row_name4.get()))
                                    window_x.destroy()
                                    window.wm_attributes('-disabled', 0)
                                    window.wm_attributes('-topmost', 1)
                                    window.wm_attributes('-topmost', 0)
                                    thread = threading.Thread(target=loop_output_x)
                                    thread.start()
                        except Exception as e:
                            messagebox.showerror("错误，已退出循环", f"发生错误: {e}\n可能与文件是否设置有关",
                                                 parent=window)
                            entry2_2_1()
                    else:
                        icon.notify("必须有列名", "Lightweight text editor")

                window_x = ttk.Toplevel()
                window_x.title("小六壬")
                window_x.iconbitmap(ICON_PATH)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text = ttk.Label(window_x, text="列名一")
                text.grid(row=0, column=0, padx=5, pady=5)
                text2 = ttk.Label(window_x, text="列名二")
                text2.grid(row=0, column=1, padx=5, pady=5)
                text3 = ttk.Label(window_x, text="列名三")
                text3.grid(row=0, column=2, padx=5, pady=5)
                text4 = ttk.Label(window_x, text="列名四")
                text4.grid(row=0, column=3, padx=5, pady=5)
                text5 = ttk.Label(window_x, text="输出细节")
                text5.grid(row=0, column=4, padx=5, pady=5)
                entry_row_name = ttk.Entry(window_x)
                entry_row_name.grid(row=1, column=0, padx=5, pady=5)
                entry_row_name2 = ttk.Entry(window_x)
                entry_row_name2.grid(row=1, column=1, padx=5, pady=5)
                entry_row_name3 = ttk.Entry(window_x)
                entry_row_name3.grid(row=1, column=2, padx=5, pady=5)
                entry_row_name4 = ttk.Entry(window_x)
                entry_row_name4.grid(row=1, column=3, padx=5, pady=5)

                combobox = ttk.Combobox(master=window_x, values=["顺序数据【空亡定为6】", "顺序数据【空亡定为0】",
                                                                 "值数据", "详细值数据【四列】", "详细值数据【十列】",
                                                                 "全部【空亡定为6】【十六列】", "全部【空亡定为6】【四列】",
                                                                 "全部【空亡定为0】【十六列】", "全部【空亡定为0】【四列】",
                                                                 "真全部【十九列】"
                                                                 ], state="readonly")
                combobox.grid(row=1, column=4, padx=5, pady=5, ipadx=10)
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
                    case _:
                        combobox.set("顺序数据【空亡定为6】")
                        combobox_save()
                entry_row_name.insert(tk.END, "天宫")
                entry_row_name2.insert(tk.END, "地宫")
                entry_row_name3.insert(tk.END, "人宫")
                entry_row_name4.insert(tk.END, "吉值")
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

            check_up_num = int(t_load(P_PATH) or 1)

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
            entry2.pack(padx=5, pady=5, side='right')
            entry2.config(font=font_style)
            entry2.insert(tk.END, entrynum)
            entry2.bind('<Return>', lambda event: entry2_())
            entry2.bind('<Shift_L>', lambda event: entry2_2())
            text2 = ttk.Label(w2, text="循环次数")
            text2.pack(padx=5, pady=5, side='right')
            text_widget.delete(1.0, END)
            w.grid_remove()
            w3 = ttk.Frame(window)
            w3.grid(row=2, column=0, sticky=E)

            if t_rule_num2 == 1:
                b3 = ttk.Button(w3, text="输出不去尾", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')
            elif t_rule_num2 == 0:
                b3 = ttk.Button(w3, text="输出保留整数", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')
            elif t_rule_num2 == 2:
                b3 = ttk.Button(w3, text="输出保留两位", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')

            if t_rule_num == 1:
                b2 = ttk.Button(w3, text="常规文字循环输出", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
            elif t_rule_num == 2:
                b2 = ttk.Button(w3, text="常规数据循环输出", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
            elif t_rule_num == 3:
                icon.notify("选用的方法不适用于该文件", "Lightweight text editor")
                entry2_2()

            b4 = ttk.Button(w3, text="循环输出csv文件", style=OUTLINE, command=entry2__)
            b4.pack(padx=5, pady=5, side='right')
            b1 = ttk.Button(w3, text="循环输出txt文件", style=OUTLINE, command=entry2__)
            b1.pack(padx=5, pady=5, side='right')
            Separator(w3, orient=VERTICAL).pack(fill=Y, padx=5, pady=5, side='right')
            wv1 = ttk.IntVar()
            if num_wv1 % 2 == 1:
                wv1.set(1)
            else:
                wv1.set(0)
            consider_checkbutton2 = ttk.Checkbutton(w3, text="本页为首", variable=wv1, command=wv_1,
                                                    style="round-toggle", state="disabled")
            consider_checkbutton2.pack(padx=5, pady=5, side='right')

        if f.winfo_viewable():
            f.grid_remove()
            text_widget.grid()
            scrollbar.grid()
            combo.grid_remove()
            w2 = ttk.Frame(window)
            w2.grid(row=0, column=0, sticky=W)
            entry = tk.Entry(w2)
            entry.pack(padx=5, pady=5, side='right')
            entry.config(font=font_style)
            text = ttk.Label(w2, text="循环次数")
            text.pack(padx=5, pady=5, side='right')
            entry.focus_set()
            entry.bind('<Return>', lambda event: t_loop_output_x())
            entry.bind('<Shift_L>', lambda event: entry2_2())
        else:
            combo.grid_remove()
            w2 = ttk.Frame(window)
            w2.grid(row=0, column=0, sticky=W)
            entry = tk.Entry(w2)
            entry.pack(padx=5, pady=5, side='right')
            entry.config(font=font_style)
            text = ttk.Label(w2, text="循环次数")
            text.pack(padx=5, pady=5, side='right')
            entry.focus_set()
            entry.bind('<Return>', lambda event: t_loop_output_x())
            entry.bind('<Shift_L>', lambda event: entry2_2())

    # noinspection DuplicatedCode
    def loop_output():
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
            xiao_liu_ren_window(root_main, icon, font_style)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
        def t_loop_output_x():

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
            def loop_output_x():
                # noinspection DuplicatedCode
                def recover():
                    text_widget.delete(1.0, END)
                    text_widget.insert(tk.END, "已完成循环")
                    entry2.pack_forget()
                    text2.pack_forget()
                    entry.pack(padx=5, pady=5, side='right')
                    entry.config(font=font_style)
                    text.pack(padx=5, pady=5, side='right')
                    w3.grid_remove()
                    w.grid()

                entry_ = entry.get()
                num = 0
                entry___ = re.findall('[^0-9]', entry_)
                match entry___:
                    case []:
                        try:
                            text_widget.insert(tk.END, "已循环次数：0")
                            t_rule_num = int(t_load(P_PATH) or 1)
                            t_rule_num2 = int(t_load(Q_PATH) or 2)
                            buffer = []

                            match t_rule_num:
                                case 0:
                                    match t_rule_num2:
                                        case 1:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+', encoding='utf-8') as file:
                                                        file.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLiuren.numgua2_1())
                                                num = num + 1
                                                if num % 200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END, "{}".format(num))
                                        case 0:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+', encoding='utf-8') as file:
                                                        file.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLiuren.numgua2_0())
                                                num = num + 1
                                                if num % 200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END, "{}".format(num))
                                        case 2:
                                            while True:
                                                if num == int(entry_):
                                                    with open(file_path, 'a+', encoding='utf-8') as file:
                                                        file.write(''.join(buffer))
                                                    recover()
                                                    break
                                                buffer.append(XiaoLiuren.numgua2_2())
                                                num = num + 1
                                                if num % 200 == 0:
                                                    text_widget.delete(1.6, END)
                                                    text_widget.insert(tk.END, "{}".format(num))
                                case 1:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+', encoding='utf-8') as file:
                                                file.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLiuren.numgua2_3())
                                        num = num + 1
                                        if num % 200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END, "{}".format(num))
                                case 2:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+', encoding='utf-8') as file:
                                                file.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLiuren.numgua2_5())
                                        num = num + 1
                                        if num % 200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END, "{}".format(num))
                                case 3:
                                    while True:
                                        if num == int(entry_):
                                            with open(file_path, 'a+', encoding='utf-8') as file:
                                                file.write(''.join(buffer))
                                            recover()
                                            break
                                        buffer.append(XiaoLiuren.numgua())
                                        num = num + 1
                                        if num % 200 == 0:
                                            text_widget.delete(1.6, END)
                                            text_widget.insert(tk.END, "{}".format(num))
                        except Exception as e:
                            messagebox.showerror("错误，已退出循环", f"发生错误: {e}\n可能与文件是否设置有关",
                                                 parent=window)
                            entry2_2()
                    case _:
                        messagebox.showerror("错误", message="请只输入整数", parent=window)
                        entry2.pack_forget()
                        text2.pack_forget()
                        entry.pack(padx=5, pady=5, side='right')
                        entry.config(font=font_style)
                        text.pack(padx=5, pady=5, side='right')
                        w3.grid_remove()
                        w.grid()

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
            def x1_x():

                def entry2_2_1():
                    window_x.destroy()
                    entry2_2()

                def combobox_save():
                    with open(V_PATH, "w", encoding='utf-8') as file:
                        file.write(str(combobox.get()))

                def combobox_load():
                    try:
                        with open(V_PATH, 'r', encoding='utf-8') as file:
                            return file.read()
                    except FileNotFoundError:
                        pass

                # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
                def combobox_():
                    try:
                        window_x.destroy()
                        window.wm_attributes('-disabled', 0)
                        window.wm_attributes('-topmost', 1)
                        window.wm_attributes('-topmost', 0)
                        thread = threading.Thread(target=loop_output_x)
                        thread.start()
                    except Exception as e:
                        messagebox.showerror("错误，已退出循环", f"发生错误: {e}\n可能与文件是否设置有关", parent=window)
                        entry2_2_1()

                window_x = ttk.Toplevel()
                window_x.title("小六壬")
                window_x.iconbitmap(ICON_PATH)
                window_x.protocol("WM_DELETE_WINDOW", entry2___)
                window_x.wm_attributes('-topmost', 1)
                window.wm_attributes('-disabled', 1)
                text_ = ttk.Label(window_x, text="输出细节")
                text_.grid(row=0, column=0, padx=5, pady=5)
                combobox = ttk.Combobox(master=window_x, values=["顺序数据【空亡定为6】", "顺序数据【空亡定为0】", "值数据",
                                                                 "详细值数据【四列】", "详细值数据【十列】"],
                                        state="readonly")
                combobox.grid(row=1, column=0, padx=5, pady=5)
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
                    case _:
                        combobox.set("顺序数据【空亡定为6】")
                        combobox_save()
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
            entry2.pack(padx=5, pady=5, side='right')
            entry2.config(font=font_style)
            entry2.insert(tk.END, entrynum)
            entry2.bind('<Return>', lambda event: entry2_())
            entry2.bind('<Shift_L>', lambda event: entry2_2())
            text2 = ttk.Label(w2, text="循环次数")
            text2.pack(padx=5, pady=5, side='right')
            text_widget.delete(1.0, END)
            w.grid_remove()
            w3 = ttk.Frame(window)
            w3.grid(row=2, column=0, sticky=E)
            t_rule_num = int(t_load(P_PATH) or 1)

            if t_rule_num2 == 1:
                b3 = ttk.Button(w3, text="输出不去尾", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')
            elif t_rule_num2 == 0:
                b3 = ttk.Button(w3, text="输出保留整数", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')
            elif t_rule_num2 == 2:
                b3 = ttk.Button(w3, text="输出保留两位", style=OUTLINE, command=entry2__)
                b3.pack(padx=5, pady=5, side='right')

            if t_rule_num == 1:
                b2 = ttk.Button(w3, text="常规文字循环输出", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
                thread = threading.Thread(target=loop_output_x)
                thread.start()
            elif t_rule_num == 0:
                b2 = ttk.Button(w3, text="只循环输出吉值", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
                thread = threading.Thread(target=loop_output_x)
                thread.start()
            elif t_rule_num == 2:
                b2 = ttk.Button(w3, text="常规数据循环输出", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
                x1_x()
            elif t_rule_num == 3:
                b2 = ttk.Button(w3, text="旧版循环输出【仅限txt文件】", style=OUTLINE, command=entry2__)
                b2.pack(padx=5, pady=5, side='right')
                thread = threading.Thread(target=loop_output_x)
                thread.start()

            b4 = ttk.Button(w3, text="循环输出csv文件", style=OUTLINE, command=entry2__)
            b4.pack(padx=5, pady=5, side='right')
            b1 = ttk.Button(w3, text="循环输出txt文件", style=OUTLINE, command=entry2__)
            b1.pack(padx=5, pady=5, side='right')
            Separator(w3, orient=VERTICAL).pack(fill=Y, padx=5, pady=5, side='right')
            wv1 = ttk.IntVar()
            if num_wv1 % 2 == 1:
                wv1.set(1)
            else:
                wv1.set(0)
            consider_checkbutton2 = ttk.Checkbutton(w3, text="本页为首", variable=wv1, command=wv_1,
                                                    style="round-toggle", state="disabled")
            consider_checkbutton2.pack(padx=5, pady=5, side='right')

        if f.winfo_viewable():
            f.grid_remove()
            text_widget.grid()
            scrollbar.grid()
            combo.grid_remove()
            w2 = ttk.Frame(window)
            w2.grid(row=0, column=0, sticky=W)
            entry = tk.Entry(w2)
            entry.pack(padx=5, pady=5, side='right')
            entry.config(font=font_style)
            text = ttk.Label(w2, text="循环次数")
            text.pack(padx=5, pady=5, side='right')
            entry.focus_set()
            entry.bind('<Return>', lambda event: t_loop_output_x())
            entry.bind('<Shift_L>', lambda event: entry2_2())
        else:
            combo.grid_remove()
            w2 = ttk.Frame(window)
            w2.grid(row=0, column=0, sticky=W)
            entry = tk.Entry(w2)
            entry.pack(padx=5, pady=5, side='right')
            entry.config(font=font_style)
            text = ttk.Label(w2, text="循环次数")
            text.pack(padx=5, pady=5, side='right')
            entry.focus_set()
            entry.bind('<Return>', lambda event: t_loop_output_x())
            entry.bind('<Shift_L>', lambda event: entry2_2())

    def count_b3_3():
        rule_num = 1
        b3.config(text="输出不去尾", command=count_b3_1)
        t_save(Q_PATH, rule_num)

    def count_b3_2():
        rule_num = 2
        b3.config(text="输出保留两位", command=count_b3_3)
        t_save(Q_PATH, rule_num)

    def count_b3_1():
        rule_num = 0
        b3.config(text="输出保留整数", command=count_b3_2)
        t_save(Q_PATH, rule_num)

    def count_b2_4():
        rule_num = 3
        b2.config(text="旧版循环输出【仅限txt文件】", command=count_b2_2)
        t_save(P_PATH, rule_num)

    def count_b2_3():
        rule_num = 2
        b2.config(text="常规数据循环输出", command=count_b2_4)
        t_save(P_PATH, rule_num)

    def count_b2_2():
        rule_num = 1
        b2.config(text="常规文字循环输出", command=count_b2_1)
        t_save(P_PATH, rule_num)

    def count_b2_1():
        rule_num = 0
        b2.config(text="只循环输出吉值", command=count_b2_3)
        t_save(P_PATH, rule_num)

    def generate_and_display():
        text_widget.delete(1.0, tk.END)

        if combo.get() == "算一卦":
            f.grid_remove()
            text_widget.grid()
            scrollbar.grid()
            text_widget.insert(tk.END, XiaoLiuren.numgua())
        elif combo.get() == "起卦":
            text_widget.grid_remove()
            scrollbar.grid_remove()
            f.grid()
            xlr_num = NewX(window).choose()
            label_manager = LabelManager(f, font_style)
            label_manager.create_labels(xlr_num)

    combo = ttk.Combobox(window, values=["起卦", "算一卦"], state="readonly")
    combo.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    combo.bind("<Button-3>", lambda event: generate_and_display())
    combo.bind("<Button-2>", lambda event: generate_and_display())
    combo.set("起卦")

    def event_t():
        if down_box.get() == "返回主页":
            window.destroy()
            root_main.deiconify()

    down_box = ttk.Combobox(window, values=["返回主页"], state="readonly")
    down_box.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    down_box.bind("<Button-3>", lambda event: event_t())
    down_box.set("返回主页")
    scrollbar = ttk.Scrollbar(window, style="round")
    scrollbar.grid(row=1, column=1, sticky="ns")
    text_widget = tk.Text(window, wrap="word",
                          yscrollcommand=scrollbar.set, font=font_style)
    text_widget.grid(row=1, column=0, sticky="nsew")
    scrollbar.config(command=text_widget.yview)

    f = ttk.Frame(window)
    f.grid(row=1, column=0, sticky="nsew")
    f.grid_remove()

    w = ttk.Frame(window)
    w.grid(row=2, column=0, sticky=E)

    if t_rule_num2 == 1:
        b3 = ttk.Button(w, text="输出不去尾", style=OUTLINE, command=count_b3_1)
        b3.pack(padx=5, pady=5, side='right')
    elif t_rule_num2 == 0:
        b3 = ttk.Button(w, text="输出保留整数", style=OUTLINE, command=count_b3_2)
        b3.pack(padx=5, pady=5, side='right')
    elif t_rule_num2 == 2:
        b3 = ttk.Button(w, text="输出保留两位", style=OUTLINE, command=count_b3_3)
        b3.pack(padx=5, pady=5, side='right')

    if t_rule_num == 1:
        b2 = ttk.Button(w, text="常规文字循环输出", style=OUTLINE, command=count_b2_1)
        b2.pack(padx=5, pady=5, side='right')
    elif t_rule_num == 0:
        b2 = ttk.Button(w, text="只循环输出吉值", style=OUTLINE, command=count_b2_3)
        b2.pack(padx=5, pady=5, side='right')
    elif t_rule_num == 2:
        b2 = ttk.Button(w, text="常规数据循环输出", style=OUTLINE, command=count_b2_4)
        b2.pack(padx=5, pady=5, side='right')
    elif t_rule_num == 3:
        b2 = ttk.Button(w, text="旧版循环输出【仅限txt文件】", style=OUTLINE, command=count_b2_2)
        b2.pack(padx=5, pady=5, side='right')

    b4 = ttk.Button(w, text="循环输出csv文件", style=OUTLINE, command=loop_output2)
    b4.pack(padx=5, pady=5, side='right')
    b1 = ttk.Button(w, text="循环输出txt文件", style=OUTLINE, command=loop_output)
    b1.pack(padx=5, pady=5, side='right')
    Separator(w, orient=VERTICAL).pack(fill=Y, padx=5, pady=5, side='right')
    wv1 = ttk.IntVar()
    if num_wv1 % 2 == 1:
        wv1.set(1)
    else:
        wv1.set(0)
    consider_checkbutton2 = ttk.Checkbutton(w, text="本页为首", variable=wv1, command=wv_1, style="round-toggle")
    consider_checkbutton2.pack(padx=5, pady=5, side='right')
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()