import ttkbootstrap as ttk


class LabelManager:
    def __init__(self, parent_frame, font_style):
        self.parent_frame = parent_frame
        self.font_style = font_style
        self.labels = []  # 存储标签的列表

    def clear_labels(self):
        """清除当前所有的标签"""
        for label in self.labels:
            label.destroy()
        self.labels = []  # 清空列表

    def create_labels(self, xlr_num):
        """创建新的标签"""
        if xlr_num is not None:
            # 清除之前的标签
            self.clear_labels()

            # 解包 xlr_num
            t1, t2, t3, t4, t5, t6, r1, r2, r3, r4, r5, r6, d1, d2, d3, d4, d5, d6 = xlr_num

            # 创建标题标签
            labels = ["天宫", "人宫", "地宫"]
            for i, label in enumerate(labels):
                lbl = ttk.Label(self.parent_frame, text=label, font=self.font_style)
                lbl.grid(row=i, column=0, padx=5, pady=5)
                self.labels.append(lbl)  # 将标签存储到实例变量中

            # 创建数值标签
            t_values = [t1, t2, t3, t4, t5, t6]
            r_values = [r1, r2, r3, r4, r5, r6]
            d_values = [d1, d2, d3, d4, d5, d6]

            # 放置 t 开头的标签在天宫下面
            for i, value in enumerate(t_values):
                lbl = ttk.Label(self.parent_frame, text=value, font=self.font_style)
                lbl.grid(row=0, column=i + 1, padx=5, pady=5)  # 天宫下的标签
                self.labels.append(lbl)

            # 放置 r 开头的标签在人宫下面
            for i, value in enumerate(r_values):
                lbl = ttk.Label(self.parent_frame, text=value, font=self.font_style)
                lbl.grid(row=1, column=i + 1, padx=5, pady=5)  # 人宫下的标签
                self.labels.append(lbl)

            # 放置 d 开头的标签在地宫下面
            for i, value in enumerate(d_values):
                lbl = ttk.Label(self.parent_frame, text=value, font=self.font_style)
                lbl.grid(row=2, column=i + 1, padx=5, pady=5)  # 地宫下的标签
                self.labels.append(lbl)
