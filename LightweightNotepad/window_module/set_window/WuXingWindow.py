from tkinter import messagebox

import ttkbootstrap as ttk

from DownBoxModify import DownBoxModify
from function.ProjectFunctions import window_init
from function.ProjectPathVariables import XLR_WU_XING_JSON, XLR_DATA_WU_XING_PATH


class WuXingWindow:
    def __init__(self,main_window):
        down_dox_values_group_main = []
        down_dox_group_main = []

        down_box_group_1 = ["单输入","三输入","关键单字单输入","关键单字三输入"]
        down_dox_values_group_main.append(down_box_group_1)

        window = ttk.Toplevel(str(main_window))
        window_init(window, main_window, "五行起卦具体设置")
        window.resizable(False, False)

        text0 = ttk.Label(window, text="五行输入")
        down_box_1 = ttk.Combobox(master=window, values=down_box_group_1, state="readonly")
        down_box_1.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main)
                        .for_modify()
                        )
        down_dox_group_main.append(down_box_1)

        messagebox.showerror("错误", message=f"{XLR_WU_XING_JSON}", parent=window) if isinstance(XLR_WU_XING_JSON,
                                                                                      Exception) else DownBoxModify(XLR_WU_XING_JSON,
                                                                            XLR_DATA_WU_XING_PATH,
                                                                            down_dox_values_group_main,
                                                                            down_dox_group_main).for_set()

        text0.grid(column=0, row=0, padx=5, pady=5)
        down_box_1.grid(row=0, column=1, padx=10, pady=10)