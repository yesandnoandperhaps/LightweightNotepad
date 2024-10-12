from window_module.set_window.RandomNumbersWindow import RandomNumbersWindow
from window_module.set_window.WuXingWindow import WuXingWindow


class Transfer:
    def __init__(self,main_window,down_box_3):
        if down_box_3.get() == "五行起卦":
            WuXingWindow(main_window)
        elif down_box_3.get() == "随机数起卦":
            RandomNumbersWindow(main_window)