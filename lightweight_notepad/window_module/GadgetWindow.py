import ttkbootstrap as ttk
from ttkbootstrap import OUTLINE

from window_module.xiao_liu_ren_window.OldXiaoLiuRenWindow import OldXiaoLiuRenWindow
from window_module.PictureWindow import picture
from function.variables.ProjectPathVariables import ICON_PATH
#from window_module.RegressionWindow import regression
from window_module.ZiWeiDouShuWindow import zi_wei_dou_shu_window


class GadgetWindow:
    _instance = None  # 用于跟踪单例窗口

    def __init__(self, root, icon, font_style):
        if GadgetWindow._instance is not None and GadgetWindow._instance.winfo_exists():
            # 如果窗口已经存在，聚焦该窗口
            GadgetWindow._instance.focus()
            return

        self.window = ttk.Toplevel(str(root))
        GadgetWindow._instance = self.window  # 记录窗口实例

        self.window.title("轻量记事本-小工具")
        self.window.iconbitmap(ICON_PATH)
        self.window.resizable(None, None)

        b1 = ttk.Button(self.window, text="小六壬", style=OUTLINE, command=lambda: OldXiaoLiuRenWindow(root, icon, font_style,0))
        b1.grid(column=0, row=0, padx=10, pady=10)
        b2 = ttk.Button(self.window, text="紫微斗数", style=OUTLINE, command=lambda: zi_wei_dou_shu_window(root, font_style))
        b2.grid(column=1, row=0, padx=10, pady=10)
        #b3 = ttk.Button(self.window, text="机器学习-回归问题", style=OUTLINE, command=lambda: regression(root))
        #b3.grid(column=2, row=0, padx=10, pady=10)
        #b4 = ttk.Button(self.window, text="三角形计算", style=OUTLINE, command=())
        #b4.grid(column=3, row=0, padx=10, pady=10)#
        b5 = ttk.Button(self.window, text="图片操作", style=OUTLINE, command=lambda: picture(root, icon))
        b5.grid(column=4, row=0, padx=10, pady=10)

        b1.bind("<Button-3>", lambda event: OldXiaoLiuRenWindow(root, icon, font_style, 1))
        # 设置窗口关闭时的行为
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        # 关闭窗口时，将实例设为 None
        GadgetWindow._instance = None
        self.window.destroy()

