from tkinter import messagebox

from function.ProjectVariables import B_PATH, C_PATH, D_PATH, E_PATH, F_PATH, L_PATH, M_PATH, H_PATH, I_PATH, J_PATH, \
    K_PATH


def save(theme,v,v2,v3,v4,v5,v6,combobox1,combobox2,combobox0,combobox3):
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
    with open(L_PATH, "w", encoding='utf-8') as file:
        file.write(str(v5))
    with open(M_PATH, "w", encoding='utf-8') as file:
        file.write(str(v6))
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