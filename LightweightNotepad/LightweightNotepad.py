import ctypes
import datetime
import idlelib.colorizer as idc
import idlelib.percolator as idp
import json
import os
import re
import shutil
import threading
import tkinter as tk
import tkinter.font as tk_font
from datetime import datetime
from tkinter import filedialog, messagebox, colorchooser
from tkinter.ttk import Separator

import dateutil.tz
import numpy as np
import pystray
import ttkbootstrap as ttk
import windnd
from PIL import Image, ImageTk
from pystray import MenuItem, Menu
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

from ProjectFunctions import t_save, save, t_load, var_save
from function import JsonFile
from function.ProjectVariables import UTC_TIME, A_PATH, B_PATH, C_PATH, D_PATH, E_PATH, F_PATH, H_PATH, I_PATH, J_PATH, \
    K_PATH, L_PATH, M_PATH, N_PATH, R_PATH, S_PATH, T_PATH, W_PATH, X_PATH, Y_PATH, \
    Z_PATH, AA_PATH, AB_PATH, W_ROOT2_C_VAR_2_PATH, ICON_PATH, DATA_FILE_PATH
from module import LinearRegression
from window_module import NewXiaoLiuRenWindow
from window_module.OldXiaoLiuRenWindow import xiao_liu_ren_window


class CustomToolTip(ToolTip):
    def update_text(self, text):
        self.text = text

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
class SpriteSheetMaker(tk.Toplevel):
    def __init__(self):
        super().__init__()

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
        icon.notify("已开始", "Lightweight text editor")
        if file_paths:
            for file_path in file_paths:
                image = Image.open(file_path)
                self.images.append(image)
                thumbnail = ImageTk.PhotoImage(image.resize((50, 50)))
                label = tk.Label(self.image_frame, image=str(thumbnail))
                label.image = thumbnail
                label.pack(side=tk.TOP, padx=5, pady=5)
                self.image_labels.append(label)
        icon.notify("已完成", "Lightweight text editor")
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
        icon.notify("已开始", "Lightweight text editor")
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
        icon.notify("已完成", "Lightweight text editor")

        sprite_image = ImageTk.PhotoImage(display_sprite_sheet)
        self.canvas.create_image(0, 0, anchor="nw", image=sprite_image)
        self.canvas.image = sprite_image

    def t_save_spritesheet(self):
        thread = threading.Thread(target=self.save_spritesheet)
        thread.start()

    def save_spritesheet(self):
        icon.notify("已开始", "Lightweight text editor")
        var_num_w_4_3 = int(t_load(Z_PATH) or 1)
        var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
        var3_num_w_4_3 = int(t_load(AB_PATH) or 0)

        if self.sprite_sheet:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG文件", "*.png")])
            try:
                if var_num_w_4_3 % 2 == 1:

                    if file_path:

                        self.sprite_sheet.save(file_path)
                        icon.notify(f"保存成功\n精灵图已保存到: {file_path}", "Lightweight text editor")

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
                icon.notify(f"HTML文件已保存到: {sprite_folder}", "Lightweight text editor")


            if var2_num_w_4_3 % 2 == 1:
                css_file_path = os.path.join(str(sprite_folder), str(sprite_name).replace('.png', '.css'))
                with open(css_file_path, 'w', encoding='utf-8') as css_f:
                    css_f.write(css_content)
                icon.notify(f"CSS文件已保存到: {sprite_folder}", "Lightweight text editor")

        except Exception as e:
                messagebox.showerror("错误", f"错误{e}", parent=self)
# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
class StartTrainingFrontWindow:
    def __init__(self,window,combo5,combo4,temp_list_2,temp_list):
        self.temp_list = temp_list
        self.whether_save = False
        if not temp_list_2:
            result = messagebox.askyesno("线性回归", "请等待-本次计算将不会保存模型，是否需要进行计算后预测",parent=window)
            if result:
                self.whether_save = True
                if combo5.get() == "CPU":
                    pass
                else:
                    if combo4.get() == "LambdaLR":
                        self.lambda_lr_window()
                    elif combo4.get() == "None":
                        pass
                    else:
                        self.pytorch_window()
            else:
                self.whether_save = False

    @staticmethod
    def lambda_lr_window_(code_input, window):
        try:
            user_code = code_input.get("1.0", tk.END)
            local_vars = {}
            exec(user_code, globals(), local_vars)
            if 'lr_lambda' not in local_vars:
                messagebox.showerror("错误", "未定义lr_lambda",parent=window)
                return
            # noinspection PyUnusedLocal
            lr_lambda = local_vars['lr_lambda']
        except Exception as e:
            messagebox.showerror("错误", str(e),parent=window)

    def lambda_lr_window(self):
        window___ = ttk.Toplevel()
        window___.title("线性回归-LambdaLR-编写函数")
        window___.iconbitmap(ICON_PATH)
        scrollbar = ttk.Scrollbar(window___, style="round")
        scrollbar.grid(row=1, column=1, sticky="ns")
        text_widget = tk.Text(window___, wrap="word",
                              yscrollcommand=scrollbar.set, font=font_style)
        text_widget.grid(row=1, column=0, sticky="nsew")
        text_widget.bind('<Shift_R>', lambda event: self.lambda_lr_window_(text_widget, window___))
        idc.color_config(text_widget)
        scrollbar.config(command=text_widget.yview)
        default_code = \
"""#自定义Py代码
#必须要存在def lr_lambda(epoch)
#基本教程：
#*乘号，**幂
#\\是整除-向下取整，\是除
#return是返回关键字，这是必须的
#epoch是模型训练数
#<Shift-R>下一步
def lr_lambda(epoch):
    return 0.5 ** (epoch // 5)
"""
        text_widget.insert(tk.END, default_code)
        p = idp.Percolator(text_widget)
        d = idc.ColorDelegator()
        p.insertfilter(d)

    @staticmethod
    def pytorch_window():
        window___ = ttk.Toplevel()
        window___.title("线性回归-参数")
        window___.iconbitmap(ICON_PATH)
        f0 = ttk.Frame(window___)
        f1 = ttk.Frame(window___)
        f2 = ttk.Frame(window___)
        f3 = ttk.Frame(window___)
        text_0_x_0 = ttk.Label(f0,text="动量")
        text_0_x_1 = ttk.Label(f0,text="动量衰减")
        text_0_x_2 = ttk.Label(f0,text="权重衰减")
        text_0_x_3 = ttk.Label(f0,text="Nesterov动量")
        text_0_x_4 = ttk.Label(f0, text="绘制损失值")

        text_0_x_e_0 = ttk.Entry(f0)
        text_0_x_e_1 = ttk.Entry(f0)
        text_0_x_e_2 = ttk.Entry(f0)
        text_0_x_e_3 = ttk.Combobox(f0,values=["True","False"] ,state="readonly")
        text_0_x_e_4 = ttk.Combobox(f0, values=["True", "False"], state="readonly")

        sep0 = Separator(window___, orient='horizontal')

        text_1_x_0 = ttk.Label(f1,text="开始值")
        # noinspection PyUnusedLocal
        text_1_x_1 = ttk.Label(f1,text="绘制学习率")
        text_1_x_2 = ttk.Label(f1,text="因子")
        text_1_x_4 = ttk.Label(f1,text="衰减周期")
        text_1_x_5 = ttk.Label(f1,text="恢复周期")
        text_1_x_6 = ttk.Label(f1,text="开始学习率")
        text_1_x_7 = ttk.Label(f1,text="结束学习率")
        text_1_x_8 = ttk.Label(f1,text="衰减率为1时循环次数")
        text_1_x_9 = ttk.Label(f1, text="多项式的幂")
        text_1_x_10 = ttk.Label(f1,text="最大迭代次数")
        text_1_x_11 = ttk.Label(f2,text="最小学习率")
        text_1_x_12 = ttk.Label(f2,text="最大学习率")
        text_1_x_13 = ttk.Label(f2, text="递增周期中训练迭代次数")
        text_1_x_14 = ttk.Label(f2,text="递增递减变化策略")
        text_1_x_15 = ttk.Label(f2,text="scale_fn")
        text_1_x_16 = ttk.Label(f2,text="scale_mode")
        text_1_x_17 = ttk.Label(f2,text="cycle_momentum")
        text_1_x_18 = ttk.Label(f2,text="每次循环中动量上限")
        text_1_x_19 = ttk.Label(f2,text="每次循环中动量下限")
        # noinspection PyUnusedLocal
        text_1_x_20 = ttk.Label(f3,text="串联方式数")

        # noinspection PyUnusedLocal
        def tool_tip():
            text_1_x_2_text =\
'''适用于
MultiplicativeLR中将乘法因子应用到前一个训练次数的LR来调整学习速率
StepLR、MultiStepLR、ExponentialLR中学习率衰减的乘法因子，默认值：0.1
ConstantLR中factor默认值：1/3
ConstantLR中gamma，exp_range模式下，控制学习率随周期的指数衰减，默认值: 1.0
'''
            text_1_x_4_text = \
'''适用于
StepLR中step_size，每到达一定step_size，学习率乘以乘法因子
MultiStepLR中milestones，输入需要是列表，形如10,20,30
MultiStepLR中例如：当训练次数达10，将学习率乘以乘法因子->当训练次数达20，将学习率乘以乘法因子
MultiStepLR中当训练数达到30之后，若无定义，学习率不变
'''
            text_1_x_5_text = \
'''适用于
ConstantLR中total_iters，达到total_iters时，每一次训练加一次total_iters，学习率将返回成原设定学习率
ConstantLR中total_iters轮内将学习率乘以常数因子
LinearLR中线性改变每个参数组的学习率，直到训练次数达到预定义的值total_iters
'''
            text_1_x_6_text = \
'''适用于
LinearLR中start_factor，在开始时，学习率的值，默认值：1/3"
'''
            text_1_x_11_text = \
'''适用于
CosineAnnealingLR中eta_min，最小学习率值
CyclicLR中base_lr，学习率最小值，也就是学习率在循环过程中能够达到的最小值
'''
            text_1_x_12_text = \
'''适用于
CyclicLR中max_lr，学习率最大值，也就是学习率在循环过程中能够达到的最大值
'''
            text_1_x_13_text = \
'''适用于
CyclicLR中step_size_up，在一个周期内，学习率从 base_lr 增加到 max_lr 所需的步数，默认值：2000
'''
            text_1_x_14_text = \
'''适用于
CyclicLR中mode，决定学习率变化的模式
CyclicLR中mode可选：
1.triangular: 学习率在 base_lr 和 max_lr 之间以线性方式上升和下降
2.triangular2: 与 'triangular' 类似，但每个周期 max_lr 减半
3.exp_range: 学习率按照指数方式衰减
默认值:triangular
'''
            text_1_x_15_text = \
'''适用于
CyclicLR中scale_fn，自定义衰减策略，若指定，则忽略mode
'''
            text_1_x_16_text = \
'''适用于
CyclicLR中scale_mode，决定在exp_range模式下如何应用 gamma 进行学习率缩放
CyclicLR中scale_mode可选:
1.cycle: gamma 在每个周期末进行缩放
2.iterations: gamma 在每次迭代后进行缩放
默认值:cycle
'''
            text_1_x_17_text = \
'''适用于
CyclicLR中cycle_momentum，决定是否在学习率循环时调整动量
CyclicLR中cycle_momentum可选:
1.True: 当学习率增加时，动量减少；学习率减少时，动量增加
2.False: False
'''
            text_1_x_18_text = \
'''适用于
CyclicLR中base_momentum，动量的最低值，也就是动量在循环过程中能够达到的最小值
CyclicLR中base_momentum在每个周期的最低点时，动量降低到 base_momentum
默认值: 若 cycle_momentum 为 True，必须指定
'''
            text_1_x_19_text = \
'''适用于
CyclicLR中max_momentum，动量的最高值，也就是动量在循环过程中能够达到的最大值
CyclicLR中max_momentum在每个周期的最高点时，动量上升到 max_momentum。
默认值: 若 cycle_momentum 为 True，必须指定
'''
            ToolTip(text_1_x_0,text="学习率调节器在何时开始\n若为1，从头开始\n若不输入，默认为1")
            ToolTip(text_1_x_2, text=text_1_x_2_text)
            ToolTip(text_1_x_4,text=text_1_x_4_text)
            ToolTip(text_1_x_5,text=text_1_x_5_text)
            ToolTip(text_1_x_6,text=text_1_x_6_text)
            ToolTip(text_1_x_7,text="适用于\nLinearLR中end_factor，在结束时，学习率的值，默认值：1.0")
            ToolTip(text_1_x_8,text="适用于\nLinearLR中学习率衰减率变为end_factor时的训练次数，默认值：5")
            ToolTip(text_1_x_9,text="适用于\nPolynomialLR中power，多项式的幂，默认值：1.0")
            ToolTip(text_1_x_10,text="适用于\nCosineAnnealingLR中T_max，最大迭代次数")
            ToolTip(text_1_x_11,text=text_1_x_11_text)
            ToolTip(text_1_x_12,text=text_1_x_12_text)
            ToolTip(text_1_x_13,text=text_1_x_13_text)
            ToolTip(text_1_x_14,text=text_1_x_14_text)
            ToolTip(text_1_x_15,text=text_1_x_15_text)
            ToolTip(text_1_x_16,text=text_1_x_16_text)
            ToolTip(text_1_x_17, text=text_1_x_17_text)
            ToolTip(text_1_x_18, text=text_1_x_18_text)
            ToolTip(text_1_x_19, text=text_1_x_19_text)


        menu_bar = tk.Menu(window___)
        window___.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="上一步", menu=file_menu)
        menu_bar.add_command(label="下一步",command=lambda: ())

        def grid():
            f0.grid(column=0, row=0,padx=10,pady=10)
            f3.grid(column=1, row=0,padx=10,pady=10)
            f1.grid(column=0, row=1,padx=10,pady=10)
            f2.grid(column=1, row=1,padx=10,pady=10)
            sep0.grid(column=0, row=2, pady=30, columnspan=1)
            text_0_x_0.grid(column=0, row=0,padx=10,pady=10)
            text_0_x_1.grid(column=0, row=1, padx=10, pady=10)
            text_0_x_2.grid(column=0, row=2, padx=10, pady=10)
            text_0_x_3.grid(column=0, row=3, padx=10, pady=10)
            text_0_x_4.grid(column=0, row=4, padx=10, pady=10)
            text_0_x_e_0.grid(column=1, row=0,padx=10,pady=10)
            text_0_x_e_1.grid(column=1, row=1,padx=10,pady=10)
            text_0_x_e_2.grid(column=1, row=2,padx=10,pady=10)
            text_0_x_e_3.grid(column=1, row=3,padx=10,pady=10)
            text_0_x_e_4.grid(column=1, row=4,padx=10,pady=10)

        grid()
        
    @staticmethod
    def simple_window():
        pass

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable
def gadget():

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def regression():
        list_language_path = os.path.join(DATA_FILE_PATH, "regression-list-language-path")
        regression_data_path = os.path.join(DATA_FILE_PATH, "regression_data.json")
        temp_list = []
        temp_list_2 = []
        selected_index = 0
        selected_index_2 = 0
        selected_index_3 = 0
        combo4_text = 0
        combo5_text = 0
        language = "英"
        regression_data = {
            "特征缩放":"0",
            "损失函数":"0",
            "优化方法":"0",
            "学习率调度器":"0",
            "使用硬件":"0"
        }

        def regression_data_save():
            with open(regression_data_path, 'w', encoding='utf-8') as file:
                json.dump(regression_data, file, indent=4)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def regression_data_load():
            nonlocal selected_index,selected_index_2,selected_index_3,combo4_text,combo5_text

            if not os.path.exists(regression_data_path):
                regression_data_save()
            else:
                try:
                    with open(regression_data_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        selected_index = int(data["特征缩放"])
                        selected_index_2 = int(data["损失函数"])
                        selected_index_3 = int(data["优化方法"])
                        combo4_text = int(data["学习率调度器"])
                        combo5_text = int(data["使用硬件"])
                except Exception as e:
                    messagebox.showerror("错误", f"发生错误: {e}")
                    regression_data_save()

        regression_data_load()

        def list_language_save_path():
            with open(list_language_path, 'w', encoding='utf-8') as file:
                file.write(language)

        def list_language_load_path():
            try:
                with open(list_language_path, 'r', encoding='utf-8') as file:
                    return file.read()
            except FileNotFoundError:
                    return None

        def csv_path():
            data_path = filedialog.askopenfilename(parent=window_, defaultextension="d",
                                               filetypes=[("csv-utf-8", "*.csv")])
            if data_path:
                temp_list.clear()
                temp_list.append(data_path)
                text_1_0.delete(0, END)
                ToolTip(wb1, text=f"已导入数据{data_path}")
                text_1_0.insert(END, data_path)
            else:
                pass

        def csv_save_path():
            data_path = filedialog.asksaveasfilename(parent=window_,defaultextension=".joblib",filetypes=[("Joblib files", "*.joblib")])
            temp_list_2.clear()
            temp_list_2.append(data_path)
            text_1_1.delete(0, END)
            ToolTip(wb2, text=f"已定义保存数据位置{data_path}")
            text_1_1.insert(END, data_path)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,PyShadowingBuiltins
        def test_input(input):
            if re.match(r'^\d+,\d+$|^\d+，\d+$', input):
                if temp_list:
                    input_columns = LinearRegression.FeatureScaling.extract_columns(input)
                    data = LinearRegression.FeatureScaling.load_data(temp_list[0], input_columns)
                    messagebox.showinfo("测试", message=f"特征数据列：{data.columns.tolist()}\n特征数量：{len(data.columns.tolist())}", parent=window_)
                else:
                    messagebox.showerror("错误", message="错误，没有文件", parent=window_)
            elif input == "":
                messagebox.showerror("错误", message="错误，未输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2", parent=window_)
            else:
                messagebox.showerror("错误", message="输入错误，请勿输入不形如0,0的输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2", parent=window_)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def test_output(output):
            if re.match(r'^\d+,\d+$|^\d+，\d+$', output):
                if temp_list:
                    input_columns = LinearRegression.FeatureScaling.extract_columns(output)
                    data = LinearRegression.FeatureScaling.load_data(temp_list[0], input_columns)
                    messagebox.showinfo("测试", message=f"目标数据列：{data.columns.tolist()}\n目标数量：{len(data.columns.tolist())}", parent=window_)
                else:
                    messagebox.showerror("错误", message="错误，没有文件", parent=window_)
            elif output == "":
                messagebox.showerror("错误", message="错误，未输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2", parent=window_)
            else:
                messagebox.showerror("错误", message="输入错误，请勿输入不形如0,0的输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2", parent=window_)

        def update_language(lang):
            nonlocal language, selected_index,selected_index_2,selected_index_3
            if language == "英":
                list_ = ["min-max_normalization",
                     "mean_normalization",
                     "max_abs_normalization",
                     "z-score_normalization",
                     "robust_standardization"]

                list_2 = ["mean_squared_error",
                          "mean_absolute_error",
                          "huber_loss"]

                list_3 = ["batch_GD",
                          "stochastic_GD",
                          "mini-batch_GD"]


            else:
                list_ = ["最大最小值归一化",
                     "均值归一化",
                     "最大绝对值归一化",
                     "Z-Score标准化",
                     "稳健标准化"]

                list_2 = ["均方误差",
                          "绝对误差",
                          "Huber损失"]

                list_3 = ["批量梯度下降",
                          "随机梯度下降",
                          "小批量梯度下降"]

            selected_index = list_.index(combo.get())
            selected_index_2 = list_2.index(combo2.get())
            selected_index_3 = list_3.index(combo3.get())

            language = lang
            list_language_save_path()
            update_combo_list()
            update_combo_2_list()
            update_combo_3_list()

        def update_combo_list():
            options = {
                "英": ["min-max_normalization",
                   "mean_normalization",
                   "max_abs_normalization",
                   "z-score_normalization",
                   "robust_standardization"],
                "中": ["最大最小值归一化",
                   "均值归一化",
                   "最大绝对值归一化",
                   "Z-Score标准化",
                   "稳健标准化"]
            }

            new_values = options.get(language, options["英"])

            combo.config(values=new_values)
            combo.set(new_values[selected_index])

        def update_combo_2_list():
            options = {
                "英": ["mean_squared_error",
                      "mean_absolute_error",
                      "huber_loss"],

                "中": ["均方误差",
                      "绝对误差",
                      "Huber损失"
                   ]
                   }

            new_values = options.get(language, options["英"])
            combo2.config(values=new_values)
            combo2.set(new_values[selected_index_2])

        def update_combo_3_list():
            options = {
                "英": ["batch_GD",
                       "stochastic_GD",
                       "mini-batch_GD",
                       #"Adam",
                       #"RMSprop",
                       #"Adagrad",
                       #"AdamW",
                       #"NAdam",
                       #"Adadelta"
                       ],

                "中": ["批量梯度下降",
                       "随机梯度下降",
                       "小批量梯度下降"]
                   }
            new_values = options.get(language, options["英"])
            combo3.config(values=new_values)
            combo3.set(new_values[selected_index_3])

        def update_combo_4_list():
            list_4 = [
                "None",
                "LambdaLR",
                "StepLR",
                "MultiStepLR",
                "ExponentialLR",
                "CosineAnnealingLR",
                "ReduceLROnPlateau",
                "CyclicLR",
                "OneCycleLR",
                "CosineAnnealingWarmRestarts",
                "PolynomialLR",
                "ConstantLR",
                "ChainedScheduler",
                "SequentialLR"
                ]
            combo4.config(values=list_4)
            combo4.set(list_4[combo4_text])

        def update_combo_5_list():
            list_5 = [
                "GPU",
                "CPU",
                "强制CPU操作Pytorch"
            ]
            combo5.config(values=list_5)
            combo5.set(list_5[combo5_text])

        language = list_language_load_path() or "英"

        window_ = ttk.Toplevel()
        window_.title("线性回归")
        window_.iconbitmap(ICON_PATH)

        menu_bar = tk.Menu(window_)
        window_.config(menu=menu_bar)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def whether_path(temp_list):
            if not temp_list:
                messagebox.showinfo("测试", message="没有数据文件", parent=window_)
            else:
                StartTrainingFrontWindow(window_, combo5, combo4, temp_list_2, temp_list)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="语言", menu=file_menu)
        menu_bar.add_cascade(label="使用模型", menu=file_menu)
        menu_bar.add_command(label="开始训练", command=lambda: whether_path(temp_list))
        file_menu.add_command(label="中文", command=lambda: update_language("中"))
        file_menu.add_command(label="英文", command=lambda: update_language("英"))

        f0 = ttk.Frame(window_)
        f0.grid(row=0, column=0, sticky='w')
        f1 = ttk.Frame(window_)
        f1.grid(row=0,column=1, sticky='nw')

        wb1 = ttk.Button(f0, text="导入文件", style="link", command=csv_path)
        wb2 = ttk.Button(f0, text="保存模型", style="link", command=csv_save_path)
        text_1_0 = ttk.Entry(f0)
        text_1_0.insert(END, "没有文件")
        text_1_1 = ttk.Entry(f0)
        text_1_1.insert(END, "没有位置")
        ToolTip(wb1, text="需导入数据用于模型训练")
        ToolTip(wb2, text="若为空，将不保存模型")
        text_0_x_0 = ttk.Label(f1, text="特征数据")
        text_0_x_1 = ttk.Label(f1, text="目标数据")
        text_0_x_e_0 = ttk.Entry(f1)
        text_0_x_e_1 = ttk.Entry(f1)
        text_0_x_e_0_wb0 = ttk.Button(f1, text="测试特征数据位置", style="link", command=lambda: test_input(text_0_x_e_0.get()))
        text_0_x_e_1_wb0 = ttk.Button(f1, text="测试目标数据位置", style="link", command=lambda: test_output(text_0_x_e_1.get()))

        text_0 = ttk.Label(f0, text="特征缩放")
        text_2 = ttk.Label(f0, text="损失函数")
        text_3 = ttk.Label(f0, text="优化方法")
        text_4 = ttk.Label(f0, text="学习率调度器【未完成】")
        text_5 = ttk.Label(f0, text="学习率")
        text_6 = ttk.Label(f0, text="训练次数")
        text_7 = ttk.Label(f0, text="使用硬件")

        combo = ttk.Combobox(f0, state="readonly")
        combo2 = ttk.Combobox(f0, state="readonly")
        combo3 = ttk.Combobox(f0, state="readonly")
        combo4 = ttk.Combobox(f0, state="readonly")
        text_e = ttk.Entry(f0)
        text_e_1 = ttk.Entry(f0)
        combo5 = ttk.Combobox(f0, state="readonly")

        def f0_grid():
            text_1_0.grid(column=1, row=0, padx=10, pady=10)
            wb1.grid(column=0, row=0, padx=10, pady=10)
            text_1_1.grid(column=1, row=1, padx=10, pady=10)
            wb2.grid(column=0, row=1, padx=10, pady=10)
            text_0.grid(row=2, column=0, padx=10, pady=10)
            combo.grid(row=2, column=1, padx=10, pady=10)
            text_2.grid(column=0, row=3, padx=10, pady=10)
            combo2.grid(row=3, column=1, padx=10, pady=10)
            text_3.grid(column=0, row=4, padx=10, pady=10)
            combo3.grid(row=4, column=1, padx=10, pady=10)
            text_4.grid(column=0, row=5, padx=10, pady=10)
            combo4.grid(row=5, column=1, padx=10, pady=10)
            text_5.grid(column=0, row=6, padx=10, pady=10)
            text_e.grid(row=6, column=1, padx=10, pady=10)
            text_6.grid(column=0, row=7, padx=10, pady=10)
            text_e_1.grid(row=7, column=1, padx=10, pady=10)
            text_7.grid(column=0, row=8, padx=10, pady=10)
            combo5.grid(column=1, row=8, padx=10, pady=10)

        def f1_grid():
            text_0_x_0.grid(column=0, row=0, padx=10, pady=10)
            text_0_x_1.grid(column=0, row=1, padx=10, pady=10)
            text_0_x_e_0.grid(column=1, row=0, padx=10, pady=10)
            text_0_x_e_1.grid(column=1, row=1, padx=10, pady=10)
            text_0_x_e_0_wb0.grid(column=2, row=0, pady=10)
            text_0_x_e_1_wb0.grid(column=2, row=1, pady=10)

        def f1_tool_tip():
            ToolTip(text_0_x_e_0, text="输入特征数据在csv文件中的位置，若不输入，默认0,0\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2")
            ToolTip(text_0_x_e_1, text="输入目标数据在csv文件中的位置，若不输入，默认1,1\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2")

        f0_grid()
        f1_grid()
        f1_tool_tip()

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_tooltip_text():
            match combo.get():
                case "最大最小值归一化"|"min-max_normalization":
                    text_ = '将数据缩放到 [0, 1]范围'
                    regression_data["特征缩放"] = "0"
                case "均值归一化"|"mean_normalization":
                    text_ = '将数据缩放到  [-1, 1]范围'
                    regression_data["特征缩放"] = "1"
                case "最大绝对值归一化"|"max_abs_normalization":
                    text_ = '将数据缩放到 [-1, 1] 范围内，但保留了数据的稀疏性'
                    regression_data["特征缩放"] = "2"
                case "Z-Score标准化"|"z-score_normalization":
                    text_ = '将数据转化为标准正态分布'
                    regression_data["特征缩放"] = "3"
                case "稳健标准化"|"robust_standardization":
                    text_ = '对异常值具有较好的鲁棒性，不易受极端值的影响'
                    regression_data["特征缩放"] = "4"

            regression_data_save()
            ToolTip(combo, text=text_)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_tooltip_text_2():
            match combo2.get():
                case "均方误差"|"mean_squared_error":
                    text_ = "对大误差敏感"
                    regression_data["损失函数"] = "0"
                case "绝对误差"|"mean_absolute_error":
                    text_ = "对异常值鲁棒"
                    regression_data["损失函数"] = "1"
                case "Huber损失":
                    text_ = "均方误差和绝对误差之间"
                    regression_data["损失函数"] = "2"
                case "huber_loss":
                    text_ = "MSE和MAE之间"
                    regression_data["损失函数"] = "3"

            regression_data_save()
            ToolTip(combo2, text=text_)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_tooltip_text_3():
            match combo3.get():
                case "批量梯度下降"|"batch_GD":
                    text_ ='一定能够得到全局最优解\n训练样本过多时很慢'
                    regression_data["梯度下降"] = "0"
                case "随机梯度下降"|"stochastic_GD":
                    text_ = "准确度下降\n可能会收敛到局部最优"
                    regression_data["梯度下降"] = "1"
                case "小批量梯度下降"|"mini-batch_GD":
                    text_ = "每次迭代使用batch_size个样本来对参数进行更新\n减小收敛所需要的迭代次数"
                    regression_data["梯度下降"] = "2"

            regression_data_save()
            ToolTip(combo3, text=text_)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_tooltip_text_4():
            match combo4.get():
                case "None":
                    text_ ='使用固定的学习率'
                    regression_data["学习率调度器"] = "0"
                case "LambdaLR":
                    text_ = "根据用户定义的函数对学习率进行更改"
                    regression_data["学习率调度器"] = "1"
                case "StepLR":
                    text_ = "每隔一定的epoch数将学习率乘以一个预定的衰减因子"
                    regression_data["学习率调度器"] = "2"
                case "MultiStepLR":
                    text_ = "在预定的epoch列表中每次到达时将学习率乘以一个预定的衰减因子"
                    regression_data["学习率调度器"] = "3"
                case "ExponentialLR":
                    text_ = "每个epoch将学习率按照一个固定的指数衰减"
                    regression_data["学习率调度器"] = "4"
                case "CosineAnnealingLR":
                    text_ = "学习率在训练期间根据余弦曲线衰减"
                    regression_data["学习率调度器"] = "5"
                case "ReduceLROnPlateau":
                    text_ = "当指标停止改进时减少学习率"
                    regression_data["学习率调度器"] = "6"
                case "CyclicLR":
                    text_ = "学习率在两个边界之间循环变化"
                    regression_data["学习率调度器"] = "7"
                case "OneCycleLR":
                    text_ = "在单个周期内调整学习率，以适应较大的学习率"
                    regression_data["学习率调度器"] = "8"
                case "CosineAnnealingWarmRestarts":
                    text_ = "使用余弦退火和周期性重启来调整学习率"
                    regression_data["学习率调度器"] = "9"
                case "PolynomialLR":
                    text_ = "使用多项式衰减的方式调整学习率"
                    regression_data["学习率调度器"] = "10"
                case "ConstantLR":
                    text_ = "在预定的steps数内保持学习率不变"
                    regression_data["学习率调度器"] = "11"
                case "ChainedScheduler":
                    text_ = "按顺序连接多个调度器"
                    regression_data["学习率调度器"] = "12"
                case "SequentialLR":
                    text_ = "将多种衰减方式以串联的方式进行组合"
                    regression_data["学习率调度器"] = "13"

            regression_data_save()
            ToolTip(combo4, text=text_)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_tooltip_text_5():
            match combo5.get():
                case "GPU":
                    text_ = '若用户设备不支持CUDA，将使用DirectML\nDirectML时可能会有不支持的方法，导致返回cpu进行\n使用Pytorch库\n若用户设备都不支持，将返回cpu进行\n返回cpu进行将使用scikit-learn库'
                    regression_data["使用硬件"] = "0"
                case "CPU":
                    text_ = '若使用cpu将只需要数据，其它值不需填写\n使用scikit-learn库'
                    regression_data["使用硬件"] = "1"
                case "强制CPU操作Pytorch":
                    text_ = '这将强制使用cpu\n使用Pytorch库'
                    regression_data["使用硬件"] = "2"

            regression_data_save()
            ToolTip(combo5, text=text_)

        def combo_():
            combo.bind("<<ComboboxSelected>>", lambda event: change_tooltip_text())
            update_combo_list()

            combo2.bind("<<ComboboxSelected>>", lambda event: change_tooltip_text_2())
            update_combo_2_list()

            combo3.bind("<<ComboboxSelected>>", lambda event: change_tooltip_text_3())
            update_combo_3_list()

            combo4.bind("<<ComboboxSelected>>", lambda event: change_tooltip_text_4())
            update_combo_4_list()

            combo5.bind("<<ComboboxSelected>>", lambda event: change_tooltip_text_5())
            update_combo_5_list()

        combo_()
        change_tooltip_text()
        change_tooltip_text_2()
        change_tooltip_text_3()
        change_tooltip_text_4()
        change_tooltip_text_5()

    def triangle():
        pass

    def picture():
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

                    if (not entry1_value.isdigit() or 0 > int(entry1_value) or int(entry1_value) > 225) and entry1_value != "保留原本":
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
                nonlocal rgb,rgb_
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
                nonlocal rgb,rgb_
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
                nonlocal rgb,rgb_
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
                nonlocal rgb,rgb_
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
                    rgb = (color[0],color[1],color[2])
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
                    rgb_ = (color[0],color[1],color[2])
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

            png_path = filedialog.askopenfilenames(title='请选择需要颜色转换的图片', filetypes=[("PNG", "*.PNG")],parent=window__)

            # noinspection PyPep8Naming
            def PNG():
                if png_path:
                    window__.focus_set()
                    window__.wm_attributes('-disabled', 1)
                    icon.notify("已开始导入，请耐心等待\n导入期间，当前窗口将被禁用\n强制退出<右Shift>", "Lightweight text editor")
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
            all_path = filedialog.askopenfilenames(title='请选择需要格式转换的图片', filetypes=[("All Images", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff")],parent=window__)

        def sprites():
            SpriteSheetMaker()

        window_ = ttk.Toplevel()
        window_.title("图片操作")
        window_.iconbitmap(ICON_PATH)
        wb1 = ttk.Button(window_, text="颜色转换", style=OUTLINE, command=color)
        wb1.grid(column=0,row=0,padx=10,pady=10)
        wb2 = ttk.Button(window_, text="格式转换", style=OUTLINE, command=format_)
        wb2.grid(column=1,row=0,padx=10,pady=10)
        wb3 = ttk.Button(window_, text="精灵图制作", style=OUTLINE, command=sprites)
        wb3.grid(column=2,row=0,padx=10,pady=10)


    window = ttk.Toplevel(str(root))
    window.title("轻量记事本-小工具")
    window.iconbitmap(ICON_PATH)
    b1 = ttk.Button(window, text="小六壬", style=OUTLINE, command=lambda: xiao_liu_ren_window(root, icon, font_style))
    b1.grid(column=0,row=0,padx=10,pady=10)
    b2 = ttk.Button(window, text="紫微斗数", style=OUTLINE, command=z)
    b2.grid(column=1,row=0,padx=10,pady=10)
    b3 = ttk.Button(window, text="机器学习-回归问题", style=OUTLINE, command=regression)
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
    v2 = int(t_load(D_PATH) or 1)
    v3 = int(t_load(E_PATH) or 0)
    v4 = int(t_load(F_PATH) or 0)
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
    font_style1 = tk_font.Font(family="宋体", size=12)
    font_style2 = tk_font.Font(family="等线", size=12)
    font_style3 = tk_font.Font(family="黑体", size=12)
    font_style = None
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
    if v2 % 2 == 1:
        font_style = font_style1
    elif v3 % 2 == 1:
        font_style = font_style2
    elif v4 % 2 == 1:
        font_style = font_style3

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
                          yscrollcommand=scrollbar.set, font=font_style)
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
        1: lambda: (root.withdraw(), xiao_liu_ren_window(root, icon, font_style)),    }

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