import os
import re
from lunardate import LunarDate
from datetime import datetime
from lunar_python import LunarMonth,Lunar,LunarYear
import numpy as np

p = os.path.dirname(__file__)

class ZiWeidoushu(object):
    def __init__(self, n,y,r,s):
        self.n = n
        self.y = y
        self.r = r
        self.s = s
    def ZiWeisoushu(self):
        
        tianGan_dict = {
            1:("甲","木","阳"),
            2:("乙","木","阴"),
            3:("丙","火","阳"),
            4:("丁","火","阴"),
            5:("戊","土","阳"),
            6:("己","土","阴"),
            7:("庚","金","阳"),
            8:("辛","金","阴"),
            9:("壬","水","阳"),
            10:("癸","水","阴")
        }
        diZhi_dict = {
            1: ("子", "阳", "水", "鼠"),
            2: ("丑", "阴", "土", "牛"),
            3: ("寅", "阳", "木", "虎"),
            4: ("卯", "阴", "木", "兔"),
            5: ("辰", "阳", "土", "龙"),
            6: ("巳", "阴", "火", "蛇"),
            7: ("午", "阳", "火", "马"),
            8: ("未", "阴", "土", "羊"),
            9: ("申", "阳", "金", "猴"),
            10: ("酉", "阴", "金", "鸡"),
            11: ("戌", "阳", "土", "狗"),
            12: ("亥", "阴", "水", "猪")
            }
        yueZhi_dict = {
            1:"寅",
            2:"卯",
            3:"辰",
            4:"巳",
            5:"午",
            6:"未",
            7:"申",
            8:"酉",
            9:"戌",
            10:"亥",
            11:"子",
            12:"丑"
            }
        shiChen_dict = {
            1: "丑", 
            2: "丑",
            3: "寅", 
            4: "寅", 
            5: "卯",
            6: "卯",
            7: "辰",
            8: "辰", 
            9: "巳时", 
            10: "巳时", 
            11: "午时", 
            12: "午时",
            13: "未时", 
            14: "未时",
            15: "申时", 
            16: "申时", 
            17: "酉时", 
            18: "酉时", 
            19: "戌时", 
            20: "戌时", 
            21: "亥时", 
            22: "亥时",
            23: "子",
            24: "子"
            }
        Zhi_dict = {
            "子":1,
            "丑":2,
            "寅":3,
            "卯":4,
            "辰":5,
            "巳":6,
            "午":7,
            "未":8,
            "申":9,
            "酉":10,
            "戌":11,
            "亥":12
        }

        
        r = re.sub(r'[^\d]+',"",self.n)
        nianGan_num = int(r)%10
        nianZhi_num = int(r)%12
        solar_year = int(r)
        solar_month = int(self.y)
        solar_day = int(self.r)

        '''
        新历转农历
        '''

        def convert_solar_to_lunar(year, month, day):
            solar_date = datetime(year, month, day)
            lunar_date = LunarDate.fromSolarDate(solar_date.year, solar_date.month, solar_date.day)
            return lunar_date
        lunar_date = convert_solar_to_lunar(solar_year, solar_month, solar_day)

        '''
        年干年支计算
        '''
        
        if self.n == str(int(self.n)):#公元后
            if nianGan_num > 3:
                t_nianGan_num = nianGan_num - 3
                nianGan,nianGanwuXing,nianGanyinYang = tianGan_dict[t_nianGan_num]
            else:
                t_nianGan_num = nianGan_num - 3 + 10
                nianGan,nianGanwuXing,nianGanyinYang = tianGan_dict[t_nianGan_num]
            
            if nianZhi_num > 3:
                t_nianZhi_num = nianZhi_num - 3
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = diZhi_dict[t_nianZhi_num]
            else:
                t_nianZhi_num = nianZhi_num - 3 + 12
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = diZhi_dict[t_nianZhi_num]

        else:#公元前
            if nianGan_num < 8:
                t_nianGan_num = 8-nianGan_num
                nianGan,nianGanwuXing,nianGanyinYang = tianGan_dict[t_nianGan_num]
            else:
                t_nianGan_num = 8-nianGan_num+10
                nianGan,nianGanwuXing,nianGanyinYang = tianGan_dict[t_nianGan_num]
            
            if nianZhi_num < 10:
                t_nianZhi_num = 10 - nianZhi_num
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = diZhi_dict[t_nianZhi_num]
            else:
                t_nianZhi_num = 10 - nianZhi_num + 12
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = diZhi_dict[t_nianZhi_num]

        '''
        月干月支
        ''' 

        yueZhi =  yueZhi_dict[solar_month]

        yueGan = ""

        match nianGan:
            case "甲" | "己":
                match yueZhi:
                    case "寅":
                        yueGan = "丙"
                    case "卯":
                        yueGan = "丁"
                    case "辰":
                        yueGan = "戊"
                    case "巳":
                        yueGan = "己"
                    case "午":
                        yueGan = "庚"
                    case "未":
                        yueGan = "辛"
                    case "申":
                        yueGan = "壬"
                    case "酉":
                        yueGan = "癸"
                    case "戌":
                        yueGan = "甲"
                    case "亥":
                        yueGan = "乙"
                    case "子":
                        yueGan = "丙"
                    case "丑":
                        yueGan = "子"
            case "乙" | "庚":
                match yueZhi:
                    case "寅":
                        yueGan = "戊"
                    case "卯":
                        yueGan = "己"
                    case "辰":
                        yueGan = "庚"
                    case "巳":
                        yueGan = "辛"
                    case "午":
                        yueGan = "壬"
                    case "未":
                        yueGan = "癸"
                    case "申":
                        yueGan = "甲"
                    case "酉":
                        yueGan = "乙"
                    case "戌":
                        yueGan = "丙"
                    case "亥":
                        yueGan = "丁"
                    case "子":
                        yueGan = "戊"
                    case "丑":
                        yueGan = "己"
            case "丙" | "辛":
                match yueZhi:
                    case "寅":
                        yueGan = "庚"
                    case "卯":
                        yueGan = "辛"
                    case "辰":
                        yueGan = "壬"
                    case "巳":
                        yueGan = "癸"
                    case "午":
                        yueGan = "甲"
                    case "未":
                        yueGan = "乙"
                    case "申":
                        yueGan = "丙"
                    case "酉":
                        yueGan = "丁"
                    case "戌":
                        yueGan = "戊"
                    case "亥":
                        yueGan = "己"
                    case "子":
                        yueGan = "庚"
                    case "丑":
                        yueGan = "辛"
            case "丁" | "壬":
                match yueZhi:
                    case "寅":
                        yueGan = "壬"
                    case "卯":
                        yueGan = "癸"
                    case "辰":
                        yueGan = "甲"
                    case "巳":
                        yueGan = "乙"
                    case "午":
                        yueGan = "丙"
                    case "未":
                        yueGan = "丁"
                    case "申":
                        yueGan = "戊"
                    case "酉":
                        yueGan = "己"
                    case "戌":
                        yueGan = "庚"
                    case "亥":
                        yueGan = "辛"
                    case "子":
                        yueGan = "壬"
                    case "丑":
                        yueGan = "癸"
            case "戊" | "癸":
                match yueZhi:
                    case "寅":
                        yueGan = "甲"
                    case "卯":
                        yueGan = "乙"
                    case "辰":
                        yueGan = "丙"
                    case "巳":
                        yueGan = "丁"
                    case "午":
                        yueGan = "戊"
                    case "未":
                        yueGan = "己"
                    case "申":
                        yueGan = "庚"
                    case "酉":
                        yueGan = "辛"
                    case "戌":
                        yueGan = "壬"
                    case "亥":
                        yueGan = "癸"
                    case "子":
                        yueGan = "甲"
                    case "丑":
                        yueGan = "乙"



        
        
        '''
        生时转换
        '''
        shiChen = shiChen_dict[int(self.s)]

        '''
        紫微斗数闰月作下月
        '''
        def ZiWeidoushuRunyue_is_next_month():
            runYue = LunarMonth.fromYm(lunar_date.year, lunar_date.month)
            yes_runYue = ""
            if runYue.isLeap():
                yes_runYue = lunar_date.month + 1
                if yes_runYue > 12:
                    yes_runYue = 1
                return yes_runYue
            else:
                return lunar_date.month

        '''
        紫微斗数闰月中分界
        ''' 
        def ZiWeidoushuRunyue_is_middle_month():
            runYue = LunarMonth.fromYm(lunar_date.year, lunar_date.month)
            yes_runYue = ""
            if runYue.isLeap():
                if lunar_date.month <= 15:
                    return lunar_date.month
                else:
                    yes_runYue = lunar_date.month + 1
                    if yes_runYue > 12:
                        yes_runYue = 1
                    return yes_runYue
            else:
                return lunar_date.month
        

        s_path = p + "\\" + "s"
        t_path = p + "\\" + "t"

        def load_down_box2():
            try:
                with open(s_path, 'r',encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                pass

        def load_down_box3():
            try:
                with open(t_path, 'r',encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                pass
        
        '''
        身宫|命宫判断
        '''

        t = str(load_down_box2() or "作下月")
        t2 = str(load_down_box3() or "子时视明日")

        match t:
            case "作下月":
                birth_month = ZiWeidoushuRunyue_is_next_month()
            case "作本月":
                birth_month = lunar_date.month
            case "月中为界":
                birth_month = ZiWeidoushuRunyue_is_middle_month()
        '''
        命宫矩阵
        '''
        Ming_x = [12,11,10,9,8,7,6,5,4,3,2,1,0]
        Ming_y = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌","亥"]

        Ming1 = ["丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅"]
        Ming2 = ["子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑"]
        Ming3 = ["亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子"]
        Ming4 = ["戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥"]
        Ming5 = ["酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌"]
        Ming6 = ["申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉"]
        Ming7 = ["未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申"]
        Ming8 = ["午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未"]
        Ming9 = ["巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午"]
        Ming10 = ["辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午","巳"]
        Ming11 = ["卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳","辰"]
        Ming12 = ["寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰","卯"]
        Ming_ty = Ming_y.index(shiChen)#时辰返回索引

        match Ming_ty:
            case 0:
                Ming = Ming1[Ming_x.index(birth_month)]
            case 1:
                Ming = Ming2[Ming_x.index(birth_month)]
            case 2:
                Ming = Ming3[Ming_x.index(birth_month)]
            case 3:
                Ming = Ming4[Ming_x.index(birth_month)]
            case 4:
                Ming = Ming5[Ming_x.index(birth_month)]
            case 5:
                Ming = Ming6[Ming_x.index(birth_month)]
            case 6:
                Ming = Ming7[Ming_x.index(birth_month)]
            case 7:
                Ming = Ming8[Ming_x.index(birth_month)]
            case 8:
                Ming = Ming9[Ming_x.index(birth_month)]
            case 9:
                Ming = Ming10[Ming_x.index(birth_month)]
            case 10:
                Ming = Ming11[Ming_x.index(birth_month)]
            case 11:
                Ming = Ming12[Ming_x.index(birth_month)]

        '''
        身宫矩阵
        '''
        Shen_x = [12,11,10,9,8,7,6,5,4,3,2,1,0]
        Shen_y = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌","亥"]

        Shen1 = ["丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅"]
        Shen2 = ["寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯"]
        Shen3 = ["卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰"]
        Shen4 = ["辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "巳"]
        Shen5 = ["巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午"]
        Shen6 = ["午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未"]
        Shen7 = ["未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申"]
        Shen8 = ["申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉"]
        Shen9 = ["酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥", "戌"]
        Shen10 = ["戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子", "亥"]
        Shen11 = ["亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑", "子"]
        Shen12 = ["子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯", "寅", "丑"]
        Shen_ty = Shen_y.index(shiChen)

        match Shen_ty:
            case 0:
                Shen = Shen1[Shen_x.index(birth_month)]
            case 1:
                Shen = Shen2[Shen_x.index(birth_month)]
            case 2:
                Shen = Shen3[Shen_x.index(birth_month)]
            case 3:
                Shen = Shen4[Shen_x.index(birth_month)]
            case 4:
                Shen = Shen5[Shen_x.index(birth_month)]
            case 5:
                Shen = Shen6[Shen_x.index(birth_month)]
            case 6:
                Shen = Shen7[Shen_x.index(birth_month)]
            case 7:
                Shen = Shen8[Shen_x.index(birth_month)]
            case 8:
                Shen = Shen9[Shen_x.index(birth_month)]
            case 9:
                Shen = Shen10[Shen_x.index(birth_month)]
            case 10:
                Shen = Shen11[Shen_x.index(birth_month)]
            case 11:
                Shen = Shen12[Shen_x.index(birth_month)]

        return nianGan,nianGanwuXing,nianGanyinYang,nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao,yueGan,yueZhi,shiChen,Ming
            

'''
年干=N-3(N＞3)或N-3+10(N≤3)，N=年号除以10的余数=年号个位数。
年支=N-3(N＞3)或N-3+12(N≤3)，N=年号除以12的余数。
'''
'''
年干=8-N(N＜8)或8-N+10(N≧8)，N=年号除以10的余数=年号个位数。
年支=10-N(N＜10)或10-N+12(N≧10)，N=年号除以12的余数。
前22的年干=8-2=6=己，
前22的年支=10-10+12=12=亥，
前159年的年干=8-9+10=9=壬；
前159年的年支=10-3=7=午；
'''
'''
月天干=年份天干对应数字×2+农历月份，
得出的数字如果是偶数，就减十，直到减为单数为止;月地支不用算，农历月份对应的地支就是月地支。
'''
ziwei = ZiWeidoushu('2023', '2', '28', '1')
result = ziwei.ZiWeisoushu()
print(result)

