import ctypes
import os
import shutil

import chardet
import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
import threading
import tkinter as tk

import pystray
import windnd
from PIL import Image, ImageTk
from pystray import MenuItem, Menu

from function.variables.ProjectCapabilityVariables import font_set
from function.ProjectFunctions import load_theme
from function.variables.ProjectInitialVariables import t_divide_up, circular_num, num_wv1, v, onandoff,t_size
from function.variables.ProjectPathVariables import A_PATH,ICON_PATH,TEXT_TEMP_PATH
from window_module.GadgetWindow import GadgetWindow
from window_module.xiao_liu_ren_window.OldXiaoLiuRenWindow import OldXiaoLiuRenWindow
from window_module.set_window.SetWindow import set_window

class LightweightNotepad(ttk.Window):
    def __init__(self, **kwargs):
        # 初始化窗口

        super().__init__(**kwargs)

        menu = (MenuItem('显示', self.show_window, default=True), Menu.SEPARATOR, MenuItem('退出', self.quit_window))
        image = Image.open(ICON_PATH)
        self.icon = pystray.Icon("icon", image, "轻量记事本", menu)
        self.title("轻量记事本")
        kwargs['iconphoto'] = ICON_PATH
        #print(ICON_PATH)
        self.FONT_STYLE, self.v2, self.v3, self.v4 = font_set()
        print(self.FONT_STYLE)
        style = ttk.Style()
        current_theme = load_theme()
        if current_theme in style.theme_names():
            style.theme_use(current_theme)
        self.drop_down_box = ttk.Combobox(self, values=["保存", "设置", "小工具"], state="readonly")
        self.drop_down_box.grid(row=0, column=0, sticky="e", pady=5)
        self.drop_down_box.bind("<Button-3>", self.drop_down_box_event)
        self.drop_down_box.set("保存")
        # noinspection DuplicatedCode
        self.scrollbar = ttk.Scrollbar(self, style="round")
        self.scrollbar.grid(row=1, column=1, sticky="ns")
        self.text_widget = tk.Text(self, wrap="word",
                              yscrollcommand=self.scrollbar.set, font=self.FONT_STYLE)
        self.text_widget.grid(row=1, column=0, sticky="nsew")
        self.text_widget.tag_configure("found", background="yellow")
        # t = self.text_widget.get("1.0", tk.END)
        self.text_widget.focus_set()
        self.w = ttk.Frame(self)
        self.w.grid(row=2, column=0, sticky=tk.E)
        b1 = ttk.Button(self.w, text="分离控制", style="link", command=self.sever)
        b1.pack(padx=5, pady=5, side='left')
        # noinspection DuplicatedCode
        b2 = ttk.Button(self.w, text="下一页", style="link", command=self.next_page)
        b2.pack(padx=5, pady=5, side='right')
        b3 = ttk.Button(self.w, text="上一页", style="link", command=self.return_page)
        b3.pack(padx=5, pady=5, side='right')
        self.window2 = None
        self.deleted_text = []
        windnd.hook_dropfiles(self, func=self.i)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        threading.Thread(target=self.icon.run, daemon=True).start()
        self.bind("<Control-z> ", self.a)
        self.bind("<Control-y>", lambda event: self.b())
        self.bind("<Shift_L>", lambda event: self.c())
        self.bind("<Control-f> ", lambda event: self.toggle_window())
        self.bind("<Control-x>", lambda event: print("永明体"))  # 永明体检测
        self.scrollbar.config(command=self.text_widget.yview)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.index = 0
        self.index_ = 0

        action_map = {
            1: lambda: (self.withdraw(), OldXiaoLiuRenWindow(self, self.icon, self.FONT_STYLE, 0)), }

        action_map.get(num_wv1 % 2, lambda: None)()

        try:
            if v % 2 == 1:
                self.text_widget.delete('1.0', tk.END)
                with open(A_PATH, 'r') as f__:
                    data = f__.read()
                    self.text_widget.insert(tk.END, data)
        except Exception as error:
            messagebox.showerror("错误", f"发生错误: {error}")

        self.mainloop()

    def quit_window(self):
        self.destroy()

    def show_window(self):
        self.deiconify()

    def on_exit(self):
        self.withdraw()

    # noinspection PyPep8Naming
    def Before_drop_down_box_events(self):
        if self.drop_down_box.get() == "保存":
            self.save_t()
        elif self.drop_down_box.get() == "设置":
            set_window(self)
        elif self.drop_down_box.get() == "小工具":
            GadgetWindow(self, self.icon, self.FONT_STYLE)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
    def drop_down_box_event(self,event):
        x, y = event.x_root, event.y_root
        if self.drop_down_box.winfo_rootx() < x < self.drop_down_box.winfo_rootx() + self.drop_down_box.winfo_width() and \
                self.drop_down_box.winfo_rooty() < y < self.drop_down_box.winfo_rooty() + self.drop_down_box.winfo_height():
            self.Before_drop_down_box_events()

    # noinspection PyUnusedLocal
    def a(self,event):
        self.deleted_text.append(self.text_widget.get('1.0', tk.END))
        self.text_widget.delete('1.0', tk.END)



    def b(self):
        if self.deleted_text:
            deleted_content = self.deleted_text.pop()
            self.text_widget.insert(tk.END, deleted_content)

    def c(self):
        self.text_widget.insert(tk.END, "\n")

    def on(self):
        self.text_widget.tag_configure("found", background="")
        self.toggle_window()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
    def two_window(self):

        # noinspection PyPep8Naming
        def mySearch():
            self.text_widget.tag_remove("found", "1.0", tk.END)
            start = "1.0"
            key = entry.get()
            if len(key.strip()) == 0:
                return
            while True:
                pos = self.text_widget.search(key, start, tk.END)
                if pos == "":
                    break
                self.text_widget.tag_add("found", pos, "%s+%dc" % (pos, len(key)))
                start = "%s+%dc" % (pos, len(key))

        def focus2():
            entry2.focus_set()

        def focus1():
            entry.focus_set()

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyAssignmentToLoopOrWithParameter
        def replace():
            k = entry.get()
            f = entry2.get()
            t = self.text_widget.get(1.0, tk.END)
            new_text = t.replace(k, f)
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.insert(tk.END, new_text)

        if not self.window2:
            self.window2 = ttk.Toplevel()
            self.window2.title("查找与替换")
            self.window2.resizable(width=False, height=False)
            self.window2.wm_attributes("-topmost", True)
            lbl = ttk.Label(self.window2, text="查找:")
            lbl.grid(row=0, column=0, padx=5, pady=5)
            entry = tk.Entry(self.window2, width=30)
            entry.grid(row=0, column=1, padx=5, pady=5)
            entry.bind("<Return>", lambda event: mySearch())
            entry.focus_set()
            lb2 = ttk.Label(self.window2, text="替换:")
            lb2.grid(row=1, column=0, padx=5, pady=5)
            entry2 = tk.Entry(self.window2, width=30)
            entry2.grid(row=1, column=1, padx=5, pady=5)
            entry2.bind("<Return>", lambda event: replace())
            self.window2.protocol("WM_DELETE_WINDOW", self.on)
            self.window2.bind("<Control-f> ", lambda event: self.toggle_window())
            entry.bind("<Control-f> ", lambda event: self.toggle_window())
            entry.bind(" <Down>", lambda event: focus2())
            entry2.bind("<Up>", lambda event: focus1())
            entry2.bind("<Control-f> ", lambda event: self.toggle_window())
            self.window2.mainloop()

    def toggle_window(self):
        if self.window2:
            # noinspection PyUnresolvedReferences
            self.window2.destroy()
            self.window2 = None
        else:
            self.two_window()

    def save_2(self):
        def save_2t():
            file_path = filedialog.asksaveasfilename(parent=self, defaultextension=".txt", filetypes=[
                ("Text files", "*.txt"), ("All files", "*.*")])

            with open(A_PATH, 'w', encoding='utf-8') as file:
                lines = self.text_widget.get("1.0", "end")
                file.writelines(lines)

            if file_path:
                shutil.copy(A_PATH, file_path)

        thread = threading.Thread(target=save_2t)
        thread.start()

    def detect_encoding(self,file_content):
        """
        使用 chardet 检测文件内容的编码。
        """
        result = chardet.detect(file_content)
        encoding = result['encoding']
        confidence = result['confidence']
        if confidence > 0.8:  # 确定性高的情况
            return encoding
        else:
            raise ValueError("无法确定文件的编码，建议手动检查或使用更高置信度的方法。")

    def convert_to_utf8(self,buf, original_encoding):
        """
        将文件内容从原始编码转换为 UTF-8 编码。
        """
        try:
            # 解码为字符串后再编码为 UTF-8
            return buf.decode(original_encoding).encode('utf-8')
        except Exception as e:
            raise ValueError(f"转换为 UTF-8 时出错: {e}")

    def mk_sub_file(self,src_name, sub, buf, folder):
        [des_filename, extname] = os.path.splitext(os.path.basename(src_name))
        sub_file_path = os.path.join(folder, f"{des_filename}_{sub}{extname}")
        print('正在生成子文件: %s' % sub_file_path)
        with open(sub_file_path, 'wb') as fout:
            fout.write(buf)  # 写入转换后的内容
            # 假设有进度条控件 progressbarOne
            progressbarOne['value'] += 1
        return sub + 1, sub_file_path

    def split_by_size(self,filename, size, folder, encoding):
        sub_files = []  # 用于保存生成的文件路径
        with open(filename, 'rb') as fin:
            buf = fin.read(size)
            sub = 1
            while len(buf) > 0:
                # 转换为 UTF-8
                utf8_buf = self.convert_to_utf8(buf, encoding)
                # 生成子文件
                sub, sub_file_path = self.mk_sub_file(filename, sub, utf8_buf, folder)
                sub_files.append(sub_file_path)  # 收集文件路径
                buf = fin.read(size)
        print("ok")
        return sub_files

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
    def read(self,filename, msg):
        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyAssignmentToLoopOrWithParameter
        def read_and_split():
            # 确定目标文件夹路径

            os.makedirs(TEXT_TEMP_PATH, exist_ok=True)

            # 打开文件进行逐块读取
            with open(msg, 'rb') as file:  # 'rb' 表示二进制模式读取
                # 读取文件的前 10KB 数据来检测编码
                raw_data = file.read(10240)

                # 使用 chardet 检测编码
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                print(f"Detected encoding: {encoding}")

                self.folder_t = self.split_by_size(msg, t_divide_up, TEXT_TEMP_PATH, encoding)

                size = os.path.getsize(msg)
                division = size // t_divide_up

                division08 = division * 0.1
                progressbarOne['value'] -= division08

                with open(self.folder_t[0], 'r', encoding='utf-8', errors='ignore') as file:
                    a = file.read()
                    progressbarOne['value'] += division08
                    self.text_widget.insert(tk.END, a)
                    window3.destroy()
                    self.attributes("-disabled", 0)
                    self.index_ = 1

        thread = threading.Thread(target=read_and_split)
        thread.start()

    # noinspection PyGlobalUndefined
    def save_ff(self):

        global progressbarOne2

        def save_tf():

            # noinspection PyBroadException,PyShadowingNames
            def save_tt():
                filename_ = os.path.join(TEXT_TEMP_PATH, f'{filename}')
                self.index = 0
                while True:
                    try:
                        folder_t = (TEXT_TEMP_PATH + "\\" + f'{filename}_{self.index}')
                        with open(folder_t, 'rb', encoding='utf-8', errors='ignore') as file:
                            a = file.read()
                            self.index += 1
                        with open(filename_, 'a', encoding='utf-8', errors='ignore') as file:
                            file.write(a)
                            progressbarOne2['value'] += 1
                    except:
                        self.index -= 1
                        print(self.index)
                        division08 = division * 0.1
                        progressbarOne2['value'] -= division08
                        shutil.copy(filename_, msg)
                        progressbarOne2['value'] += division08
                        window4.destroy()
                        self.attributes("-disabled", 0)
                        self.icon.notify("文件已成功保存", "Lightweight text editor")
                        break

            thread = threading.Thread(target=save_tt)
            thread.start()

        size = os.path.getsize(msg)
        division = size // t_divide_up
        window4 = ttk.Toplevel(self)
        window4.title("保存")
        window4.resizable(None, None)
        window4.minsize(400, 50)
        window4.maxsize(400, 50)
        window4.wm_attributes("-topmost", True)
        self.attributes("-disabled", 1)
        lbl = ttk.Label(window4, text="正在保存中")
        lbl.pack(padx=5, pady=5)

        def on2():
            messagebox.showerror("错误", message="正在保存中，请勿退出", parent=window4)

        progressbarOne2 = ttk.Progressbar(window4, style="striped")
        progressbarOne2.pack(pady=5, fill=tk.X)
        progressbarOne2['maximum'] = division
        progressbarOne2['value'] = 0
        window4.protocol("WM_DELETE_WINDOW", on2)
        save_tf()
        window4.mainloop()

    # noinspection PyBroadException,PyShadowingNames
    def save_t(self):
        try:
            size = os.path.getsize(msg)
            filename = os.path.basename(msg)
            if os.path.exists(msg):
                if size < t_size:
                    with open(msg, 'w', encoding='utf-8') as file:
                        lines = self.text_widget.get("1.0", "end")
                        file.writelines(lines)
                        self.icon.notify("文件已成功保存", "Lightweight text editor")
                else:
                    if self.index_ == 1:
                        folder_t = (TEXT_TEMP_PATH + "\\" + f'{filename}_{self.index}')
                        with open(folder_t, 'w', encoding='utf-8') as file:
                            lines = self.text_widget.get("1.0", "end")
                            file.writelines(lines)
                            self.save_ff()
                    else:
                        pass
            else:
                self.save_2()
        except:
            self.save_2()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
    def i(self,files):
        global progressbarOne, window3, filename, t_size, msg
        msg = '\n'.join((item.decode('gbk') for item in files))
        filename = os.path.basename(msg)
        size = os.path.getsize(msg)

        if size < t_size:
            with open(msg, 'rb') as file:
                data = file.read()
                # 检测编码
                result = chardet.detect(data)
                encoding = result['encoding']

                # 使用检测到的编码解码文件内容
                text = data.decode(encoding)
                self.text_widget.insert(tk.END, text)

        elif onandoff == "关闭":

            # noinspection PyShadowingNames
            def save_ttt():
                self.icon.notify("正在导入文件，不建议操作当前窗口", "Lightweight text editor")
                with open(msg, 'rb') as file:

                    while True:

                        data = file.readlines(circular_num)

                        if not data:
                            self.icon.notify("导入成功", "Lightweight text editor")
                            break

                        # 将 data 列表中的所有字节数据合并成一个字节串
                        combined_data = b''.join(data)

                        # 检测编码
                        result = chardet.detect(combined_data)
                        encoding = result['encoding']

                        # 解码
                        text = combined_data.decode(encoding)

                        # 插入到 self.text_widget 中
                        self.text_widget.insert(tk.END, text)

            thread = threading.Thread(target=save_ttt)
            thread.start()

        else:
            size = os.path.getsize(msg)
            division = size // t_divide_up
            window3 = ttk.Toplevel(self)
            window3.title("导入")
            window3.resizable(None, None)
            window3.minsize(400, 50)
            window3.maxsize(400, 50)
            window3.wm_attributes("-topmost", True)
            self.attributes("-disabled", 1)
            lbl = ttk.Label(window3, text="正在导入中")
            lbl.pack(padx=5, pady=5)

            def on2():
                messagebox.showerror("错误", message="导入过程中，请勿退出", parent=window3)

            progressbarOne = ttk.Progressbar(window3, style="striped")
            progressbarOne.pack(pady=5, fill=tk.X)
            progressbarOne['maximum'] = division
            progressbarOne['value'] = 0
            window3.protocol("WM_DELETE_WINDOW", on2)
            self.read(filename, msg)
            window3.mainloop()

    # noinspection PyBroadException,PyGlobalUndefined
    def next_page(self):
        if self.index_ != 1:
            messagebox.showerror("错误", message="仅限大文件操作", parent=self)
            return
        try:
            self.index += 1
            self._update_text_widget(self,self.folder_t[self.index])
        except FileNotFoundError:
            messagebox.showerror("错误", message="已经是尾页", parent=self)
            self.index -= 1  # 恢复index为上一页
        except Exception as e:
            messagebox.showerror("错误", message=f"读取文件出错: {str(e)}", parent=self)

    # noinspection PyBroadException
    def return_page(self):

        if self.index_ != 1:
            messagebox.showerror("错误", message="仅限大文件操作", parent=self)
            return
        try:
            self.index -= 1
            self._update_text_widget(self.folder_t[self.index])
        except FileNotFoundError:
            messagebox.showerror("错误", message="已经是首页", parent=self)
            self.index += 1  # 恢复index为下一页
        except Exception as e:
            messagebox.showerror("错误", message=f"读取文件出错: {str(e)}", parent=self)

    def _update_text_widget(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.insert(tk.END, file.read())

    # noinspection DuplicatedCode
    def sever(self):
        self.w.grid_forget()
        window = ttk.Toplevel(self)
        window.title("分离控制")
        window.resizable(None, None)
        window.minsize(400, 50)
        window.maxsize(400, 50)
        sever_window_b2 = ttk.Button(window, text="下一页", style="link", command=self.next_page)
        sever_window_b2.pack(padx=5, pady=5, side='right')
        sever_window_b3 = ttk.Button(window, text="上一页", style="link", command=self.return_page)
        sever_window_b3.pack(padx=5, pady=5, side='right')

        def on2():
            window.destroy()
            self.w.grid(row=2, column=0, sticky=tk.E)

        b4 = ttk.Button(window, text="取消分离", style="link", command=on2)
        b4.pack(padx=5, pady=5, side='left')
        window.protocol("WM_DELETE_WINDOW", on2)
        window.mainloop()

if __name__ == '__main__':
    LightweightNotepad(iconphoto=ICON_PATH)
