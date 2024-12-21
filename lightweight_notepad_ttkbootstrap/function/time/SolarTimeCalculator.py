import math
from datetime import datetime, timedelta, timezone

from lunar_python.util import SolarUtil


class SolarTimeCalculator:
    def __init__(self,longitude):
        self.longitude = longitude
        self.utc_time = self.utc_8()
        self.f = self.flat_solar_time()
        self.t = self.true_solar_time()

    @staticmethod
    def utc_8():
        return datetime.now(timezone.utc) + timedelta(hours=8)

    def flat_solar_time(self):
        flat_solar_time_variable = timedelta(minutes=(self.longitude - 120) * 4)

        flat_solar_time_variable_t = self.utc_time + flat_solar_time_variable

        return flat_solar_time_variable_t

    def true_solar_time(self):

        day = SolarUtil.getDaysInYear(self.utc_time.year, self.utc_time.month, self.utc_time.day)

        n0 = 79.6764 + 0.2422 * (self.utc_time.year - 1985) - int((self.utc_time.year - 1985) / 4)

        a = 2 * math.pi * (day - n0) / 365.2422

        a2 = a * 2

        t = 0.0028 - 1.9857 * math.sin(a) + 9.9059 * math.sin(a2) - 7.0924 * math.cos(a) - 0.6882 * math.cos(a2)

        true_solar_time_variable = self.flat_solar_time()

        true_solar_time_variable_t = true_solar_time_variable + timedelta(minutes=t)

        return true_solar_time_variable_t

    def true_flat_solar_time(self):
        return self.f, self.t

    def all(self):
        return self.f, self.t, self.utc_time
