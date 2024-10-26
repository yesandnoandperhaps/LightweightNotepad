from ttkbootstrap.tooltip import ToolTip
class CustomToolTip(ToolTip):
    def update_text(self, text):
        self.text = text