from tkinter import messagebox
from tkinter.ttk import Separator
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from window_module.set_window.set_function.Transfer import Transfer
from function.JsonFile import File
from function.CustomToolTip import CustomToolTip as ToolTip
from function.variables.ProjectDictionaryVariables import UTC_TIME, YONG_MING_TI_LIST
from function.ProjectFunctions import save, t_load, var_save, utc, window_init, window_closes, t_s, t_s_
from function.variables.ProjectInitialVariables import onandoff, circular, divide_up, size__, v,v2,v3,v4
from function.variables.ProjectPathVariables import R_PATH, S_PATH, T_PATH, W_PATH, X_PATH, Z_PATH, AA_PATH, AB_PATH, \
    W_ROOT2_C_VAR_2_PATH, XLR_DATA_PATH, XLR_JSON, B_PATH, YONG_MING_TI_DATA_JSON, YONG_MING_TI_PATH
from function.QuicklyCreate import QuicklyCreate


# noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable

def set_window(root):
    window = ttk.Toplevel(str(root))
    window_init(window,root,"轻量记事本-设置")
    window.resizable(None,None)

    # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
    def w_root1():

        global theme_cbo

        # noinspection SpellCheckingInspection
        def bao_chun():
            p1=v2%2
            p2=v3%2
            p3=v4%2
            #window_close_()
            if p1+p2+p3==1:
                save(theme_cbo.get(),v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3)
            else:
                messagebox.showerror("错误", message="不支持多字体或无字体选择",parent=window)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal
        def change_theme(event):
            theme_cbo_value = theme_cbo.get()
            with open(B_PATH, 'w', encoding='utf-8') as file:
                file.write(theme_cbo_value)
            style.theme_use(theme_cbo_value)

        w_ = ttk.Frame(window)
        w_.grid(row=0,column=0,sticky=W)
        lbl = ttk.Label(w_, text="选择主题:")
        lbl.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        lb2 = ttk.Label(w_, text="选择字体:")
        lb2.grid(column=0,row=1,padx=10,pady=10,ipadx=5)


        window_button_two = ttk.Button(w_, text="返回", style=OUTLINE, command=lambda: window_closes(window,root))
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
        consider_checkbutton2 = ttk.Checkbutton(w2, text="宋体", variable=consider_var_2, command=lambda: t_s(v2), style="round-toggle")
        consider_checkbutton2.grid(column=1,row=1,padx=10,pady=10)

        consider_var_3 = ttk.IntVar()
        if v3 % 2 == 1:
            consider_var_3.set(1)
        else:
            consider_var_3.set(0)
        consider_checkbutton3 = ttk.Checkbutton(w2, text="等线", variable=consider_var_3, command=lambda: t_s(v3), style="round-toggle")
        consider_checkbutton3.grid(column=2,row=1,padx=10,pady=10)

        consider_var_4 = ttk.IntVar()
        if v4 % 2 == 1:
            consider_var_4.set(1)
        else:
            consider_var_4.set(0)
        consider_checkbutton4 = ttk.Checkbutton(w2, text="黑体", variable=consider_var_4, command=lambda: t_s(v4), style="round-toggle")
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
        consider_checkbutton = ttk.Checkbutton(w_2, text="是否关联上一次保存的文件", variable=consider_var, command=lambda: t_s(v), style="round-toggle")
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

        lb5 = ttk.Label(w_3, text="永明体:")
        lb5.grid(column=2, row=0, padx=10, pady=10, ipadx=5, sticky=W)

        w6 = ttk.Frame(w_3)
        w6.grid(row=0,column=3,sticky=W)

        #w6_lb1 = ttk.Label(w6,text="永明体:")
        #w6_lb1.grid(column=0,row=0,padx=10,pady=10,ipadx=5,sticky=W)

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

            match size__:
                case "70MB" | "50MB" | "128MB" | "256MB" | "512MB":
                    combobox1.set(size__)
                case _:
                    combobox1.set("70MB")
                    save(theme_cbo.get(),v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3)

            match divide_up:
                case "等于大文件定义" | "5MB" | "10MB" | "15MB" | "30MB":
                    combobox2.set(divide_up)
                case _:
                    combobox2.set("70MB")
                    save(theme_cbo.get(),v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3)

            match onandoff:
                case "开启" | "关闭":
                    combobox0.set(onandoff)
                case "关闭":
                    combobox0.set("开启")
                    save(theme_cbo.get(),v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3)

            match circular:
                case "5MB" | "10MB" | "30MB" | "50MB" | "70MB" | "128MB" | "256MB" | "512MB":
                    combobox3.set(circular)
                case _:
                    save(theme_cbo.get(),v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3)

        QuicklyCreate(w6).quickly_create_drop_down_box(["使用時代:", "使用性質:", "使用作者:", "使用韻書:","使用聲調"],
                                                       YONG_MING_TI_LIST,
                                                       YONG_MING_TI_DATA_JSON, YONG_MING_TI_PATH, main_frame_row=0, main_frame_column=0)

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
                w_4_3_var_ = ttk.Checkbutton(w_4_3_1, text="PNG", variable=w_4_3_var, command=lambda: t_s_(Z_PATH, var_num_w_4_3), style="round-toggle")
                w_4_3_var_.grid(column=0,row=0,padx=5,pady=5)

                w_4_3_var2 = ttk.IntVar()
                if var2_num_w_4_3 % 2 == 1:
                    w_4_3_var2.set(1)
                else:
                    w_4_3_var2.set(0)
                w_4_3_var2_ = ttk.Checkbutton(w_4_3_1, text="css", variable=w_4_3_var2, command=lambda: t_s_(AA_PATH, var2_num_w_4_3), style="round-toggle")
                w_4_3_var2_.grid(column=1,row=0,padx=5,pady=5)

                w_4_3_var3 = ttk.IntVar()
                if var3_num_w_4_3 % 2 == 1:
                    w_4_3_var3.set(1)
                else:
                    w_4_3_var3.set(0)
                w_4_3_var3_ = ttk.Checkbutton(w_4_3_1, text="HTML", variable=w_4_3_var3, command=lambda: t_s_(AB_PATH, var3_num_w_4_3), style="round-toggle")
                w_4_3_var3_.grid(column=2,row=0,padx=5,pady=5)

            # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException
            def w_4_2_():

                def event_t():
                    with open(R_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box.get()))

                def down_box2_save():
                    with open(S_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box2.get()))

                def down_box3_save():
                    with open(T_PATH, 'w', encoding='utf-8') as file:
                        file.write(str(down_box3.get()))

                down_box = ttk.Combobox(w_4_2, values=["横排样式", "竖排样式"], state="readonly")
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
                    case "子时视明日":
                        ToolTip(down_box3, text="早子时、晚子时视明日\n新历、农历、道历都会受此项影响")
                        down_box3.set(t3)
                    case "子时视本日":
                        ToolTip(down_box3, text="早子时、晚子时视本日\n新历、农历、道历都会受此项影响")
                        down_box3.set(t3)
                    case "子时中而分界":
                        ToolTip(down_box3, text="早子时视今日，晚子时视明日\n新历、农历、道历都会受此项影响")
                        down_box3.set(t3)
                    case _:
                        down_box3.set("子时视明日")
                        down_box3_save()

            w_4_3_()

            w_4_2_()

        lb6 = ttk.Label(w_4, text="小六壬:")
        lb6.grid(column=0,row=0,padx=10,pady=10,ipadx=5)

        # noinspection PyPep8Naming,PyShadowingNames,PyArgumentList,PyUnboundLocalVariable,PyBroadException,PyUnusedLocal,DuplicatedCode
        def w_4_1_():

            w_4_1_v_0 = ["新历","农历","道历"]
            w_4_1_v_1 = ["时区","平太阳时","真太阳时"]
            w_4_1_v_3 = ["月日时起卦","时刻分起卦","平均随机数起卦","随机数起卦", "五行起卦", "八卦起卦", "八卦五行起卦"]
            w_4_1_v_4 = ["子时视明日", "子时视本日", "子时中而分界"]
            w_4_1_v_5 = ["作本月", "作下月", "月中为界"]
            w_4_1_v_6 = ["关闭","开启"]
            w_4_1_v_7 = ["开启","关闭"]
            w_4_1_v_8 = ["顺首","复首"]
            w_4_1_v_9 = ["0取10","0取0"]
            w_4_1_v_10 = ["0刻取0刻", "0刻取1刻"]

            text1_dict = {
                0: "将调用“起卦时区”中选择的时区",
                1: "将调用“起卦时区”中选择的时区，后转换成平太阳时",
                2: "将调用“起卦时区”中选择的时区，后转换成真太阳时"
            }

            text4_dict = {
                0: "将调用“起卦时区”中选择的时区",
                1: "将调用“起卦时区”中选择的时区，后转换成平太阳时",
                2: "将调用“起卦时区”中选择的时区，后转换成真太阳时"
            }

            text5_dict = {
                0: "早子时、晚子时视明日\n新历、农历、道历都会受此项影响",
                1: "早子时、晚子时视本日\n新历、农历、道历都会受此项影响",
                2: "早子时视今日，晚子时视明日\n新历、农历、道历都会受此项影响"
            }

            text6_dict = {
                0: "此设置仅限农历、道历",
                1: "此设置仅限农历、道历",
                2: "此设置仅限农历、道历"
            }

            text8_dict = {
                0: "大安为首，天宫，人宫所落位置的下一位为第二、第三首",
                1: "大安为首，天宫，人宫所落位置为第二、第三首"
            }

            def tool_tip_text():
                text_1 = text1_dict[XLR_JSON[1]]
                text_4 = text5_dict[XLR_JSON[4]]
                text_5 = text6_dict[XLR_JSON[5]]
                text_8 = text8_dict[XLR_JSON[8]]
                ToolTip(down_box_1, text=text_1)
                ToolTip(down_box_4, text=text_4)
                ToolTip(down_box_5, text=text_5)
                ToolTip(down_box_8, text=text_8)

            def set_down_box():
                down_box_0.set(w_4_1_v_0[XLR_JSON[0]])
                down_box_1.set(w_4_1_v_1[XLR_JSON[1]])
                down_box_2.set(utc())
                down_box_3.set(w_4_1_v_3[XLR_JSON[3]])
                down_box_4.set(w_4_1_v_4[XLR_JSON[4]])
                down_box_5.set(w_4_1_v_5[XLR_JSON[5]])
                down_box_6.set(w_4_1_v_6[XLR_JSON[6]])
                down_box_7.set(w_4_1_v_7[XLR_JSON[7]])
                down_box_8.set(w_4_1_v_8[XLR_JSON[8]])
                down_box_9.set(w_4_1_v_9[XLR_JSON[9]])
                down_box_10.set(w_4_1_v_10[XLR_JSON[10]])

                tool_tip_text()

            def modify_xlr_json():
                XLR_JSON[0] = w_4_1_v_0.index(down_box_0.get())
                XLR_JSON[1] = w_4_1_v_1.index(down_box_1.get())
                XLR_JSON[2] = UTC_TIME.index(down_box_2.get())
                XLR_JSON[3] = w_4_1_v_3.index(down_box_3.get())
                XLR_JSON[4] = w_4_1_v_4.index(down_box_4.get())
                XLR_JSON[5] = w_4_1_v_5.index(down_box_5.get())
                XLR_JSON[6] = w_4_1_v_6.index(down_box_6.get())
                XLR_JSON[7] = w_4_1_v_7.index(down_box_7.get())
                XLR_JSON[8] = w_4_1_v_8.index(down_box_8.get())
                XLR_JSON[9] = w_4_1_v_9.index(down_box_9.get())
                XLR_JSON[10] = w_4_1_v_10.index(down_box_10.get())

                tool_tip_text()

                File.dict_save(XLR_DATA_PATH, XLR_JSON.file_dict)

            w_4_1_f_1 = ttk.Frame(w_4_1)

            w_4_1_text_0 = ttk.Label(w_4_1_f_1, text="起卦历法:")
            w_4_1_text_1 = ttk.Label(w_4_1_f_1, text="起卦时间:")
            w_4_1_text_2 = ttk.Label(w_4_1_f_1, text="起卦时区:")
            w_4_1_text_3 = ttk.Label(w_4_1_f_1, text="起卦方法:")
            w_4_1_text_8 = ttk.Label(w_4_1_f_1, text="起卦算法:")
            w_4_1_text_4 = ttk.Label(w_4_1_f_1, text="时辰问题:")
            w_4_1_text_5 = ttk.Label(w_4_1_f_1, text="闰月问题:")
            w_4_1_text_6 = ttk.Label(w_4_1_f_1, text="计算吉值:")
            w_4_1_text_7 = ttk.Label(w_4_1_f_1, text="三宫定义:")
            w_4_1_text_9 = ttk.Label(w_4_1_f_1, text="数值问题:")
            w_4_1_text_10 = ttk.Label(w_4_1_f_1, text="时刻问题:")

            down_box_0 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_0, state="readonly")
            down_box_0.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_1 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_1, state="readonly")
            down_box_1.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_2 = ttk.Combobox(w_4_1_f_1, values=UTC_TIME, state="readonly")
            down_box_2.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_3 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_3, state="readonly")
            down_box_3.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())
            down_box_3.bind("<Button-3>", lambda event: Transfer(window,down_box_3))

            down_box_4 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_4, state="readonly")
            down_box_4.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_5 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_5, state="readonly")
            down_box_5.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_6 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_6, state="readonly")
            down_box_6.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_7 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_7, state="readonly")
            down_box_7.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_8 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_8, state="readonly")
            down_box_8.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_9 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_9, state="readonly")
            down_box_9.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            down_box_10 = ttk.Combobox(w_4_1_f_1, values=w_4_1_v_10, state="readonly")
            down_box_10.bind("<<ComboboxSelected>>", lambda event: modify_xlr_json())

            messagebox.showerror("错误", message=f"{XLR_JSON}", parent=window) if isinstance(XLR_JSON,Exception) else set_down_box()
            w_4_1_f_1.grid(row=0,column=0,padx=10,pady=10,sticky=W)

            w_4_1_text_0.grid(row=0,column=0,padx=5,pady=5,sticky=W)
            w_4_1_text_1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_2.grid(row=2, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_3.grid(row=3, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_8.grid(row=4, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_4.grid(row=5, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_5.grid(row=6, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_6.grid(row=7, column=0, padx=5, pady=5, sticky=W)
            w_4_1_text_7.grid(row=8, column=0, padx=5, pady=5, sticky=W)
            down_box_0.grid(row=0, column=1, padx=5, pady=5, sticky=W)
            down_box_1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            down_box_2.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            down_box_3.grid(row=3, column=1, padx=5, pady=5, sticky=W)
            down_box_8.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            down_box_4.grid(row=5, column=1, padx=5, pady=5, sticky=W)
            down_box_5.grid(row=6, column=1, padx=5, pady=5, sticky=W)
            down_box_6.grid(row=7, column=1, padx=5, pady=5, sticky=W)
            down_box_7.grid(row=8, column=1, padx=5, pady=5, sticky=W)

            w_4_1_text_9.grid(row=0, column=2, padx=5, pady=5, sticky=W)
            down_box_9.grid(row=0, column=3, padx=5, pady=5, sticky=W)
            w_4_1_text_10.grid(row=1, column=2, padx=5, pady=5, sticky=W)
            down_box_10.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        w_4_1_()

        w_root4_row6()


    w_root4()


    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = window.winfo_width()
    window_height = window.winfo_height()

    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2

    window.geometry(f"+{position_x}+{position_y+80}")

    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()