from LightweightNotepad.function.ProjectDictionaryVariables import ZHI_DICT_NUM


class XiaoLiuRenNum:
    def __init__(self,month,day,hour,method=0):
        self.month=month
        self.day=day
        self.hour=ZHI_DICT_NUM[hour]
        self.method=method

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