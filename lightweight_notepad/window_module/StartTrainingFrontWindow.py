import idlelib.colorizer as idc
import idlelib.percolator as idp
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Separator
import ttkbootstrap as ttk

from ttkbootstrap.tooltip import ToolTip
from function.variables import ProjectCapabilityVariables
from function.variables.ProjectPathVariables import ICON_PATH

# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,DuplicatedCode
class StartTrainingFrontWindow:
    def __init__(self, window, combo5, combo4, temp_list_2, temp_list):
        self.temp_list = temp_list
        self.whether_save = False
        self.FONT_STYLE = ProjectCapabilityVariables.font_set()
        if not temp_list_2:
            result = messagebox.askyesno("线性回归", "请等待-本次计算将不会保存模型，是否需要进行计算后预测",
                                         parent=window)
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
                messagebox.showerror("错误", "未定义lr_lambda", parent=window)
                return
            # noinspection PyUnusedLocal
            lr_lambda = local_vars['lr_lambda']
        except Exception as e:
            messagebox.showerror("错误", str(e), parent=window)

    def lambda_lr_window(self):
        window___ = ttk.Toplevel()
        window___.title("线性回归-LambdaLR-编写函数")
        window___.iconbitmap(ICON_PATH)
        scrollbar = ttk.Scrollbar(window___, style="round")
        scrollbar.grid(row=1, column=1, sticky="ns")
        text_widget = tk.Text(window___, wrap="word",
                              yscrollcommand=scrollbar.set, font=self.FONT_STYLE)
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
        text_0_x_0 = ttk.Label(f0, text="动量")
        text_0_x_1 = ttk.Label(f0, text="动量衰减")
        text_0_x_2 = ttk.Label(f0, text="权重衰减")
        text_0_x_3 = ttk.Label(f0, text="Nesterov动量")
        text_0_x_4 = ttk.Label(f0, text="绘制损失值")

        text_0_x_e_0 = ttk.Entry(f0)
        text_0_x_e_1 = ttk.Entry(f0)
        text_0_x_e_2 = ttk.Entry(f0)
        text_0_x_e_3 = ttk.Combobox(f0, values=["True", "False"], state="readonly")
        text_0_x_e_4 = ttk.Combobox(f0, values=["True", "False"], state="readonly")

        sep0 = Separator(window___, orient='horizontal')

        text_1_x_0 = ttk.Label(f1, text="开始值")
        # noinspection PyUnusedLocal
        text_1_x_1 = ttk.Label(f1, text="绘制学习率")
        text_1_x_2 = ttk.Label(f1, text="因子")
        text_1_x_4 = ttk.Label(f1, text="衰减周期")
        text_1_x_5 = ttk.Label(f1, text="恢复周期")
        text_1_x_6 = ttk.Label(f1, text="开始学习率")
        text_1_x_7 = ttk.Label(f1, text="结束学习率")
        text_1_x_8 = ttk.Label(f1, text="衰减率为1时循环次数")
        text_1_x_9 = ttk.Label(f1, text="多项式的幂")
        text_1_x_10 = ttk.Label(f1, text="最大迭代次数")
        text_1_x_11 = ttk.Label(f2, text="最小学习率")
        text_1_x_12 = ttk.Label(f2, text="最大学习率")
        text_1_x_13 = ttk.Label(f2, text="递增周期中训练迭代次数")
        text_1_x_14 = ttk.Label(f2, text="递增递减变化策略")
        text_1_x_15 = ttk.Label(f2, text="scale_fn")
        text_1_x_16 = ttk.Label(f2, text="scale_mode")
        text_1_x_17 = ttk.Label(f2, text="cycle_momentum")
        text_1_x_18 = ttk.Label(f2, text="每次循环中动量上限")
        text_1_x_19 = ttk.Label(f2, text="每次循环中动量下限")
        # noinspection PyUnusedLocal
        text_1_x_20 = ttk.Label(f3, text="串联方式数")

        # noinspection PyUnusedLocal
        def tool_tip():
            text_1_x_2_text = \
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
            ToolTip(text_1_x_0, text="学习率调节器在何时开始\n若为1，从头开始\n若不输入，默认为1")
            ToolTip(text_1_x_2, text=text_1_x_2_text)
            ToolTip(text_1_x_4, text=text_1_x_4_text)
            ToolTip(text_1_x_5, text=text_1_x_5_text)
            ToolTip(text_1_x_6, text=text_1_x_6_text)
            ToolTip(text_1_x_7, text="适用于\nLinearLR中end_factor，在结束时，学习率的值，默认值：1.0")
            ToolTip(text_1_x_8, text="适用于\nLinearLR中学习率衰减率变为end_factor时的训练次数，默认值：5")
            ToolTip(text_1_x_9, text="适用于\nPolynomialLR中power，多项式的幂，默认值：1.0")
            ToolTip(text_1_x_10, text="适用于\nCosineAnnealingLR中T_max，最大迭代次数")
            ToolTip(text_1_x_11, text=text_1_x_11_text)
            ToolTip(text_1_x_12, text=text_1_x_12_text)
            ToolTip(text_1_x_13, text=text_1_x_13_text)
            ToolTip(text_1_x_14, text=text_1_x_14_text)
            ToolTip(text_1_x_15, text=text_1_x_15_text)
            ToolTip(text_1_x_16, text=text_1_x_16_text)
            ToolTip(text_1_x_17, text=text_1_x_17_text)
            ToolTip(text_1_x_18, text=text_1_x_18_text)
            ToolTip(text_1_x_19, text=text_1_x_19_text)

        menu_bar = tk.Menu(window___)
        window___.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="上一步", menu=file_menu)
        menu_bar.add_command(label="下一步", command=lambda: ())

        def grid():
            f0.grid(column=0, row=0, padx=10, pady=10)
            f3.grid(column=1, row=0, padx=10, pady=10)
            f1.grid(column=0, row=1, padx=10, pady=10)
            f2.grid(column=1, row=1, padx=10, pady=10)
            sep0.grid(column=0, row=2, pady=30, columnspan=1)
            text_0_x_0.grid(column=0, row=0, padx=10, pady=10)
            text_0_x_1.grid(column=0, row=1, padx=10, pady=10)
            text_0_x_2.grid(column=0, row=2, padx=10, pady=10)
            text_0_x_3.grid(column=0, row=3, padx=10, pady=10)
            text_0_x_4.grid(column=0, row=4, padx=10, pady=10)
            text_0_x_e_0.grid(column=1, row=0, padx=10, pady=10)
            text_0_x_e_1.grid(column=1, row=1, padx=10, pady=10)
            text_0_x_e_2.grid(column=1, row=2, padx=10, pady=10)
            text_0_x_e_3.grid(column=1, row=3, padx=10, pady=10)
            text_0_x_e_4.grid(column=1, row=4, padx=10, pady=10)

        grid()

    @staticmethod
    def simple_window():
        pass