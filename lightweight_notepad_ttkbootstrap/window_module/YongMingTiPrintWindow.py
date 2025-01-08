import threading

import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText

from function.ProjectFunctions import window_init
from module.YongMingTi import YongMingTi


class PrintWindow:
    def __init__(self, main_window, title, font_style, text_widget):
        self.FONT_STYLE = font_style
        self.text_widget = text_widget
        window = ttk.Toplevel(str(main_window))
        window_init(window, main_window, text=title)
        window.resizable(None, None)

        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)
        window.geometry(f"{window_width}x{window_height}")

        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(2, weight=1)

        self.wait_label = ttk.Label(window, text="请等待...")
        self.wait_label.grid(row=0, column=0, pady=10, padx=10, sticky="n")

        self.detail_button = ttk.Button(
            window, text="显示详细信息", style="link", command=self.toggle_details
        )
        self.detail_button.grid(row=1, column=0, pady=5, padx=10, sticky="n")

        self.details_frame = ttk.Frame(window)
        self.details_visible = True

        self.text_box = ScrolledText(
            self.details_frame, height=15, autohide=True, font=self.FONT_STYLE
        )
        self.text_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.details_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.details_frame.grid_rowconfigure(0, weight=1)
        self.details_frame.grid_columnconfigure(0, weight=1)

        self.detail_button.config(text="隐藏详细信息")

        thread = threading.Thread(target=self.yongming)
        thread.start()

        # window.bind("<Control-x>", lambda event: YongMingTi(self.text_box).fetch())

    def toggle_details(self):
        """显示或隐藏日志区域"""
        if self.details_visible:
            # 隐藏日志区域
            self.details_frame.grid_forget()
            self.detail_button.config(text="显示详细信息")
        else:
            # 显示日志区域
            self.details_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
            self.details_frame.grid_rowconfigure(0, weight=1)
            self.details_frame.grid_columnconfigure(0, weight=1)
            self.detail_button.config(text="隐藏详细信息")
        self.details_visible = not self.details_visible

    def yongming(self):
        YongMingTi(self.text_widget,self.text_box).fetch()


if __name__ == "__main__":
    root = ttk.Window()
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = PrintWindow(root,"a")
    root.mainloop()
