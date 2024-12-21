import os
import re
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

import numpy as np
import ttkbootstrap as ttk
from PIL import Image
from ttkbootstrap.constants import *

from function.ProjectFunctions import window_init
from window_module.SpriteSheetMakerWindow import SpriteSheetMaker
from function.variables.ProjectPathVariables import W_PATH, X_PATH, Y_PATH, \
    ICON_PATH


def picture(root_main,icon):
    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def color():
        rgb = None
        rgb_ = None

        def root_w_4_3_load():
            try:
                with open(W_PATH, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                pass

        def root_w_4_3_load_2():
            try:
                with open(X_PATH, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                pass

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def choose_color():
            nonlocal rgb
            color = colorchooser.askcolor(parent=window__)
            rgb = color[0]

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def choose_color_():
            nonlocal rgb_
            color = colorchooser.askcolor(parent=window__)
            rgb_ = color[0]

        def color_rgb():
            if rgb is None or rgb_ is None:
                messagebox.showerror("错误", message="没有值", parent=window__)
                return
            if not png_path:
                messagebox.showerror("错误", message="没有路径", parent=window__)
                return

            try:
                for path in png_path:
                    img = Image.open(path).convert("RGB")
                    datas = np.array(img)

                    # 创建掩码，确定需要转换的颜色
                    mask = np.all(datas == rgb, axis=-1)

                    # 执行颜色转换
                    datas[mask] = rgb_

                    # 保存处理后的图像
                    img = Image.fromarray(datas, 'RGB')
                    img.save(path, "PNG")
                messagebox.showinfo("完成", "颜色转换完成", parent=window__)
            except Exception as e:
                messagebox.showerror("错误", message=f"处理图像时出错: {e}", parent=window__)

        def color_rgba():
            try:
                entry1_value = entry1.get()
                entry2_value = entry2.get()

                if (not entry1_value.isdigit() or 0 > int(entry1_value) or int(
                        entry1_value) > 225) and entry1_value != "保留原本":
                    messagebox.showerror("错误", message="请输入0~255的值，或输入保留原本", parent=window__)
                    return

                if not entry2_value.isdigit() or int(entry2_value) < 0 or int(entry2_value) > 255:
                    messagebox.showerror("错误", message="请输入0~255的值", parent=window__)
                    return

                entry1_value_int = int(entry1_value) if entry1_value.isdigit() else None
                entry2_value_int = int(entry2_value) if entry2_value.isdigit() else None

                if rgb is None or rgb_ is None:
                    messagebox.showerror("错误", message="没有值", parent=window__)
                    return

                if not png_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                    return

                for path in png_path:
                    img = Image.open(path).convert("RGBA")
                    datas = np.array(img)

                    mask = np.all(datas[:, :, :3] == rgb, axis=-1)

                    if entry1_value == "保留原本":
                        if entry2_value_int is not None:
                            datas[mask] = [rgb_, rgb_, rgb_, entry2_value_int]
                        else:
                            datas[mask] = [rgb_, rgb_, rgb_, datas[mask, 3]]
                    else:
                        if entry2_value_int is not None:
                            datas[mask] = [rgb_, rgb_, rgb_, entry2_value_int]
                        datas[:, :, 3] = entry1_value_int if entry1_value_int is not None else datas[:, :, 3]

                    img = Image.fromarray(datas, 'RGBA')
                    img.save(path, "PNG")
                messagebox.showinfo("完成", "颜色转换完成", parent=window__)
            except Exception as e:
                messagebox.showerror("错误", message=f"发生错误: {str(e)}", parent=window__)

        def is_valid_hex_color(color_):
            pattern = re.compile(r'^#[0-9A-Fa-f]{6}$', re.IGNORECASE)
            return bool(pattern.match(color_))

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def hex_to_rgb(hex_value):

            hex_value = hex_value.lower()
            if hex_value.startswith('#'):
                hex_value = hex_value[1:]

            r = int(hex_value[0:2], 16)
            g = int(hex_value[2:4], 16)
            b = int(hex_value[4:6], 16)

            return r, g, b

        def color_rgba_16():
            nonlocal rgb, rgb_
            if is_valid_hex_color(entry1_1.get()) and is_valid_hex_color(entry2_1.get()):
                if not png_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                    return
                rgb = hex_to_rgb(entry1_1.get())
                rgb_ = hex_to_rgb(entry2_1.get())
                color_rgba()
            else:
                messagebox.showerror("错误", message="十六进制错误", parent=window__)

        def color_rgb_16():
            nonlocal rgb, rgb_
            if is_valid_hex_color(entry1_1.get()) and is_valid_hex_color(entry2_1.get()):
                if not png_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                    return
                rgb = hex_to_rgb(entry1_1.get())
                rgb_ = hex_to_rgb(entry2_1.get())
                color_rgb()
            else:
                messagebox.showerror("错误", message="十六进制错误", parent=window__)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def is_valid_rgb(rgb):
            return all(0 <= value <= 255 for value in rgb)

        def color_rgba_rgb():
            nonlocal rgb, rgb_
            entry1_2_t = entry1_2.get()
            entry2_2_t = entry2_2.get()

            rgb = tuple(map(int, entry1_2_t.split(',')))
            rgb_ = tuple(map(int, entry2_2_t.split(',')))
            if is_valid_rgb(rgb) and is_valid_rgb(rgb_):
                if not png_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                color_rgba()
            else:
                messagebox.showerror("错误", message="RGB值错误", parent=window__)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def color_rgb_rgb():
            nonlocal rgb, rgb_
            entry1_2_t = entry1_2.get()
            entry2_2_t = entry2_2.get()

            rgb = tuple(map(int, entry1_2_t.split(',')))
            rgb_ = tuple(map(int, entry2_2_t.split(',')))
            if all(0 <= x <= 225 for x in rgb) and all(0 <= x <= 225 for x in rgb_):
                if not png_path:
                    messagebox.showerror("错误", message="没有路径", parent=window__)
                color_rgb()
            else:
                messagebox.showerror("错误", message="RGB值错误", parent=window__)

        def get_image_colors(image_path):
            with Image.open(image_path) as img:
                img = img.convert('RGBA')
                pixels = img.getdata()
                colors = set(pixels)
                return colors

        # noinspection PyShadowingNames
        def display_colors(colors):
            # 清空颜色画布
            canvas.delete("all")

            # 设定每行最多显示的颜色数
            max_per_row = 11
            max_rows = 8
            color_size = 50
            padding = 5

            # 获取颜色数量
            total_colors = len(colors)

            # 计算显示区域的高度和宽度
            canvas_width = max_per_row * (color_size + padding) + padding
            canvas_height = min(total_colors // max_per_row + 1, max_rows) * (color_size + padding) + padding

            # 更新画布大小
            canvas.config(width=canvas_width, height=canvas_height)

            # 绘制颜色矩形
            x = padding
            y = padding
            for i, color in enumerate(colors):
                color_hex = rgba_to_hex(color)
                # 使用白色替代透明颜色
                if color[3] == 0:
                    color_hex = '#FFFFFF'  # 替换透明像素为白色

                # 画颜色矩形
                rect_id = canvas.create_rectangle(x, y, x + color_size, y + color_size, fill=color_hex, outline="")
                canvas.tag_bind(rect_id, "<Button-1>", lambda event, c=color: on_color_click(event, c))

                x += color_size + padding
                if (i + 1) % max_per_row == 0:
                    x = padding
                    y += color_size + padding
            canvas.config(scrollregion=canvas.bbox("all"))
            window__.wm_attributes('-disabled', 0)
            messagebox.showinfo("导入", "导入成功", parent=window__)

        def rgba_to_hex(rgba):
            return '#{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2])

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def on_color_click(event, color):
            menu = tk.Menu(window_, tearoff=0)
            menu.add_command(label="设置为需要转换的颜色", command=lambda: set_choose_color(color))
            menu.add_command(label="设置为转换成的颜色", command=lambda: set_choose_color_(color))
            menu.add_command(label="复制颜色十进制", command=lambda: copy_color_decimal(color))
            menu.add_command(label="复制颜色十六进制", command=lambda: copy_color_hex(color))
            menu.post(event.x_root, event.y_root)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def set_choose_color(color):
            nonlocal rgb
            if t == "颜色选择器":
                rgb = (color[0], color[1], color[2])
            elif t == "十六进制":
                hex_color = rgba_to_hex(color)
                entry1_1.delete(0, tk.END)
                entry1_1.insert(tk.END, str(hex_color))
            elif t == "RGB值":
                entry1_2.delete(0, tk.END)
                entry1_2.insert(tk.END, f"{color[0]}, {color[1]}, {color[2]}")

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def set_choose_color_(color):
            nonlocal rgb_
            if t == "颜色选择器":
                rgb_ = (color[0], color[1], color[2])
                if t_ == "RGBA":
                    entry2.delete(0, tk.END)
                    entry2.insert(tk.END, str(color[3]))
            elif t == "十六进制":
                hex_color = rgba_to_hex(color)
                entry2_1.delete(0, tk.END)
                entry2_1.insert(tk.END, str(hex_color))
            elif t == "RGB值":
                if t_ == "RGBA":
                    entry2.delete(0, tk.END)
                    entry2.insert(tk.END, str(color[3]))
                entry2_2.delete(0, tk.END)
                entry2_2.insert(tk.END, f"{color[0]}, {color[1]}, {color[2]}")

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def copy_color_decimal(color):
            decimal_color = f"({color[0]}, {color[1]}, {color[2]})"
            window_.clipboard_clear()
            window_.clipboard_append(decimal_color)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def copy_color_hex(color):
            hex_color = rgba_to_hex(color)
            window_.clipboard_clear()
            window_.clipboard_append(hex_color)

        def exit_win():
            window__.destroy()
            window_.wm_attributes('-topmost', 1)
            window_.wm_attributes('-topmost', 0)

        window__ = ttk.Toplevel(str(window_))
        window__.title("颜色转换")
        window__.iconbitmap(ICON_PATH)
        window__.bind("<Shift_R>", lambda event: exit_win())

        f = ttk.Frame(window__)
        f.grid(column=0, row=0, padx=10, pady=10)

        t = str(root_w_4_3_load() or "颜色选择器")
        t_ = str(root_w_4_3_load_2() or "RGBA")

        if t == "颜色选择器":
            wb1_ = ttk.Button(f, text="颜色选择器", style=OUTLINE, command=choose_color)
            wb1_.grid(column=1, row=0, padx=10, pady=10)
            wb2_ = ttk.Button(f, text="颜色选择器", style=OUTLINE, command=choose_color_)
            wb2_.grid(column=1, row=1, padx=10, pady=10)
            if t_ == "RGBA":
                text3 = ttk.Label(f, text="整张透明度：")
                text3.grid(column=0, row=2, padx=10, pady=10)
                entry1 = tk.Entry(f)
                entry1.grid(column=1, row=2, padx=5, pady=5)
                entry1.insert(tk.END, "保留原本")
                text4 = ttk.Label(f, text="转换颜色透明度：")
                text4.grid(column=0, row=3, padx=10, pady=10)
                entry2 = tk.Entry(f)
                entry2.grid(column=1, row=3, padx=5, pady=5)
                entry2.insert(tk.END, "255")
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_L>', lambda event: color_rgba())
                entry2.bind('<Shift_L>', lambda event: color_rgba())
                wb1_.bind("<Button-3>", lambda event: color_rgba())
                wb2_.bind("<Button-3>", lambda event: color_rgba())
            elif t_ == "RGB":
                wb1_.bind("<Button-3>", lambda event: color_rgb())
                wb2_.bind("<Button-3>", lambda event: color_rgb())
        elif t == "十六进制":
            entry1_1 = tk.Entry(f)
            entry1_1.grid(column=1, row=0, padx=5, pady=5)
            entry2_1 = tk.Entry(f)
            entry2_1.grid(column=1, row=1, padx=5, pady=5)
            if t_ == "RGBA":
                text3 = ttk.Label(f, text="整张透明度：")
                text3.grid(column=0, row=2, padx=10, pady=10)
                entry1 = tk.Entry(f)
                entry1.grid(column=1, row=2, padx=5, pady=5)
                entry1.insert(tk.END, "保留原本")
                text4 = ttk.Label(f, text="转换颜色透明度：")
                text4.grid(column=0, row=3, padx=10, pady=10)
                entry2 = tk.Entry(f)
                entry2.grid(column=1, row=3, padx=5, pady=5)
                entry2.insert(tk.END, "255")
                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry1_1.focus_set())
                entry1_1.bind("<Return>", lambda event: entry2_1.focus_set())
                entry2_1.bind("<Return>", lambda event: entry1.focus_set())
                entry1.bind('<Shift_L>', lambda event: color_rgba_16())
                entry2.bind('<Shift_L>', lambda event: color_rgba_16())
                entry1_1.bind('<Shift_L>', lambda event: color_rgba_16())
                entry2_1.bind('<Shift_L>', lambda event: color_rgba_16())
            elif t_ == "RGB":
                entry1_1.bind('<Shift_L>', lambda event: color_rgb_16())
                entry2_1.bind('<Shift_L>', lambda event: color_rgb_16())
                entry1_1.bind("<Return>", lambda event: entry2_1.focus_set())
                entry2_1.bind("<Return>", lambda event: entry1_1.focus_set())
        elif t == "RGB值":
            entry1_2 = tk.Entry(f)
            entry1_2.grid(column=1, row=0, padx=5, pady=5)
            entry2_2 = tk.Entry(f)
            entry2_2.grid(column=1, row=1, padx=5, pady=5)
            if t_ == "RGBA":
                text3 = ttk.Label(f, text="整张透明度：")
                text3.grid(column=0, row=2, padx=10, pady=10)
                entry1 = tk.Entry(f)
                entry1.grid(column=1, row=2, padx=5, pady=5)
                entry1.insert(tk.END, "保留原本")
                text4 = ttk.Label(f, text="转换颜色透明度：")
                text4.grid(column=0, row=3, padx=10, pady=10)
                entry2 = tk.Entry(f)
                entry2.grid(column=1, row=3, padx=5, pady=5)
                entry2.insert(tk.END, "255")

                entry1.bind("<Return>", lambda event: entry2.focus_set())
                entry2.bind("<Return>", lambda event: entry1_2.focus_set())
                entry1_2.bind("<Return>", lambda event: entry2_2.focus_set())
                entry2_2.bind("<Return>", lambda event: entry1.focus_set())

                entry1.bind('<Shift_L>', lambda event: color_rgba_rgb())
                entry2.bind('<Shift_L>', lambda event: color_rgba_rgb())
                entry1_2.bind('<Shift_L>', lambda event: color_rgba_rgb())
                entry2_2.bind('<Shift_L>', lambda event: color_rgba_rgb())
            elif t_ == "RGB":
                entry1_2.bind("<Return>", lambda event: entry2_2.focus_set())
                entry2_2.bind("<Return>", lambda event: entry1_2.focus_set())
                entry1_2.bind('<Shift_L>', lambda event: color_rgb_rgb())
                entry2_2.bind('<Shift_L>', lambda event: color_rgb_rgb())

        text = ttk.Label(f, text="需要转换的颜色：")
        text.grid(column=0, row=0, padx=10, pady=10)

        text2 = ttk.Label(f, text="转换成的颜色：")
        text2.grid(column=0, row=1, padx=10, pady=10)

        canvas_frame = ttk.Frame(window__)
        canvas_frame.grid(column=0, row=1, padx=10, pady=10, sticky="nsew")

        canvas = tk.Canvas(canvas_frame, bg='white')
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.config(yscrollcommand=scrollbar.set)

        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)

        png_path = filedialog.askopenfilenames(title='请选择需要颜色转换的图片', filetypes=[("PNG", "*.PNG")],
                                               parent=window__)

        # noinspection PyPep8Naming
        def PNG():
            if png_path:
                window__.focus_set()
                window__.wm_attributes('-disabled', 1)
                icon.notify("已开始导入，请耐心等待\n导入期间，当前窗口将被禁用\n强制退出<右Shift>",
                            "Lightweight text editor")
                canvas.delete("all")

                all_colors = set()

                for file_path in png_path:
                    colors = get_image_colors(file_path)
                    all_colors.update(colors)

                display_colors(all_colors)

        thread_png = threading.Thread(target=PNG)
        thread_png.start()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def format_():

        def exit_win():
            window__.destroy()
            window_.wm_attributes('-topmost', 1)
            window_.wm_attributes('-topmost', 0)

        window__ = ttk.Toplevel(str(window_))
        window__.title("格式转换")
        window__.iconbitmap(ICON_PATH)
        window__.bind("<Shift_R>", lambda event: exit_win())

        def f_image():
            output_format = down_box.get()
            messagebox.showinfo("开始", "已开始", parent=window__)
            if output_format == "二进制":
                for file_path in all_path:
                    try:
                        with Image.open(file_path) as img:
                            if img.mode == 'RGBA':
                                img = img.convert('RGB')

                            base, _ = os.path.splitext(file_path)
                            new_file_path = f"{base}.bin"
                            with open(new_file_path, 'wb') as file:
                                img.save(file, format='BMP')

                    except Exception as e:
                        print(f"Error converting {file_path}: {e}")
                messagebox.showinfo("完成", "转换完成", parent=window__)
            else:
                for file_path in all_path:
                    try:
                        with Image.open(file_path) as img:
                            if img.mode == 'RGBA':
                                img = img.convert('RGB')

                            base, ext = os.path.splitext(file_path)
                            new_file_path = f"{base}.{output_format}"
                            img.save(new_file_path, format=output_format)
                    except Exception as e:
                        print(f"Error converting {file_path}: {e}")
                messagebox.showinfo("完成", "转换完成", parent=window__)

        def tf_image():

            thread_png = threading.Thread(target=f_image)
            thread_png.start()

        def down_box_save_1():
            with open(Y_PATH, 'w', encoding='utf-8') as file:
                file.write(str(down_box.get()))

        def w_4_3_load():
            try:
                with open(Y_PATH, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                pass

        text = ttk.Label(window__, text="目标格式：")
        text.grid(column=0, row=0, padx=10, pady=10)

        down_box = ttk.Combobox(window__, values=['png', 'jpeg', 'bmp', 'gif', 'tiff', '二进制'], state="readonly")
        down_box.grid(row=0, column=1, padx=5, pady=5)
        down_box.bind("<<ComboboxSelected>>", lambda event: down_box_save_1())
        down_box.bind("<Button-3>", lambda event: tf_image())
        t = str(w_4_3_load() or "png")
        down_box.set(t)
        all_path = filedialog.askopenfilenames(title='请选择需要格式转换的图片',
                                               filetypes=[("All Images", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff")],
                                               parent=window__)

    def sprites():
        SpriteSheetMaker(icon)

    window_ = ttk.Toplevel(root_main)
    window_init(window_, root_main, "图片操作")
    wb1 = ttk.Button(window_, text="颜色转换", style=OUTLINE, command=color)
    wb1.grid(column=0, row=0, padx=10, pady=10)
    wb2 = ttk.Button(window_, text="格式转换", style=OUTLINE, command=format_)
    wb2.grid(column=1, row=0, padx=10, pady=10)
    wb3 = ttk.Button(window_, text="精灵图制作", style=OUTLINE, command=sprites)
    wb3.grid(column=2, row=0, padx=10, pady=10)