class FullscreenExample:
    def __init__(self,window):
        self.window = window
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggle_full_screen)
        self.window.bind("<Escape>", self.quit_full_screen)

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)