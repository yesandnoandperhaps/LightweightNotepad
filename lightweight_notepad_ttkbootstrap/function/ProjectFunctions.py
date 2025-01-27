import datetime
from datetime import datetime
from tkinter import messagebox

import dateutil.tz

from function import JsonFile
from function.variables.ProjectDictionaryVariables import UTC_TIME
from function.variables.ProjectPathVariables import B_PATH, C_PATH, H_PATH, I_PATH, J_PATH, \
    K_PATH, W_ROOT2_C_VAR_2_PATH, XLR_DATA_PATH, D_PATH, E_PATH, F_PATH, XLR_JSON

def t_s(v):
    v+=1
    return v

def t_s_(v,path):
    v += 1
    t_save(path, v)
    return v

def save(theme,v,v2,v3,v4,combobox1,combobox2,combobox0,combobox3):
    with open(B_PATH, 'w', encoding='utf-8') as file:
        file.write(theme)
    with open(C_PATH, 'w', encoding='utf-8') as file:
        file.write(str(v))
    with open(D_PATH, "w", encoding='utf-8') as file:
        file.write(str(v2))
    with open(E_PATH, "w", encoding='utf-8') as file:
        file.write(str(v3))
    with open(F_PATH, "w", encoding='utf-8') as file:
        file.write(str(v4))
    with open(H_PATH, "w", encoding='utf-8') as file:
        file.write(combobox1.get())
    with open(I_PATH, "w", encoding='utf-8') as file:
        file.write(combobox2.get())
    with open(J_PATH, "w", encoding="utf-8") as file:
        file.write(combobox0.get())
    with open(K_PATH, "w", encoding="utf-8") as file:
        file.write(combobox3.get())

def t_save(path,text_path):
    with open(path,"w",encoding='utf-8') as file:
        file.write(str(text_path))

def var_save(path,text_path):
    with open(path,"w",encoding='utf-8') as file:
        text_path += 1
        file.write(str(text_path))

def t_load(path):
    try:
        with open(path,"r",encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        pass
    except Exception as e:
        messagebox.showerror("错误", f"发生错误: {e}")

def load_theme():
    try:
        with open(B_PATH, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


def utc():
    def utc_():
        return UTC_TIME[UTC_TIME.index(formatted_offset)]
    local_timezone = dateutil.tz.tzlocal()
    now = datetime.now(local_timezone)
    offset = now.strftime('%z')
    formatted_offset = f"UTC{offset[:3]}:{offset[3:]}"
    var2 = int(t_load(W_ROOT2_C_VAR_2_PATH) or 0)
    if XLR_JSON[2] != UTC_TIME.index(formatted_offset):
        if var2 % 2 == 1:
            return UTC_TIME[int(XLR_JSON[2])]
        else:
            utc__ = utc_()
            XLR_JSON[2] = UTC_TIME.index(formatted_offset)
            JsonFile.File.dict_save(XLR_DATA_PATH, XLR_JSON.file_dict)
            return utc__
    else:
        return UTC_TIME[UTC_TIME.index(formatted_offset)]

def window_closes(window, root_main):
    window.destroy()
    root_main.wm_attributes('-disabled', 0)
    root_main.wm_attributes('-topmost', 1)
    root_main.wm_attributes('-topmost', 0)

def window_on(window, root_main):
    window.wm_attributes('-topmost', 1)
    window.wm_attributes('-topmost', 0)
    root_main.wm_attributes('-disabled', 1)

def window_init(window, root_main, text):
    window.title(text)
    window.protocol("WM_DELETE_WINDOW", lambda: window_closes(window, root_main))
    window_on(window, root_main)
    window.focus()

open_window = []

def a_window(window_class, root, icon, font_style):
    window = window_class(root, icon, font_style)
    # 检查是否已经有窗口打开
    if not open_window:
        window = window_class()

        # 在关闭窗口时移除实例
        def on_closing():
            open_window.remove(window)
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", on_closing)

        # 将窗口添加到列表中
        open_window.append(window)
        window.mainloop()
    else:
        open_window[0].focus_force()
