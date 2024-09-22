from datetime import datetime

from lunar_python import Solar, Lunar

from function.ProjectDictionaryVariables import SHI_CHEN_DICT
from function.ProjectFunctions import utc
from function.TimeZoneConversion import TimeZoneConversionT


class Calendar:
    def __init__(self, xlr_json_list_0, xlr_json_list_1):
        self.xlr_json_list_0 = xlr_json_list_0
        self.xlr_json_list_1 = xlr_json_list_1
        self.utc = utc()
        self.convert_time = datetime.now().astimezone().replace()

        a = TimeZoneConversionT(self.convert_time, self.utc)
        self.converted_time = a.get_zone_time()

    def function_selection(self):
        function_selection = {
            0: self.gregorian_calendar,
            1: self.chinese_calendar,
            2: self.taoism_calendar,
        }

        return function_selection[self.xlr_json_list_0]()

    @staticmethod
    def time_partition(minute,second,d_):
        if minute <= 59 and second <= 59:
            pass
        else:
            d_.next(1)
        return d_

    def gregorian_calendar(self):
        d = Solar.fromDate(self.converted_time)
        a0,a1,a2,a3=SHI_CHEN_DICT[self.converted_time.hour]

        if a0 == "子":
            if self.xlr_json_list_1 == 0:
                self.converted_time = d.next(1)
            elif self.xlr_json_list_1 == 1:
                pass
            else:
                self.converted_time = Calendar.time_partition(self.converted_time.minute, self.converted_time.second, d)

        return self.converted_time.year, self.converted_time.month, self.converted_time.day, SHI_CHEN_DICT[self.converted_time.hour]


    def chinese_calendar(self):
        return ChineseCalendar(self.converted_time,self.xlr_json_list_1).get_lunar_date()

    def taoism_calendar(self):
        lunar_year, lunar_month, lunar_day, lunar_hour = self.chinese_calendar()
        current_year, _, _, _ = self.gregorian_calendar()
        dao_year = current_year + 2698
        return dao_year, lunar_month, lunar_day, lunar_hour


class ChineseCalendar:
    def __init__(self, current_time, xlr_json_list_1):

        self.converted_time = current_time
        self.xlr_json_list_1 = xlr_json_list_1


        d = Lunar.fromDate(self.converted_time)
        self.lunar_year = d.getYear()
        self.lunar_month = d.getMonth()
        self.lunar_day = d.getDay()
        self.a0 = d.getTimeZhi()

        if self.a0 == "子":
            if self.xlr_json_list_1 == 0:
                self.converted_time = d.next(1)
                self.lunar_year = self.converted_time.getYear()
                self.lunar_month = self.converted_time.getMonth()
                self.lunar_day = self.converted_time.getDay()
            elif self.xlr_json_list_1 == 1:
                pass
            else:
                self.converted_time = Calendar.time_partition(self.converted_time.minute, self.converted_time.second, d)
                self.lunar_year = self.converted_time.getYear()
                self.lunar_month = self.converted_time.getMonth()
                self.lunar_day = self.converted_time.getDay()

    def get_lunar_date(self):
        return self.lunar_year, self.lunar_month, self.lunar_day, self.a0


p = Calendar(1,1)
print(p.function_selection())