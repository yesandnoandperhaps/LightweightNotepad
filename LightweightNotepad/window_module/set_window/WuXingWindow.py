from tkinter import messagebox
from tkinter.ttk import Separator
import re
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ProjectDictionaryVariables import XLR_DATA_WU_XING
from function import JsonFile
from function.CustomToolTip import CustomToolTip as ToolTip
from function.ProjectDictionaryVariables import UTC_TIME
from function.ProjectFunctions import save, t_load, var_save, utc, window_init, window_closes, t_s, t_s_
from function.ProjectInitialVariables import onandoff, circular, divide_up, size__, v,v2,v3,v4,var2_num_w_4_3,var3_num_w_4_3,var_num_w_4_3
from function.ProjectPathVariables import R_PATH, S_PATH, T_PATH, W_PATH, X_PATH, Z_PATH, AA_PATH, AB_PATH, \
    W_ROOT2_C_VAR_2_PATH, XLR_DATA_PATH, XLR_JSON, XLR_WU_XING_JSON, XLR_DATA_WU_XING_PATH


class WuXingWindow:
    def __init__(self,main_window,down_box_3):
        if down_box_3.get() == "五行起卦":
            down_box_group_1 = ["单输入","三输入","关键单字单输入","关键单字三输入"]
            window = ttk.Toplevel(str(main_window))
            window_init(window, main_window, "五行起卦具体设置")
            window.resizable(False, False)

            text0 = ttk.Label(window, text="五行输入")
            down_box_1 = ttk.Combobox(master=window, values=down_box_group_1, state="readonly")
            down_box_1.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            text0.grid(column=0, row=0, padx=5, pady=5)
            down_box_1.grid(row=0, column=1, padx=10, pady=10)

            JsonFile.File.dict_save(XLR_DATA_WU_XING_PATH, XLR_WU_XING_JSON.file_dict)
