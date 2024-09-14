import json
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from function.ProjectVariables import ICON_PATH, DATA_FILE_PATH
from CustomToolTip import CustomToolTip as ToolTip
from module import LinearRegression
from window_module.StartTrainingFrontWindow import StartTrainingFrontWindow


# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
def regression(root_main):
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
        "特征缩放": "0",
        "损失函数": "0",
        "优化方法": "0",
        "学习率调度器": "0",
        "使用硬件": "0"
    }

    def regression_data_save():
        with open(regression_data_path, 'w', encoding='utf-8') as file:
            json.dump(regression_data, file, indent=4)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def regression_data_load():
        nonlocal selected_index, selected_index_2, selected_index_3, combo4_text, combo5_text

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
        data_path = filedialog.asksaveasfilename(parent=window_, defaultextension=".joblib",
                                                 filetypes=[("Joblib files", "*.joblib")])
        temp_list_2.clear()
        temp_list_2.append(data_path)
        text_1_1.delete(0, END)
        ToolTip(wb2, text=f"已定义保存数据位置{data_path}")
        text_1_1.insert(END, data_path)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,PyShadowingBuiltins,DuplicatedCode
    def test_input(input):
        if re.match(r'^\d+,\d+$|^\d+，\d+$', input):
            if temp_list:
                input_columns = LinearRegression.FeatureScaling.extract_columns(input)
                data = LinearRegression.FeatureScaling.load_data(temp_list[0], input_columns)
                messagebox.showinfo("测试",
                                    message=f"特征数据列：{data.columns.tolist()}\n特征数量：{len(data.columns.tolist())}",
                                    parent=window_)
            else:
                messagebox.showerror("错误", message="错误，没有文件", parent=window_)
        elif input == "":
            messagebox.showerror("错误",
                                 message="错误，未输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2",
                                 parent=window_)
        else:
            messagebox.showerror("错误",
                                 message="输入错误，请勿输入不形如0,0的输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2",
                                 parent=window_)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
    def test_output(output):
        if re.match(r'^\d+,\d+$|^\d+，\d+$', output):
            if temp_list:
                input_columns = LinearRegression.FeatureScaling.extract_columns(output)
                data = LinearRegression.FeatureScaling.load_data(temp_list[0], input_columns)
                messagebox.showinfo("测试",
                                    message=f"目标数据列：{data.columns.tolist()}\n目标数量：{len(data.columns.tolist())}",
                                    parent=window_)
            else:
                messagebox.showerror("错误", message="错误，没有文件", parent=window_)
        elif output == "":
            messagebox.showerror("错误",
                                 message="错误，未输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2",
                                 parent=window_)
        else:
            messagebox.showerror("错误",
                                 message="输入错误，请勿输入不形如0,0的输入值\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2",
                                 parent=window_)

    def update_language(lang):
        nonlocal language, selected_index, selected_index_2, selected_index_3
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
                   # "Adam",
                   # "RMSprop",
                   # "Adagrad",
                   # "AdamW",
                   # "NAdam",
                   # "Adadelta"
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

    window_ = ttk.Toplevel(root_main)
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
    f1.grid(row=0, column=1, sticky='nw')

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
    text_0_x_e_0_wb0 = ttk.Button(f1, text="测试特征数据位置", style="link",
                                  command=lambda: test_input(text_0_x_e_0.get()))
    text_0_x_e_1_wb0 = ttk.Button(f1, text="测试目标数据位置", style="link",
                                  command=lambda: test_output(text_0_x_e_1.get()))

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
        ToolTip(text_0_x_e_0,
                text="输入特征数据在csv文件中的位置，若不输入，默认0,0\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为特征：0,2\n2.获取二列的数据为特征：2,2\n3.获取第二列到第三列的数据为特征：1,2")
        ToolTip(text_0_x_e_1,
                text="输入目标数据在csv文件中的位置，若不输入，默认1,1\n方法：列数范围,列数范围\n第一列为0，依次类推\n示例：\n1.获取第一列到第三列的数据为目标：0,2\n2.获取二列的数据为目标：2,2\n3.获取第二列到第三列的数据为目标：1,2")

    f0_grid()
    f1_grid()
    f1_tool_tip()

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def change_tooltip_text():
        match combo.get():
            case "最大最小值归一化" | "min-max_normalization":
                text_ = '将数据缩放到 [0, 1]范围'
                regression_data["特征缩放"] = "0"
            case "均值归一化" | "mean_normalization":
                text_ = '将数据缩放到  [-1, 1]范围'
                regression_data["特征缩放"] = "1"
            case "最大绝对值归一化" | "max_abs_normalization":
                text_ = '将数据缩放到 [-1, 1] 范围内，但保留了数据的稀疏性'
                regression_data["特征缩放"] = "2"
            case "Z-Score标准化" | "z-score_normalization":
                text_ = '将数据转化为标准正态分布'
                regression_data["特征缩放"] = "3"
            case "稳健标准化" | "robust_standardization":
                text_ = '对异常值具有较好的鲁棒性，不易受极端值的影响'
                regression_data["特征缩放"] = "4"

        regression_data_save()
        ToolTip(combo, text=text_)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def change_tooltip_text_2():
        match combo2.get():
            case "均方误差" | "mean_squared_error":
                text_ = "对大误差敏感"
                regression_data["损失函数"] = "0"
            case "绝对误差" | "mean_absolute_error":
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
            case "批量梯度下降" | "batch_GD":
                text_ = '一定能够得到全局最优解\n训练样本过多时很慢'
                regression_data["梯度下降"] = "0"
            case "随机梯度下降" | "stochastic_GD":
                text_ = "准确度下降\n可能会收敛到局部最优"
                regression_data["梯度下降"] = "1"
            case "小批量梯度下降" | "mini-batch_GD":
                text_ = "每次迭代使用batch_size个样本来对参数进行更新\n减小收敛所需要的迭代次数"
                regression_data["梯度下降"] = "2"

        regression_data_save()
        ToolTip(combo3, text=text_)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
    def change_tooltip_text_4():
        match combo4.get():
            case "None":
                text_ = '使用固定的学习率'
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