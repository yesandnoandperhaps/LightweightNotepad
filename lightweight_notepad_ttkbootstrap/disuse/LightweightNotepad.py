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


# noinspection PyTypeChecker
class FadeInAnimation:
    def __init__(self, windows, image_path_png, steps=20, delay=100):
        self.photo = None
        self.root = windows
        self.image_path = image_path_png
        self.steps = steps
        self.delay = delay
        self.alpha = 0  # 初始透明度
        self.increment = 255 // steps  # 计算每次增加的透明度步长

        # 加载原始图像并创建一个标签用于显示
        self.original_image = Image.open(image_path_png).convert("RGBA")
        self.image_label = tk.Label(windows,bg="white", relief="flat")
        self.image_label.pack(side="right", padx=20)

        # 开始淡入动画
        self.fade_in()

    def fade_in(self):
        # 创建带透明度的图像副本
        faded_image = self.original_image.copy()
        faded_image.putalpha(self.alpha)
        self.photo = ImageTk.PhotoImage(faded_image)

        # 更新图片显示
        self.image_label.config(image=self.photo)

        # 增加透明度，直到达到最大值255
        if self.alpha < 255:
            self.alpha = min(255, self.alpha + self.increment)
            # 继续下一次动画更新
            self.root.after(self.delay, self.fade_in)
# noinspection PyUnresolvedReferences
'''
def import_modules():
    try:
        global ctypes, os, shutil, ttk, filedialog, messagebox
        global pystray, windnd, Image, MenuItem, Menu, font_set, load_theme
        global t_divide_up, circular_num, num_wv1, v, onandoff
        global A_PATH, DATA_FILE_PATH, ICON_PATH, GadgetWindow, OldXiaoLiuRenWindow, set_window

        import ctypes
        import os
        import shutil
        import ttkbootstrap as ttk
        from tkinter import filedialog, messagebox

        import pystray
        import windnd
        from PIL import Image
        from pystray import MenuItem, Menu

        from function.variables.ProjectCapabilityVariables import font_set
        from function.ProjectFunctions import load_theme
        from function.variables.ProjectInitialVariables import t_divide_up, circular_num, num_wv1, v, onandoff
        from function.variables.ProjectPathVariables import A_PATH, DATA_FILE_PATH, ICON_PATH
        from window_module.GadgetWindow import GadgetWindow
        from window_module.xiao_liu_ren_window.OldXiaoLiuRenWindow import OldXiaoLiuRenWindow
        from window_module.set_window.SetWindow import set_window

        # 模块导入完毕后关闭启动窗口
        # noinspection PyTypeChecker
        splash.after(500, continue_execution)

    except Exception as e:
        splash_ = tk.Tk()

        tk.Label(splash_, text=str(e)).pack()

        splash_.mainloop()
'''
# noinspection PyPep8Naming

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
        GadgetWindow(root, icon, FONT_STYLE)

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
        text_widget.tag_remove("found", "1.0", tk.END)
        start = "1.0"
        key = entry.get()
        if len(key.strip()) == 0:
            return
        while True:
            pos = text_widget.search(key, start, tk.END)
            if pos == "":
                break
            text_widget.tag_add("found", pos, "%s+%dc" % (pos, len(key)))
            start = "%s+%dc" % (pos, len(key))

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
        window2.resizable(width=False, height=False)
        window2.wm_attributes("-topmost", True)
        lbl = ttk.Label(window2, text="查找:")
        lbl.grid(row=0, column=0, padx=5, pady=5)
        entry = tk.Entry(window2, width=30)
        entry.grid(row=0, column=1, padx=5, pady=5)
        entry.bind("<Return>", lambda event: mySearch())
        entry.focus_set()
        lb2 = ttk.Label(window2, text="替换:")
        lb2.grid(row=1, column=0, padx=5, pady=5)
        entry2 = tk.Entry(window2, width=30)
        entry2.grid(row=1, column=1, padx=5, pady=5)
        entry2.bind("<Return>", lambda event: replace())
        window2.protocol("WM_DELETE_WINDOW", on)
        window2.bind("<Control-f> ", lambda event: toggle_window())
        entry.bind("<Control-f> ", lambda event: toggle_window())
        entry.bind(" <Down>", lambda event: focus2())
        entry2.bind("<Up>", lambda event: focus1())
        entry2.bind("<Control-f> ", lambda event: toggle_window())
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
            lines = text_widget.get("1.0", "end")
            file.writelines(lines)

        if file_path:
            shutil.copy(A_PATH, file_path)

    thread = threading.Thread(target=save_2t)
    thread.start()


def detect_encoding(file_content):
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

def convert_to_utf8(buf, original_encoding):
    """
    将文件内容从原始编码转换为 UTF-8 编码。
    """
    try:
        # 解码为字符串后再编码为 UTF-8
        return buf.decode(original_encoding).encode('utf-8')
    except Exception as e:
        raise ValueError(f"转换为 UTF-8 时出错: {e}")

def mk_sub_file(src_name, sub, buf, folder):
    [des_filename, extname] = os.path.splitext(os.path.basename(src_name))
    sub_file_path = os.path.join(folder, f"{des_filename}_{sub}{extname}")
    print('正在生成子文件: %s' % sub_file_path)
    with open(sub_file_path, 'wb') as fout:
        fout.write(buf)  # 写入转换后的内容
        # 假设有进度条控件 progressbarOne
        progressbarOne['value'] += 1
    return sub + 1, sub_file_path

def split_by_size(filename, size, folder,encoding):
    sub_files = []  # 用于保存生成的文件路径
    with open(filename, 'rb') as fin:
        buf = fin.read(size)
        sub = 1
        while len(buf) > 0:
            # 转换为 UTF-8
            utf8_buf = convert_to_utf8(buf, encoding)
            # 生成子文件
            sub, sub_file_path = mk_sub_file(filename, sub, utf8_buf, folder)
            sub_files.append(sub_file_path)  # 收集文件路径
            buf = fin.read(size)
    print("ok")
    return sub_files

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def read(filename, msg):
    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyAssignmentToLoopOrWithParameter
    def read_and_split():
        global index, index_, t_size,folder_t
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

            folder_t=split_by_size(msg,t_divide_up,TEXT_TEMP_PATH,encoding)

            size = os.path.getsize(msg)
            division = size // t_divide_up

            division08 = division * 0.1
            progressbarOne['value'] -= division08

            with open(folder_t[0], 'r', encoding='utf-8', errors='ignore') as file:
                a = file.read()
                progressbarOne['value'] += division08
                text_widget.insert(tk.END, a)
                window3.destroy()
                root.attributes("-disabled", 0)
                index_=1



    thread = threading.Thread(target=read_and_split)
    thread.start()

# noinspection PyGlobalUndefined
def save_ff():

    global progressbarOne2

    def save_tf():

        # noinspection PyBroadException,PyShadowingNames
        def save_tt():
            filename_ = os.path.join(TEXT_TEMP_PATH, f'{filename}')
            index = 0
            while True:
                try:
                    folder_t = (TEXT_TEMP_PATH + "\\" + f'{filename}_{index}')
                    with open(folder_t, 'rb', encoding='utf-8', errors='ignore') as file:
                        a = file.read()
                        index += 1
                    with open(filename_, 'a', encoding='utf-8', errors='ignore') as file:
                        file.write(a)
                        progressbarOne2['value'] += 1
                except:
                    index -= 1
                    print(index)
                    division08 = division * 0.1
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
    division = size // t_divide_up
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
        messagebox.showerror("错误", message="正在保存中，请勿退出", parent=window4)

    progressbarOne2 = ttk.Progressbar(window4, style="striped")
    progressbarOne2.pack(pady=5, fill=tk.X)
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
                    lines = text_widget.get("1.0", "end")
                    file.writelines(lines)
                    icon.notify("文件已成功保存", "Lightweight text editor")
            else:
                if index_ == 1:
                    folder_t = (TEXT_TEMP_PATH + "\\" + f'{filename}_{index}')
                    with open(folder_t, 'w', encoding='utf-8') as file:
                        lines = text_widget.get("1.0", "end")
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
            text_widget.insert(tk.END, text)

    elif onandoff == "关闭":

        # noinspection PyShadowingNames
        def save_ttt():
            icon.notify("正在导入文件，不建议操作当前窗口", "Lightweight text editor")
            with open(msg, 'rb') as file:

                while True:

                    data = file.readlines(circular_num)

                    if not data:
                        icon.notify("导入成功", "Lightweight text editor")
                        break

                    # 将 data 列表中的所有字节数据合并成一个字节串
                    combined_data = b''.join(data)

                    # 检测编码
                    result = chardet.detect(combined_data)
                    encoding = result['encoding']

                    # 解码
                    text = combined_data.decode(encoding)

                    # 插入到 text_widget 中
                    text_widget.insert(tk.END, text)

        thread = threading.Thread(target=save_ttt)
        thread.start()

    else:
        size = os.path.getsize(msg)
        division = size // t_divide_up
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
            messagebox.showerror("错误", message="导入过程中，请勿退出", parent=window3)

        progressbarOne = ttk.Progressbar(window3, style="striped")
        progressbarOne.pack(pady=5, fill=tk.X)
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
    try:
        index += 1
        _update_text_widget(folder_t[index])
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
    try:
        index -= 1
        _update_text_widget(folder_t[index])
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
        w.grid(row=2, column=0, sticky=tk.E)

    b4 = ttk.Button(window, text="取消分离", style="link", command=on2)
    b4.pack(padx=5, pady=5, side='left')
    window.protocol("WM_DELETE_WINDOW", on2)
    window.mainloop()

menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR, MenuItem('退出', quit_window))
image = Image.open(ICON_PATH)
icon = pystray.Icon("icon", image, "轻量记事本", menu)

root = ttk.Window(themename="flatly")
root.title("轻量记事本")
root.iconbitmap(ICON_PATH)
root.place_window_center()
FONT_STYLE, v2, v3, v4 = font_set()
print(FONT_STYLE)
style = ttk.Style()
current_theme = load_theme()
if current_theme in style.theme_names():
    style.theme_use(current_theme)
#ctypes.windll.shcore.SetProcessDpiAwareness(1)
#ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
#root.tk.call('tk', 'scaling', ScaleFactor / 75)
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
#t = text_widget.get("1.0", tk.END)
text_widget.focus_set()
w = ttk.Frame(root)
w.grid(row=2, column=0, sticky=tk.E)
b1 = ttk.Button(w, text="分离控制", style="link", command=sever)
b1.pack(padx=5, pady=5, side='left')
# noinspection DuplicatedCode
b2 = ttk.Button(w, text="下一页", style="link", command=next_page)
b2.pack(padx=5, pady=5, side='right')
b3 = ttk.Button(w, text="上一页", style="link", command=return_page)
b3.pack(padx=5, pady=5, side='right')
window2 = None
windnd.hook_dropfiles(root, func=i)
root.protocol('WM_DELETE_WINDOW', on_exit)
threading.Thread(target=icon.run, daemon=True).start()
root.bind("<Control-z> ", a)
root.bind("<Control-y>", lambda event: b())
root.bind("<Shift_L>", lambda event: c())
root.bind("<Control-f> ", lambda event: toggle_window())
root.bind("<Control-x>",lambda event: print("永明体"))#永明体检测
scrollbar.config(command=text_widget.yview)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
index = 0
index_ = 0

action_map = {
    1: lambda: (root.withdraw(), OldXiaoLiuRenWindow(root, icon, FONT_STYLE, 0)), }

action_map.get(num_wv1 % 2, lambda: None)()

try:
    if v % 2 == 1:
        text_widget.delete('1.0', tk.END)
        with open(A_PATH, 'r') as f__:
            data = f__.read()
            text_widget.insert(tk.END, data)
except Exception as error:
    messagebox.showerror("错误", f"发生错误: {error}")

root.mainloop()

'''
if __name__ == '__main__':
    import threading
    import tkinter as tk
    # noinspection PyUnresolvedReferences
    from PIL import Image, ImageTk

    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.attributes("-topmost", True)
    splash.configure(bg="white")

    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()

    window_width = 810
    window_height = 610

    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    splash.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    image_path = r"D:\lightweight_notepad\lightweight_notepad\icon\main_icon_no.png"

    fade_steps = 20
    animation_delay = 100

    anim = FadeInAnimation(splash, image_path, fade_steps, animation_delay)

    f_ = tk.Frame(splash)
    label = tk.Label(f_, text="lightweight_notepad——加载中", font=("宋体", 16), bg="white")

    f_.pack(side="left", padx=20)
    label.grid(column=0, row=0)

    threading.Thread(target=import_modules).start()

    splash.mainloop()
'''