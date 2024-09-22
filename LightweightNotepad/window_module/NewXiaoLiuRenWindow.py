import os

from function.SolarTimeCalculator import SolarTimeCalculator
from XiaoLiuRenJson import Calendar
from function.JsonFile import File
from function.ProjectPathVariables import DATA_FILE_PATH, ICON_PATH
from function.ProjectDictionaryVariables import XLR_DATA
import ttkbootstrap as ttk


class NewX:
    def __init__(self,root_main):
        self.xlr_data_path = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
        xlr_json = File.dict_load(self.xlr_data_path, XLR_DATA)
        self.calendar = xlr_json[0]
        self.time = xlr_json[1]
        self.time_zone = xlr_json[2]
        self.function=xlr_json[3]
        self.root_main = root_main


    def choose(self):

        time_dict = {
            0:self.time_zone,
            1:self.flat_solar_time,
            2:self.true_solar_time
        }



    def time_zone(self):
        choose_dict = {
            0: self.time_qi_gua,
        }

        choose_dict[self.function]()

    def flat_solar_time(self):
        window = ttk.Toplevel(self.root_main)
        window.title("平太阳时")
        window.iconbitmap(ICON_PATH)
        text = ttk.Label(window,text="经度")
        text2 = ttk.Label(window,text="时区")
        text3 = ttk.Label(window,text="日期")
        entry = ttk.Entry(window)
        entry.grid(column=0, row=0, padx=5, pady=5)

    def true_solar_time(self):
        pass

    def time_qi_gua(self):
        p = Calendar(self.calendar)

        p0,p1,p2,p3 = p.function_selection()



a = NewX("a")

a.choose()