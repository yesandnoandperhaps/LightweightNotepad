import threading

import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText

from function.ProjectFunctions import window_init
from module.YongMingTi import YongMingTi


class PrintWindow:
    def __init__(self, main_window, title, font_style, text_widget):
        self.main_window = main_window
        self.FONT_STYLE = font_style
        self.text_widget = text_widget
        self.window = ttk.Toplevel(str(main_window))
        window_init(self.window, main_window, text=title)
        self.window.resizable(None, None)

        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        self.window_width = int(screen_width * 0.5)
        self.window_height = int(screen_height * 0.5)
        self.window.geometry(f"{self.window_width}x{self.window_height}")

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(2, weight=1)

        self.wait_label = ttk.Label(self.window, text="请等待...")
        self.wait_label.grid(row=0, column=0, pady=10, padx=10, sticky="n")

        self.detail_button = ttk.Button(
            self.window, text="显示详细信息", style="link", command=self.toggle_details
        )
        self.detail_button.grid(row=1, column=0, pady=5, padx=10, sticky="n")

        self.details_frame = ttk.Frame(self.window)
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
        thread.daemon = True
        thread.start()

        # window.bind("<Control-x>", lambda event: YongMingTi(self.text_box).fetch())

    def toggle_details(self):
        """显示或隐藏日志区域并调整窗口大小以适配组件"""
        window_width = self.window.winfo_width()

        if self.details_visible:
            self.details_frame.grid_forget()
            self.detail_button.config(text="显示详细信息")

            self.window.update_idletasks()
            new_height = self.wait_label.winfo_reqheight() + self.detail_button.winfo_reqheight() + 40  # 加额外边距
            self.window.geometry(f"{window_width}x{new_height}")
        else:
            self.details_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
            self.window.grid_columnconfigure(0, weight=1)
            self.window.grid_rowconfigure(2, weight=1)
            self.detail_button.config(text="隐藏详细信息")

            self.window.update_idletasks()
            new_height = (
                    self.wait_label.winfo_reqheight()
                    + self.detail_button.winfo_reqheight()
                    + self.details_frame.winfo_reqheight()
                    + 40  # 加额外边距
            )
            self.window.geometry(f"{self.window_width}x{self.window_height}")

        # 切换状态
        self.details_visible = not self.details_visible

    def yongming(self):
        YongMingTi(self.text_widget,self.text_box,self.window,
        self.FONT_STYLE,self.main_window).fetch()


if __name__ == "__main__":
    root = ttk.Window()
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app = PrintWindow(root,"a")
    root.mainloop()
