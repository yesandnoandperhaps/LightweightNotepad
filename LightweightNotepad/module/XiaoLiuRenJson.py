from datetime import datetime

from lunar_python import Solar, Lunar, LunarMonth

from function.ProjectDictionaryVariables import SHI_CHEN_DICT
from function.ProjectFunctions import utc
from function.TimeZoneConversion import TimeZoneConversionT


class Calendar:
    def __init__(self, li_fa, shi_chen, run_yue):
        self.li_fa = li_fa
        self.shi_chen_issue = shi_chen
        self.run_yue = run_yue
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

        return function_selection[self.li_fa]()

    @staticmethod
    def time_partition(minute,second,d_):
        if minute <= 59 and second <= 59:
            pass
        else:
            d_.next(1)
        return d_

    def gregorian_calendar(self):
        d = Solar.fromDate(self.converted_time)
        a0,a1,a2,a3=SHI_CHEN_DICT[self.converted_time.shi_chen_issue]

        if a0 == "子":
            if self.shi_chen_issue == 0:
                self.converted_time = d.next(1)
            elif self.shi_chen_issue == 1:
                pass
            else:
                self.converted_time = Calendar.time_partition(self.converted_time.minute, self.converted_time.second, d)

        return self.converted_time.year, self.converted_time.month, self.converted_time.day, SHI_CHEN_DICT[self.converted_time.shi_chen_issue]


    def chinese_calendar(self):
        return ChineseCalendar(self.converted_time, self.shi_chen_issue,self.run_yue).get_lunar_date()

    def taoism_calendar(self):
        lunar_year, lunar_month, lunar_day, lunar_hour = self.chinese_calendar()
        lunar = Lunar.fromYmd(lunar_year, lunar_month, lunar_day)
        tao = lunar.getTao()
        dao_year = tao.getYear()
        return dao_year, lunar_month, lunar_day, lunar_hour


class ChineseCalendar:
    def __init__(self, current_time, shi_chen, run_yue):

        self.converted_time = current_time
        self.shi_chen = shi_chen
        self.run_yue = run_yue


        self.d = Lunar.fromDate(self.converted_time)
        self.lunar_year = self.d.getYear()
        self.lunar_month = self.d.getMonth()
        self.lunar_day = self.d.getDay()
        self.a0 = self.d.getTimeZhi()
        self.run_yue_month = LunarMonth.fromYm(self.lunar_year, self.lunar_month)
        self.judgement_runyue()
        self.judgement_shichen()


    def get_lunar_date(self):
        return self.lunar_year, self.lunar_month, self.lunar_day, self.a0

    def judgement_shichen(self):
        if self.a0 == "子":
            if self.shi_chen == 0:
                self.converted_time = self.d.next(1)
                self.lunar_year = self.converted_time.getYear()
                self.lunar_month = self.converted_time.getMonth()
                self.lunar_day = self.converted_time.getDay()
            elif self.shi_chen == 1:
                pass
            else:
                self.converted_time = Calendar.time_partition(self.converted_time.minute, self.converted_time.second, self.d)
                self.lunar_year = self.converted_time.getYear()
                self.lunar_month = self.converted_time.getMonth()
                self.lunar_day = self.converted_time.getDay()

    def judgement_runyue(self):
        if self.run_yue_month.isLeap():
            if self.run_yue == 0:
                pass
            elif self.run_yue == 1:
                f = self.run_yue_month.getDayCount()
                self.run_yue_month.next(1)
                t = self.run_yue_month.getDayCount()

                if f == t:
                    self.lunar_year = self.run_yue_month.getYear()
                    self.lunar_month = self.run_yue_month.getMonth()
                else:
                    if f == 30:
                        self.lunar_year = self.run_yue_month.getYear()
                        self.lunar_month = self.run_yue_month.getMonth()
                        self.lunar_day = 1
                    else:
                        self.lunar_year = self.run_yue_month.getYear()
                        self.lunar_month = self.run_yue_month.getMonth()


p = Calendar(1,1,1)
print(p.function_selection())