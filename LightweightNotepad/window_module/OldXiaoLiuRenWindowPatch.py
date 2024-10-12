import ttkbootstrap as ttk


class LabelManager:
    labels = []
    def __init__(self, parent_frame, font_style):
        self.parent_frame = parent_frame
        self.font_style = font_style

    def init_labels(self):
        label0 = ttk.Label(self.parent_frame, text="天宫",font=self.font_style)
        label1 = ttk.Label(self.parent_frame, text="人宫",font=self.font_style)
        label2 = ttk.Label(self.parent_frame, text="地宫",font=self.font_style)
        label0.grid(column=0, row=0, padx=10, pady=10)
        label1.grid(column=0, row=1, padx=10, pady=10)
        label2.grid(column=0, row=2, padx=10, pady=10)
        a = 1
        a_ = 1
        for i in range(18):
            lbl = ttk.Label(self.parent_frame, text="", font=self.font_style)
            LabelManager.labels.append(lbl)
            if i <= 5:
                lbl.grid(column=1 + i, row=0, padx=10, pady=10)
            elif 6 <= i <= 11:
                lbl.grid(column=a, row=1, padx=10, pady=10)
                a += 1
            else:
                lbl.grid(column=a_, row=2, padx=10, pady=10)
                a_ += 1

    @staticmethod
    def update_labels(xlr_num):
        """更新标签的文本"""
        if xlr_num is not None:
            t1, t2, t3, t4, t5, t6, r1, r2, r3, r4, r5, r6, d1, d2, d3, d4, d5, d6 = xlr_num

            values = [t1, t2, t3, t4, t5, t6, r1, r2, r3, r4, r5, r6, d1, d2, d3, d4, d5, d6]

            for i, value in enumerate(values):
                print(i, value)
                LabelManager.labels[i].config(text=value)

