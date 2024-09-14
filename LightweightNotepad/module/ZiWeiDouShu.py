import math
import re

from lunar_python import LunarMonth

from function.GregorianCalendarLunar import GregorianCalendarToLunar
from function.ProjectVariables import ZHI_DICT_NUM, TIAN_GAN_DICT, DI_ZHI_DICT, YUE_GAN_DICT, YUE_ZHI_DICT, \
    SHI_CHEN_DICT, S_PATH, T_PATH


# noinspection PyPep8Naming,PyUnboundLocalVariable,DuplicatedCode,SpellCheckingInspection
class ZiWeiDouShu:
    def __init__(self, n,y,r,s):
        self.n = n
        self.y = y
        self.r = r
        self.s = s
    def ZiWeisoushu(self):

        r = re.sub(r'\D+',"",self.n)
        nianGan_num = int(r)%10
        nianZhi_num = int(r)%12
        solar_year = int(r)
        solar_month = int(self.y)
        solar_day = int(self.r)

        '''
        新历转农历
        '''
        
        Lunar_year,Lunar_month,Lunar_day = GregorianCalendarToLunar.to_lunar(solar_year, solar_month, solar_day)

        '''
        年干年支计算
        '''
        
        if self.n == re.sub(r'\D+',"",self.n):#公元后
            if nianGan_num > 3:
                t_nianGan_num = nianGan_num - 3
                nianGan,nianGanwuXing,nianGanyinYang = TIAN_GAN_DICT[t_nianGan_num]
            else:
                t_nianGan_num = nianGan_num - 3 + 10
                nianGan,nianGanwuXing,nianGanyinYang = TIAN_GAN_DICT[t_nianGan_num]
            
            if nianZhi_num > 3:
                t_nianZhi_num = nianZhi_num - 3
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = DI_ZHI_DICT[t_nianZhi_num]
            else:
                t_nianZhi_num = nianZhi_num - 3 + 12
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = DI_ZHI_DICT[t_nianZhi_num]

        else:#公元前
            if nianGan_num < 8:
                t_nianGan_num = 8-nianGan_num
                nianGan,nianGanwuXing,nianGanyinYang = TIAN_GAN_DICT[t_nianGan_num]
            else:
                t_nianGan_num = 8-nianGan_num+10
                nianGan,nianGanwuXing,nianGanyinYang = TIAN_GAN_DICT[t_nianGan_num]
            
            if nianZhi_num < 10:
                t_nianZhi_num = 10 - nianZhi_num
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = DI_ZHI_DICT[t_nianZhi_num]
            else:
                t_nianZhi_num = 10 - nianZhi_num + 12
                nianZhi,nianZhiyinYang,nianZhiwuXing,nianZhishengXiao = DI_ZHI_DICT[t_nianZhi_num]

        '''
        月干月支
        ''' 

        yueZhi,yueZhiyinYang,yueZhiwuXing,yueZhishengXiao =  YUE_ZHI_DICT[Lunar_month]

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

        yueGan,yueGanwuXing,yueGanyinYang = YUE_GAN_DICT[yueGan]

        '''
        儒略日和日干支
        '''

        def ce2jd(year,month,d):
            if month in [1,2]:
                M = month + 12
                Y = year - 1
            else:
                Y = year
                M = month
            B = 0
            if Y>1582 or (Y==1582 and M>10) or (Y==1582 and M==10 and d>=15):
                B = 2 - int(Y/100) + int(Y/400)  #公元1582年10月15日以后每400年减少3闰
            JD_ = math.floor(365.25 * (Y + 4716)) + int(30.6 * (M + 1)) + d + B - 1524.5
            MJD_ = "无"
            #JD = math.floor(365.25*(Y+4712))+int(30.6*(M+1))+D+B-63.5
            if Y>1858 or (Y==1858 and M>11) or (Y==1858 and M==11 and d>=17):
                MJD_ = int(JD_ - 2400000.5)
                return JD_,MJD_
            return JD_,MJD_
        
        if self.n == re.sub(r'\D+',"",self.n):
            JD,MJD = ce2jd(int(self.n),int(self.y),int(self.r))
        else:
            n_new = -int(re.sub(r'\D+',"",self.n))
            JD,MJD = ce2jd(n_new,int(self.y),int(self.r))
        
        NOONJD = math.ceil(JD)

        riGan_num = 1+(NOONJD-1)%10
        riZhi_num = 1+(NOONJD+1)%12

        riGan,riGanwuXing,ruGanyinYang = TIAN_GAN_DICT[riGan_num]
        riZhi,riZhiyinYang,riZhiwuXing,ruZhishengXiao = DI_ZHI_DICT[riZhi_num]
        
        

        '''
        时干支
        '''
        
        #print(JD,NOONJD)

        shiChen,shiChenyinYang,shiChenwuXing,shiChenshengXiao = SHI_CHEN_DICT[int(self.s)]

        shiGan,shiGanwuXing,shiGanyinYang = TIAN_GAN_DICT[((riGan_num*12 + ZHI_DICT_NUM[shiChen])-1)%10]


        

        '''
        紫微斗数闰月作下月
        '''
        def ZiWeidoushuRunyue_is_next_month():
            runYue = LunarMonth.fromYm(Lunar_year, Lunar_month)
            yes_runYue = ""
            if runYue.isLeap():
                yes_runYue = Lunar_month + 1
                if yes_runYue > 12:
                    yes_runYue = 1
                return yes_runYue
            else:
                return Lunar_month

        '''
        紫微斗数闰月中分界
        ''' 
        def ZiWeidoushuRunyue_is_middle_month():
            runYue = LunarMonth.fromYm(Lunar_year, Lunar_month)
            yes_runYue = ""
            if runYue.isLeap():
                if Lunar_month <= 15:
                    return Lunar_month
                else:
                    yes_runYue = Lunar_month + 1
                    if yes_runYue > 12:
                        yes_runYue = 1
                    return yes_runYue
            else:
                return Lunar_month

        def load_down_box2():
            try:
                with open(S_PATH, 'r', encoding='utf-8') as f:
                    return f.read()
            except FileNotFoundError:
                pass

        def load_down_box3():
            try:
                with open(T_PATH, 'r', encoding='utf-8') as f:
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
                birth_month = Lunar_month
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
        '''
        五行局
        '''
        match nianGan:
            case "甲"|"己":
                wuXingju_nianGan = "甲己"
            case "乙"|"庚":
                wuXingju_nianGan = "乙庚" 
            case "丙"|"辛":
                wuXingju_nianGan = "丙辛"
            case "丁"|"壬":
                wuXingju_nianGan = "丁壬"
            case "戊"|"癸":
                wuXingju_nianGan = "戊癸"
        
        match Ming:
            case "子"|"丑":
                wuXingju_Ming = "子丑"
            case "寅"|"卯":
                wuXingju_Ming = "寅卯"
            case "辰"|"巳":
                wuXingju_Ming = "辰巳"
            case "午"|"未":
                wuXingju_Ming = "午未"
            case "申"|"酉":
                wuXingju_Ming = "申酉"
            case "戌"|"亥":
                wuXingju_Ming = "戌亥"
                
        wuXingju_nianGan_x = ["戊癸","丁壬","丙辛","乙庚","甲己"]
        wuXingju_Ming_y = ["子丑", "寅卯", "辰巳", "午未", "申酉", "戌亥"]
        
        
        wuXingju1 = ["金四局", "木三局", "土五局", "火六局", "水二局"]
        wuXingju2 = ["水二局", "金四局", "木三局", "土五局", "火六局"]
        wuXingju3 = ["土五局", "火六局", "水二局", "金四局", "木三局"]
        wuXingju4 = ["火六局", "水二局", "金四局", "木三局", "土五局"]
        wuXingju5 = ["木三局", "土五局", "火六局", "水二局", "金四局"]
        wuXingju6 = ["水二局", "金四局", "木三局", "土五局", "火六局"]
        wuXingju_Ming_ty = wuXingju_Ming_y.index(wuXingju_Ming)

        match wuXingju_Ming_ty:
            case 0:
                wuXingju = wuXingju1[wuXingju_nianGan_x.index(wuXingju_nianGan)]
            case 1:
                wuXingju = wuXingju2[wuXingju_nianGan_x.index(wuXingju_nianGan)]
            case 2:
                wuXingju = wuXingju3[wuXingju_nianGan_x.index(wuXingju_nianGan)]
            case 3:
                wuXingju = wuXingju4[wuXingju_nianGan_x.index(wuXingju_nianGan)]
            case 4:
                wuXingju = wuXingju5[wuXingju_nianGan_x.index(wuXingju_nianGan)]
            case 5:
                wuXingju = wuXingju6[wuXingju_nianGan_x.index(wuXingju_nianGan)]

        '''
        定紫微
        '''
        ziWei_wuXingju_x = ["火六局", "土五局", "金四局", "木三局", "水二局"]
        shenRi_y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

        ziWei1  = ["酉", "午", "亥", "辰", "丑"]
        ziWei2  = ["午", "亥", "辰", "丑", "寅"]
        ziWei3  = ["亥", "辰", "丑", "寅", "寅"]
        ziWei4  = ["辰", "丑", "寅", "巳", "卯"]
        ziWei5  = ["丑", "寅", "子", "寅", "卯"]
        ziWei6  = ["寅", "未", "巳", "卯", "辰"]
        ziWei7  = ["戌", "子", "寅", "午", "辰"]
        ziWei8  = ["未", "巳", "卯", "卯", "巳"]
        ziWei9  = ["子", "寅", "丑", "辰", "巳"]
        ziWei10 = ["巳", "卯", "午", "未", "午"]
        ziWei11 = ["寅", "申", "卯", "辰", "午"]
        ziWei12 = ["卯", "丑", "辰", "巳", "未"]
        ziWei13 = ["亥", "午", "寅", "申", "未"]
        ziWei14 = ["申", "卯", "未", "巳", "申"]
        ziWei15 = ["丑", "辰", "辰", "午", "申"]
        ziWei16 = ["午", "酉", "巳", "酉", "酉"]
        ziWei17 = ["卯", "寅", "卯", "午", "酉"]
        ziWei18 = ["辰", "未", "申", "未", "戌"]
        ziWei19 = ["子", "辰", "巳", "戌", "戌"]
        ziWei20 = ["酉", "巳", "午", "未", "亥"]
        ziWei21 = ["寅", "戌", "辰", "申", "亥"]
        ziWei22 = ["未", "卯", "酉", "亥", "子"]
        ziWei23 = ["辰", "申", "午", "申", "子"]
        ziWei24 = ["巳", "巳", "未", "酉", "丑"]
        ziWei25 = ["丑", "午", "巳", "子", "丑"]
        ziWei26 = ["戌", "亥", "戌", "酉", "寅"]
        ziWei27 = ["卯", "辰", "未", "戌", "寅"]
        ziWei28 = ["申", "酉", "申", "丑", "卯"]
        ziWei29 = ["巳", "午", "午", "戌", "卯"]
        ziWei30 = ["午", "未", "亥", "亥", "辰"]
        shenRi_ty = shenRi_y.index(Lunar_day)

        match shenRi_ty:
            case 0:
                ziWei = ziWei1[ziWei_wuXingju_x.index(wuXingju)]
            case 1:
                ziWei = ziWei2[ziWei_wuXingju_x.index(wuXingju)]
            case 2:
                ziWei = ziWei3[ziWei_wuXingju_x.index(wuXingju)]
            case 3:
                ziWei = ziWei4[ziWei_wuXingju_x.index(wuXingju)]
            case 4:
                ziWei = ziWei5[ziWei_wuXingju_x.index(wuXingju)]
            case 5:
                ziWei = ziWei6[ziWei_wuXingju_x.index(wuXingju)]
            case 6:
                ziWei = ziWei7[ziWei_wuXingju_x.index(wuXingju)]
            case 7:
                ziWei = ziWei8[ziWei_wuXingju_x.index(wuXingju)]
            case 8:
                ziWei = ziWei9[ziWei_wuXingju_x.index(wuXingju)]
            case 9:
                ziWei = ziWei10[ziWei_wuXingju_x.index(wuXingju)]
            case 10:
                ziWei = ziWei11[ziWei_wuXingju_x.index(wuXingju)]
            case 11:
                ziWei = ziWei12[ziWei_wuXingju_x.index(wuXingju)]
            case 12:
                ziWei = ziWei13[ziWei_wuXingju_x.index(wuXingju)]
            case 13: 
                ziWei = ziWei14[ziWei_wuXingju_x.index(wuXingju)]
            case 14:    
                ziWei = ziWei15[ziWei_wuXingju_x.index(wuXingju)]
            case 15:    
                ziWei = ziWei16[ziWei_wuXingju_x.index(wuXingju)]
            case 16:  
                ziWei = ziWei17[ziWei_wuXingju_x.index(wuXingju)]
            case 17:      
                ziWei = ziWei18[ziWei_wuXingju_x.index(wuXingju)]
            case 18:  
                ziWei = ziWei19[ziWei_wuXingju_x.index(wuXingju)]
            case 19:  
                ziWei = ziWei20[ziWei_wuXingju_x.index(wuXingju)]
            case 20:  
                ziWei = ziWei21[ziWei_wuXingju_x.index(wuXingju)]
            case 21:  
                ziWei = ziWei22[ziWei_wuXingju_x.index(wuXingju)]
            case 22:  
                ziWei = ziWei23[ziWei_wuXingju_x.index(wuXingju)]
            case 23:
                ziWei = ziWei24[ziWei_wuXingju_x.index(wuXingju)]
            case 24:  
                ziWei = ziWei25[ziWei_wuXingju_x.index(wuXingju)]
            case 25:  
                ziWei = ziWei26[ziWei_wuXingju_x.index(wuXingju)]
            case 26:  
                ziWei = ziWei27[ziWei_wuXingju_x.index(wuXingju)]
            case 27:  
                ziWei = ziWei28[ziWei_wuXingju_x.index(wuXingju)]
            case 28:  
                ziWei = ziWei29[ziWei_wuXingju_x.index(wuXingju)]
            case 29:  
                ziWei = ziWei30[ziWei_wuXingju_x.index(wuXingju)]
        



        return nianGan,nianGanwuXing,nianGanyinYang\
            ,nianZhi,nianZhiwuXing,nianZhiyinYang,nianZhishengXiao\
                ,yueGan,yueGanwuXing,yueGanyinYang\
                    ,yueZhi,yueZhiwuXing,yueZhiyinYang,yueZhishengXiao\
                    ,shiChen,shiChenwuXing,shiChenyinYang,shiChenshengXiao\
                        ,Ming,Shen,wuXingju,ziWei\
                            ,JD,NOONJD,MJD\
                                ,riGan,riGanwuXing,ruGanyinYang\
                                    ,riZhi,riZhiwuXing,riZhiyinYang,ruZhishengXiao\
                                    ,shiGan,shiGanwuXing,shiGanyinYang\
                                    ,Lunar_day
            

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
#ziwei = ZiWeidoushu('2024', '7', '18', '24')
#result = ziwei.ZiWeisoushu()
#print(result)

