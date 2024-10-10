from function.ProjectDictionaryVariables import ZHI_DICT_NUM


class XiaoLiuRenNum:
    def __init__(self,month,day,hour,shuzhi,method=0):
        self.month=month#月-时
        self.day=day#天-刻
        self.hour=ZHI_DICT_NUM[hour]#时-分
        self.method=method
        self.shuzhi=shuzhi
        if shuzhi == 1:
            if self.month == 0:
                self.month = 10
            if self.day == 0:
                self.day = 10
            if self.hour == 0:
                self.hour = 10

    def xiao_liu_ren_num(self):
        if self.method == 0:
            t = self.month % 6
            r = (self.month + self.day) % 6
            d = (self.month + self.day + self.hour - 2) % 6
        else:
            t = self.month % 6
            r = (self.month + self.day - 1) % 6
            d = (self.month + self.day + self.hour - 2) % 6
        return t, r, d