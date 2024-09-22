import math
from datetime import datetime, timedelta, timezone

class SolarTimeCalculator:
    def __init__(self, longitude, timezone_offset, date=None):
        """
        初始化 SolarTimeCalculator 实例
        :param longitude: 地理经度（东经为正，西经为负）
        :param timezone_offset: 本地时区相对 UTC 的偏移，单位为小时
        :param date: 指定日期（datetime 对象），默认为当前时间
        """
        self.longitude = longitude
        self.timezone_offset = timezone_offset
        self.date = date or datetime.now(timezone.utc) + timedelta(hours=timezone_offset)

    def calculate_mean_solar_time(self):
        """
        计算平太阳时（Mean Solar Time, MST）
        :return: 平太阳时（小时:分钟:秒）
        """
        mst = self.date + timedelta(hours=self.longitude / 15)  # 地球每小时自转15度
        return mst.strftime("%H:%M:%S")

    def calculate_true_solar_time(self):
        """
        计算真太阳时（True Solar Time, TST）
        :return: 真太阳时（小时:分钟:秒）
        """
        # 计算平太阳时
        mst = self.calculate_mean_solar_time()

        # 求出年积日（year day, yday）
        start_of_year = datetime(self.date.year, 1, 1, tzinfo=timezone.utc)
        day_of_year = (self.date - start_of_year).days + 1

        # 计算均时差（Equation of Time, eo_t），单位为分钟
        b = (360 / 365) * (day_of_year - 81)  # 81是春分日
        eo_t = 9.87 * math.sin(math.radians(2 * b)) - 7.53 * math.cos(math.radians(b)) - 1.5 * math.sin(math.radians(b))

        # 计算真太阳时
        mst_dt = datetime.strptime(mst, "%H:%M:%S")
        true_solar_time = mst_dt + timedelta(minutes=eo_t)
        return true_solar_time.strftime("%H:%M:%S")