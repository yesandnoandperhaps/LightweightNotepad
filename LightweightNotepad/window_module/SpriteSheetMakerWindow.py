import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap.constants import *

from function.ProjectFunctions import t_load
from function.ProjectPathVariables import Z_PATH, AA_PATH, AB_PATH, ICON_PATH


# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
class SpriteSheetMaker(tk.Toplevel):
    def __init__(self,icon=None):
        super().__init__()
        self.icon = icon
        self.title("精灵图制作")
        self.iconbitmap(ICON_PATH)
        self.images = []
        self.image_labels = []
        self.sprite_sheet = None

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, style="round", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.image_frame = tk.Frame(self.canvas)

        self.internal_frame = tk.Frame(self.canvas)
        self.internal_frame.pack(side=tk.RIGHT, fill=tk.Y)
        # noinspection PyTypeChecker
        self.internal_frame.bind("<Configure>", self.update_scrollregion)

        self.image_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.create_window((0, 0), window=self.image_frame, anchor="ne")

        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.add_button = ttk.Button(self.control_frame, text="添加图片", style=OUTLINE, command=self.t_add_images)
        self.add_button.pack(pady=5)

        self.clear_button = ttk.Button(self.control_frame, text="清除图片", style=OUTLINE, command=self.clear_images)
        self.clear_button.pack(pady=5)

        self.create_button = ttk.Button(self.control_frame, text="生成精灵图", style=OUTLINE, command=self.t_create_spritesheet)
        self.create_button.pack(pady=5)

        self.save_button = ttk.Button(self.control_frame, text="保存精灵图", style=OUTLINE, command=self.t_save_spritesheet)
        self.save_button.pack(pady=5)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def update_scrollregion(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_images(self):
        self.add_button.configure(state="disabled")
        file_paths = filedialog.askopenfilenames(title="选择图片文件", filetypes=[("PNG文件", "*.png")], parent=self)
        self.icon.notify("已开始", "Lightweight text editor")
        if file_paths:
            for file_path in file_paths:
                image = Image.open(file_path)
                self.images.append(image)
                thumbnail = ImageTk.PhotoImage(image.resize((50, 50)))
                label = tk.Label(self.image_frame, image=str(thumbnail))
                label.image = thumbnail
                label.pack(side=tk.TOP, padx=5, pady=5)
                self.image_labels.append(label)
        self.icon.notify("已完成", "Lightweight text editor")
        self.add_button.configure(state="normal")
        self.update_scrollregion()

    def t_add_images(self):
        thread_png = threading.Thread(target=self.add_images)
        thread_png.start()

    def clear_images(self):
        self.add_button.configure(state="normal")
        self.images.clear()
        for label in self.image_labels:
            label.destroy()
        self.image_labels.clear()

    def t_create_spritesheet(self):
        thread_png = threading.Thread(target=self.create_spritesheet)
        thread_png.start()

    def create_spritesheet(self):
        self.add_button.configure(state="disabled")
        self.icon.notify("已开始", "Lightweight text editor")
        if not self.images:
            messagebox.showerror("错误", "没有图片")
            return

        widths, heights = zip(*(i.size for i in self.images))

        total_width = sum(widths)
        max_height = max(heights)

        self.sprite_sheet = Image.new('RGBA', (total_width, max_height))

        x_offset = 0
        for img in self.images:
            self.sprite_sheet.paste(img, (x_offset, 0))
            x_offset += img.width

        self.clear_images()

        self.add_button.configure(state="disabled")
        display_sprite_sheet = self.sprite_sheet.copy()
        display_sprite_sheet.thumbnail((400, 400))
        self.icon.notify("已完成", "Lightweight text editor")

        sprite_image = ImageTk.PhotoImage(display_sprite_sheet)
        self.canvas.create_image(0, 0, anchor="nw", image=sprite_image)
        self.canvas.image = sprite_image

    def t_save_spritesheet(self):
        thread = threading.Thread(target=self.save_spritesheet)
        thread.start()

    def save_spritesheet(self):
        self.icon.notify("已开始", "Lightweight text editor")
        var_num_w_4_3 = int(t_load(Z_PATH) or 1)
        var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
        var3_num_w_4_3 = int(t_load(AB_PATH) or 0)

        if self.sprite_sheet:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG文件", "*.png")])
            try:
                if var_num_w_4_3 % 2 == 1:

                    if file_path:

                        self.sprite_sheet.save(file_path)
                        self.icon.notify(f"保存成功\n精灵图已保存到: {file_path}", "Lightweight text editor")

                if (var2_num_w_4_3 % 2 == 1) or (var3_num_w_4_3 % 2 == 1):

                    thread = threading.Thread(target=self.generate_html_css, args=(file_path,))
                    thread.start()

                if (var_num_w_4_3 % 2 == 0) and (var2_num_w_4_3 % 2 == 0) and (var3_num_w_4_3 % 2 == 0):
                    messagebox.showerror("错误", "设置错误", parent=self)
            except Exception as e:
                messagebox.showerror("错误", f"错误{e}", parent=self)
        else:
            messagebox.showerror("错误", "没有精灵图", parent=self)

    def generate_html_css(self, sprite_path):
        try:
            var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
            var3_num_w_4_3 = int(t_load(AB_PATH) or 0)
            sprite_name = os.path.basename(sprite_path)
            sprite_folder = os.path.dirname(sprite_path)

            html_content = f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <title>精灵图展示</title>
            <link rel="stylesheet" href="{sprite_name.replace('.png', '.css')}">
        </head>
        <body>
            <div class="sprite-container">
        """

            css_content = f""".sprite-container {{
            background: url('{sprite_name}') no-repeat;
            width: {self.sprite_sheet.width}px;
            height: {self.sprite_sheet.height}px;
        }}\n"""

            x_offset = 0
            for index, img in enumerate(self.images):
                width, height = img.size
                html_content += f'<div class="sprite sprite-{index + 1}"></div>\n'
                css_content += f""".sprite-{index + 1} {{
                width: {width}px;
                height: {height}px;
                background-position: -{x_offset}px 0;
            }}\n"""
                x_offset += width

            html_content += """
            </div>
        </body>
        </html>
        """

            if var3_num_w_4_3 % 2 == 1:
                html_file_path = os.path.join(str(sprite_folder), str(sprite_name).replace('.png', '.html'))
                with open(html_file_path, 'w', encoding='utf-8') as html_f:
                    html_f.write(html_content)
                self.icon.notify(f"HTML文件已保存到: {sprite_folder}", "Lightweight text editor")


            if var2_num_w_4_3 % 2 == 1:
                css_file_path = os.path.join(str(sprite_folder), str(sprite_name).replace('.png', '.css'))
                with open(css_file_path, 'w', encoding='utf-8') as css_f:
                    css_f.write(css_content)
                self.icon.notify(f"CSS文件已保存到: {sprite_folder}", "Lightweight text editor")

        except Exception as e:
                messagebox.showerror("错误", f"错误{e}", parent=self)