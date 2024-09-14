from datetime import datetime, timedelta, timezone

import re

from lunar_python import Solar

from function.GregorianCalendarLunar import GregorianCalendarToLunar

'''
print("年：", year)
print("月：", month)
print("日：", day)
print("小时：", hour)
print("分钟：", minute)

Lunar_year,Lunar_month,Lunar_day = GregorianCalendarToLunar.to_lunar(year, month, day)
'''


class XiaoLiuRenQiGua:
    def __init__(self, to_utc_offset):
        # 获取
        current_time = datetime.now().astimezone().replace(second=0, microsecond=0)
        self.to_zone = self._parse_timezone_offset(to_utc_offset)

        original_time_str = current_time.strftime('%Y-%m-%d %H:%M')
        print(f"Original Time: {original_time_str}")

        # 时间转换
        converted_time = self._convert_timezone(current_time)
        print(f"Converted Time: {converted_time.strftime('%Y-%m-%d %H:%M')}")

        # 农历
        solar = Solar.fromDate(converted_time)
        lunar = solar.getLunar()
        lunar_year, lunar_month, lunar_day = GregorianCalendarToLunar.to_lunar(
            converted_time.year, converted_time.month, converted_time.day)

        print(f"Solar Date: {solar}")
        print(f"Lunar Date: Year {lunar_year}, Month {lunar_month}, Day {lunar_day}")

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

# 使用例子，只输入目标时区
gua = XiaoLiuRenQiGua("UTC+02:00")