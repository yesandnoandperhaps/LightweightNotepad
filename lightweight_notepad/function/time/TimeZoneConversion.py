import re
from datetime import timedelta, timezone


class TimeZoneConversionF:
    def __init__(self, current_time,to_utc_offset):
        self.to_zone = self.parse_timezone_offset(to_utc_offset)
        self.converted_time = self.convert_timezone(current_time)

    @staticmethod
    def parse_timezone_offset(offset_str):
        if not re.match(r'^UTC[+-]\d{2}:\d{2}$', offset_str):
            raise ValueError("Invalid time zone format. Use 'UTC±HH:MM'.")

        sign = 1 if offset_str[3] == '+' else -1
        hours, minutes = map(int, offset_str[4:].split(':'))
        return timezone(timedelta(hours=sign * hours, minutes=sign * minutes))

    def convert_timezone(self, time):
        to_time = time.astimezone(self.to_zone)
        return to_time

class TimeZoneConversionT:
    def __init__(self, current_time, to_utc_offset):
        a = TimeZoneConversionF(current_time, to_utc_offset)
        self.to_zone = a.parse_timezone_offset(to_utc_offset)
        self.converted_time = a.convert_timezone(current_time)

    def get_zone_time(self):
        return self.converted_time