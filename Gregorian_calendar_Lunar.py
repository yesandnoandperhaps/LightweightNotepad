from datetime import datetime
from lunar_python import Solar, Lunar
from lunar_python import LunarYear


class LunarNew(Lunar):
    @staticmethod
    def fromSolar(solar):
        year = 0
        month = 0
        day = 0
        ly = LunarYear.fromYear(solar.getYear())
        for m in ly.getMonths():
            days = solar.subtract(Solar.fromJulianDay(m.getFirstJulianDay()))
            if days < m.getDayCount():
                year = m.getYear()
                month = m.getMonth()
                day = days + 1
                break
        return year,month,day

class SolarNew(Solar):
    def getLunar(self):
        return LunarNew.fromSolar(self)

class GregorianCalendarToLunar:
    @staticmethod
    def to_lunar(year,month,day):
        solar = Solar.fromDate(datetime(year, month, day))
        lunar = SolarNew.getLunar(solar)
        return lunar

a,b,c = GregorianCalendarToLunar.to_lunar(2018,1,31)
print(a,b,c)