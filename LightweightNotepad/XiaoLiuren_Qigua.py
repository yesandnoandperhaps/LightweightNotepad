from datetime import datetime
import math
import os
import re
from lunar_python import LunarMonth,Solar
from scipy.special.cython_special import shichi

from Gregorian_calendar_Lunar import GregorianCalendarToLunar
shiChen_dict = {
            1: ("丑", "阴", "土", "牛"),
            2: ("丑", "阴", "土", "牛"),
            3: ("寅", "阳", "木", "虎"),
            4: ("寅", "阳", "木", "虎"),
            5: ("卯", "阴", "木", "兔"),
            6: ("卯", "阴", "木", "兔"),
            7: ("辰", "阳", "土", "龙"),
            8: ("辰", "阳", "土", "龙"),
            9: ("巳", "阴", "火", "蛇"),
            10: ("巳", "阴", "火", "蛇"),
            11: ("午", "阳", "火", "马"),
            12: ("午", "阳", "火", "马"),
            13: ("未", "阴", "土", "羊"),
            14: ("未", "阴", "土", "羊"),
            15: ("申", "阳", "金", "猴"),
            16: ("申", "阳", "金", "猴"),
            17: ("酉", "阴", "金", "鸡"),
            18: ("酉", "阴", "金", "鸡"),
            19: ("戌", "阳", "土", "狗"),
            20: ("戌", "阳", "土", "狗"),
            21: ("亥", "阴", "水", "猪"),
            22: ("亥", "阴", "水", "猪"),
            23: ("子", "阳", "水", "鼠"),
            24: ("子", "阳", "水", "鼠"),
            }

current_time = datetime.now()



print("年：", year)
print("月：", month)
print("日：", day)
print("小时：", hour)
print("分钟：", minute)

Lunar_year,Lunar_month,Lunar_day = GregorianCalendarToLunar.to_lunar(year, month, day)

class XiaoLiuRenQiGua:
    def __init__(self,text):

        year = current_time.year
        month = current_time.month
        day = current_time.day
        hour = current_time.hour
        minute = current_time.minute

        solar = Solar.fromDate(current_time)
        lunar = solar.getLunar()
        print (lunar.toFullString())
