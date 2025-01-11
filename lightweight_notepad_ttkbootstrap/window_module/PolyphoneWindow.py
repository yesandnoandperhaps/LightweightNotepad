from function.ProjectFunctions import window_init, window_closes
import ttkbootstrap as ttk

class PolyphoneWindow:
    def __init__(self, main_window, title, font_style, polyphone_list,word):
        self.window = None
        self.word = word
        self.drop_down_box = None
        self.result = None
        self.FONT_STYLE = font_style
        self.main_window = main_window
        self.title = title
        self.polyphone_list = polyphone_list

    def polyphone_window(self):
        self.window = ttk.Toplevel(str(self.main_window))
        self.window.resizable(False, False)
        window_init(self.window, self.main_window, text=self.title)

        text = ttk.Label(self.window, text=self.word)
        text.grid(column=0, row=0, padx=10, pady=10)

        self.drop_down_box = ttk.Combobox(
            self.window,
            values=self.polyphone_list,
            state="readonly",
        )

        self.drop_down_box.bind(
            "<Control_R>",
            lambda event: self.assignment(),
        )

        self.drop_down_box.grid(column=1, row=0, padx=10, pady=10)

        while self.result is None:
            self.main_window.update()

        return self.result

    def assignment(self):
        self.result = self.drop_down_box.get()
        window_closes(self.window, self.main_window)