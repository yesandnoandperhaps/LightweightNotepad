from lunardate import LunarDate
from datetime import datetime
class ZiWeidoushu(object):
    def __init__(self, n,y,r,s):
        self.n = n
        self.y = y
        self.r = r
        self.s = s
    def incentre(self):
        tianGan_list=["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
        diZhi_list=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
        shengXiao_list=["鼠","牛","虎","兔","龙","蛇","马","羊","猴","鸡","狗","猪"]
        wuXing_yinYang_dict = {
    "甲": ("木", "阳"),
    "乙": ("木", "阴"),
    "丙": ("火", "阳"),
    "丁": ("火", "阴"),
    "戊": ("土", "阳"),
    "己": ("土", "阴"),
    "庚": ("金", "阳"),
    "辛": ("金", "阴"),
    "壬": ("水", "阳"),
    "癸": ("水", "阴")
    }
        if self.n-2020>=0:
            tgPointer=abs(self.n-2020)%10+6
            if tgPointer>9:
                tgPointer=abs(self.n-2020)%10+6-10
            else:
                tgPointer=abs(self.n-2020)%10+6
            dzPointer=abs(self.n-2020)%12
        else:
            if abs(self.n-2020)%10==0:
                tgPointer=abs(self.n-2020)%10+6
            else:
                tgPointer=6-abs(self.n-2020)%10

            if abs(self.n-2020)%12==0:
                dzPointer=abs(self.n-2020)%12
            else:
                dzPointer=12-(abs(self.n-2020)%12)

        if tgPointer>=0 and tgPointer<=9: 
            tianGan=tianGan_list[tgPointer]
        else:
            tianGan=tianGan_list[tgPointer+10]

        diZhi = diZhi_list[dzPointer]
        shengXiao = shengXiao_list[dzPointer]
        wuXing, yinYang = wuXing_yinYang_dict[tianGan]




		

