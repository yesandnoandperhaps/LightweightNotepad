from tkinter import messagebox

import ttkbootstrap as ttk
from function.CustomToolTip import CustomToolTip as ToolTip

from function.DownBoxModify import DownBoxModify
from function.ProjectFunctions import window_init
from function.variables.ProjectPathVariables import XLR_WU_XING_JSON, XLR_DATA_WU_XING_PATH
from window_module.set_window.RandomNumbersWindow import RandomNumbersWindow


class WuXingWindow:
    def __init__(self,main_window):
        down_dox_values_group_main = []
        down_dox_group_main = []

        down_box_group_0 = ["单输入","三输入","关键单字单输入","关键单字三输入"]
        down_box_group_1 = ["后天","先天","四象数"]
        down_box_group_2 = ["地支阴阳","早晚阴阳","早晚阳阴","自定义"]
        down_box_group_3 = ["阴/阳单数输入取三数","阴阳两数输入取三数"]
        down_box_group_4 = ["阳时取单数，阴时取双数","阳时取双数，阴时取单数"]
        down_box_group_5 = ["小于阴/阳单数/阴阳两数","范围"]
        down_box_group_6 = ["后输入","前输入"]

        down_dox_values_group_main.append(down_box_group_0)
        down_dox_values_group_main.append(down_box_group_1)
        down_dox_values_group_main.append(down_box_group_2)
        down_dox_values_group_main.append(down_box_group_3)
        down_dox_values_group_main.append(down_box_group_4)
        down_dox_values_group_main.append(down_box_group_5)
        down_dox_values_group_main.append(down_box_group_6)

        window = ttk.Toplevel(str(main_window))
        window_init(window, main_window, "五行起卦具体设置")
        window.resizable(False, False)

        text0 = ttk.Label(window, text="五行输入：")
        text1 = ttk.Label(window, text="五行取数：")
        text2 = ttk.Label(window, text="阴阳时问题:")
        text3 = ttk.Label(window, text="单输入问题:")
        text4 = ttk.Label(window, text="单双数问题:")
        text5 = ttk.Label(window, text="取数计算:")
        text6 = ttk.Label(window, text="范围输入:")

        down_box_0 = ttk.Combobox(master=window, values=down_box_group_0, state="readonly")
        down_box_0.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_0)

        down_box_1 = ttk.Combobox(master=window, values=down_box_group_1, state="readonly")
        down_box_1.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_1)

        down_box_2 = ttk.Combobox(master=window, values=down_box_group_2, state="readonly")
        down_box_2.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_2)

        down_box_3 = ttk.Combobox(master=window, values=down_box_group_3, state="readonly")
        down_box_3.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_3)

        ToolTip(down_box_3, text="阴阳两数输入取三数时，阴阳时问题失效\n四象数时，将单数取三数")

        down_box_4 = ttk.Combobox(master=window, values=down_box_group_4, state="readonly")
        down_box_4.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_4)

        down_box_5 = ttk.Combobox(master=window, values=down_box_group_5, state="readonly")
        down_box_5.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_5)

        down_box_6 = ttk.Combobox(master=window, values=down_box_group_6, state="readonly")
        down_box_6.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_box_6.bind("<Button-3>", lambda event: WuXingWindow.transfer(window, down_box_6,13,14))
        down_dox_group_main.append(down_box_6)

        messagebox.showerror("错误", message=f"{XLR_WU_XING_JSON}", parent=window) if isinstance(XLR_WU_XING_JSON,
                                                                                      Exception) else DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main).for_set()
        text0.grid(column=0, row=0, padx=5, pady=5)
        down_box_0.grid(row=0, column=1, padx=10, pady=10)
        text1.grid(column=0, row=1, padx=5, pady=5)
        down_box_1.grid(row=1, column=1, padx=10, pady=10)
        text2.grid(column=0, row=2, padx=5, pady=5)
        down_box_2.grid(row=2, column=1, padx=10, pady=10)
        text3.grid(column=0, row=3, padx=5, pady=5)
        down_box_3.grid(row=3, column=1, padx=10, pady=10)
        text4.grid(column=0, row=3, padx=5, pady=5)
        down_box_4.grid(row=3, column=1, padx=10, pady=10)
        text5.grid(column=0, row=4, padx=5, pady=5)
        down_box_5.grid(row=4, column=1, padx=10, pady=10)
        text6.grid(column=0, row=5, padx=5, pady=5)
        down_box_6.grid(row=5, column=1, padx=10, pady=10)

    @staticmethod
    def transfer(main_window,down_box_3,num1=None,num2=None):
        if down_box_3.get() == "前输入":
            RandomNumbersWindow(main_window,num1,num2,1).event0()