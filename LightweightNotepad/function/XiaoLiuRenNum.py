from LightweightNotepad.function.variables.ProjectDictionaryVariables import ZHI_DICT_NUM


class XiaoLiuRenNum:
    def __init__(self, month, day, hour, shuzhi, method=0):
        print(
            f"Initializing XiaoLiuRenNum with month={month}, day={day}, hour={hour}, shuzhi={shuzhi}, method={method}")

        self.month = month  # 月-时
        self.day = day  # 天-刻

        if isinstance(hour, str):
            self.hour = ZHI_DICT_NUM[hour]  # 时-分
            print(f"XiaoLiuRenNum: hour is str, converted hour={self.hour}")
        elif isinstance(hour, int):
            self.hour = hour
            print(f"XiaoLiuRenNum: hour is int, using hour={self.hour}")

        self.method = method
        self.shuzhi = shuzhi

        # Debug prints for checking values
        print(f"Before adjustment: month={self.month}, day={self.day}, hour={self.hour}, shuzhi={self.shuzhi}")

        if shuzhi == 1:
            if self.month == 0:
                self.month = 10
            if self.day == 0:
                self.day = 10
            if self.hour == 0:
                self.hour = 10

        # Final values after adjustments
        print(f"After adjustment: month={self.month}, day={self.day}, hour={self.hour}, shuzhi={self.shuzhi}")

    def xiao_liu_ren_num(self):
        if self.method == 0:
            t = self.month % 6
            r = (self.month + self.day) % 6
            d = (self.month + self.day + self.hour - 2) % 6
        else:
            t = self.month % 6
            r = (self.month + self.day - 1) % 6
            d = (self.month + self.day + self.hour - 2) % 6

        print(f"xiao_liu_ren_num results: t={t}, r={r}, d={d}")
        return t, r, d
