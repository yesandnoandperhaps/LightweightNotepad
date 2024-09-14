import tkinter.font as tk_font
from ProjectFunctions import t_load
from ProjectPathVariables import D_PATH, E_PATH, F_PATH


# noinspection PyPep8Naming
def font_set():
    v2 = int(t_load(D_PATH) or 1)
    v3 = int(t_load(E_PATH) or 0)
    v4 = int(t_load(F_PATH) or 0)
    FONT_STYLE = None
    font_style1 = tk_font.Font(family="宋体", size=12)
    font_style2 = tk_font.Font(family="等线", size=12)
    font_style3 = tk_font.Font(family="黑体", size=12)

    if v2 % 2 == 1:
        FONT_STYLE = font_style1
    elif v3 % 2 == 1:
        FONT_STYLE = font_style2
    elif v4 % 2 == 1:
        FONT_STYLE = font_style3

    return FONT_STYLE,v2,v3,v4

