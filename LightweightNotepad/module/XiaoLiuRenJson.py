from datetime import datetime, timedelta, timezone
import re
from lunar_python import Solar
from function.GregorianCalendarLunar import GregorianCalendarToLunar
from function.ProjectFunctions import utc
from function.ProjectDictionaryVariables import SHI_CHEN_DICT

class Calendar:
    def __init__(self,xlr_json_list):
        self.xlr_json_list = xlr_json_list


    def function_selection(self):

        function_selection = {
            0: self.gregorian_calendar,
            1: self.chinese_calendar,
            2: self.taoism_calendar,
        }

        return function_selection[self.xlr_json_list]()

    @staticmethod
    def gregorian_calendar():
        current_time = datetime.now().astimezone().replace(second=0, microsecond=0)
        return current_time

    @staticmethod
    def chinese_calendar():
        current_time = Calendar.gregorian_calendar()
        return ChineseCalendar(current_time,utc()).get_lunar_date()

    @staticmethod
    def taoism_calendar():
        converted_time, lunar_year, lunar_month, lunar_day,lunar_hour, all_lunar = Calendar.chinese_calendar()
        dao_year = converted_time.year + 2698
        return dao_year, lunar_month, lunar_day, lunar_hour


class ChineseCalendar:
    def __init__(self, current_time,to_utc_offset):
        # 获取
        self.to_zone = self._parse_timezone_offset(to_utc_offset)

        #original_time_str = current_time.strftime('%Y-%m-%d %H:%M')

        # 时间转换
        self.converted_time = self._convert_timezone(current_time)

        # 农历
        solar = Solar.fromDate(self.converted_time)
        lunar = solar.getLunar()
        lunar_year, lunar_month, lunar_day = GregorianCalendarToLunar.to_lunar(
            self.converted_time.year, self.converted_time.month, self.converted_time.day)

        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day
        self.lunar_hour = SHI_CHEN_DICT[self.converted_time.hour]
        self.all_lunar = lunar.toFullString()

    @staticmethod
    def _parse_timezone_offset(offset_str):
        if not re.match(r'^UTC[+-]\d{2}:\d{2}$', offset_str):
            raise ValueError("Invalid time zone format. Use 'UTC±HH:MM'.")

        sign = 1 if offset_str[3] == '+' else -1
        hours, minutes = map(int, offset_str[4:].split(':'))
        return timezone(timedelta(hours=sign * hours, minutes=sign * minutes))

    def _convert_timezone(self, time):
        to_time = time.astimezone(self.to_zone)
        return to_time

    def get_lunar_date(self):
        return self.converted_time, self.lunar_year, self.lunar_month, self.lunar_day, self.lunar_hour, self.all_lunar


p = Calendar(2)
print(p.function_selection())