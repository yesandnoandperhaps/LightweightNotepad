import math
from datetime import datetime, timedelta, timezone
from pysolar.solar import get_altitude

class SolarTimeCalculator:
    def __init__(self, latitude, longitude):
        """
        初始化类，接收纬度和经度
        :param latitude: 纬度
        :param longitude: 经度
        """
        self.latitude = latitude
        self.longitude = longitude

    def get_current_utc_time(self):
        """
        获取当前的UTC时间
        :return: 当前的UTC时间（时区感知的datetime对象）
        """
        return datetime.now(timezone.utc)

    def calculate_standard_time(self):
        """
        计算平太阳时（标准时间），基于当前UTC时间和经度
        :return: 标准时间（时区感知的datetime对象）
        """
        utc_time = self.get_current_utc_time()
        standard_time = utc_time + timedelta(hours=self.longitude / 15)
        return standard_time

    def calculate_solar_time(self):
        """
        计算真太阳时，基于标准时间、太阳的高度角
        :return: 真太阳时（时区感知的datetime对象）
        """
        standard_time = self.calculate_standard_time()
        utc_time = self.get_current_utc_time()

        # 使用pysolar库计算太阳的高度角
        altitude = get_altitude(self.latitude, self.longitude, utc_time)

        # 通过太阳的高度角修正标准时间以获得真太阳时
        solar_time = standard_time + timedelta(minutes=4 * (math.degrees(math.atan2(1, math.tan(math.radians(altitude))))))
        return solar_time

    def get_solar_times(self):
        """
        返回平太阳时和真太阳时
        :return: (平太阳时, 真太阳时) - 时区感知的datetime对象
        """
        standard_time = self.calculate_standard_time()
        solar_time = self.calculate_solar_time()
        return standard_time, solar_time


if __name__ == "__main__":
    # 输入经纬度
    latitude = float(input("输入纬度："))
    longitude = float(input("输入经度："))

    # 创建SolarTimeCalculator类的实例
    calculator = SolarTimeCalculator(latitude, longitude)

    # 获取平太阳时和真太阳时
    standard_time, solar_time = calculator.get_solar_times()

    print(f"平太阳时: {standard_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"真太阳时: {solar_time.strftime('%Y-%m-%d %H:%M:%S')}")
