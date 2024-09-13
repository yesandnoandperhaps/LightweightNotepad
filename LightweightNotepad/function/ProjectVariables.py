import os

p_ = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(p_, '..'))
data_file_path = os.path.join(p, "data")
icon_file_path = os.path.join(p, "icon")
os.makedirs(data_file_path, exist_ok=True)
a_path = os.path.join(data_file_path, "a")
b_path = os.path.join(data_file_path, "b")
c_path = os.path.join(data_file_path, "c")
d_path = os.path.join(data_file_path, "d")
e_path = os.path.join(data_file_path, "e")
f_path = os.path.join(data_file_path, "f")
g_path = os.path.join(data_file_path,"g")
h_path = os.path.join(data_file_path, "h")
i_path = os.path.join(data_file_path, "i")
j_path = os.path.join(data_file_path, "j")
k_path = os.path.join(data_file_path, "k")
l_path = os.path.join(data_file_path, "l")
m_path = os.path.join(data_file_path, "m")
n_path = os.path.join(data_file_path, "n")
o_path = os.path.join(data_file_path, "o")
p_path = os.path.join(data_file_path, "p")
q_path = os.path.join(data_file_path, "q")
r_path = os.path.join(data_file_path, "r")
s_path = os.path.join(data_file_path,"s")
t_path = os.path.join(data_file_path,"t")
u_path = os.path.join(data_file_path,"u")
v_path = os.path.join(data_file_path,"v")
w_path = os.path.join(data_file_path,"w")
x_path = os.path.join(data_file_path,"x")
y_path = os.path.join(data_file_path,"y")
z_path = os.path.join(data_file_path,"z")
aa_path = os.path.join(data_file_path,"aa")
ab_path = os.path.join(data_file_path,"ab")
w_root2_c_var_2_path = os.path.join(data_file_path, "w_root2_c_var_2_path")
icon_path = os.path.join(icon_file_path, "main_icon.ico")

UTC_TIME = [
                "UTC-12:00", "UTC-11:00", "UTC-10:00", "UTC-09:00", "UTC-09:30", "UTC-08:00", "UTC-07:00",
                "UTC-06:00", "UTC-05:00", "UTC-04:00", "UTC-03:00", "UTC-02:00", "UTC-01:00", "UTC+00:00",
                "UTC-00:00", "UTC+01:00", "UTC+02:00", "UTC+03:00", "UTC+03:30", "UTC+04:00", "UTC+04:30",
                "UTC+05:00", "UTC+05:30", "UTC+05:45", "UTC+06:00", "UTC+06:30", "UTC+07:00", "UTC+08:00",
                "UTC+08:45", "UTC+09:00", "UTC+09:30", "UTC+10:00", "UTC+10:30", "UTC+11:00", "UTC+12:00",
                "UTC+12:45", "UTC+13:00", "UTC+14:00"
]

ZHI_DICT_NUM = {
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

TIAN_GAN_DICT = {
            0:("甲","木","阳"),
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

DI_ZHI_DICT = {
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

YUE_GAN_DICT = {
            "甲":("甲","木","阳"),
            "乙":("乙","木","阴"),
            "丙":("丙","火","阳"),
            "丁":("丁","火","阴"),
            "戊":("戊","土","阳"),
            "己":("己","土","阴"),
            "庚":("庚","金","阳"),
            "辛":("辛","金","阴"),
            "壬":("壬","水","阳"),
            "癸":("癸","水","阴")

}

YUE_ZHI_DICT = {
            1:("寅", "阳", "木", "虎"),
            2:("卯", "阴", "木", "兔"),
            3:("辰", "阳", "土", "龙"),
            4:("巳", "阴", "火", "蛇"),
            5:("午", "阳", "火", "马"),
            6:("未", "阴", "土", "羊"),
            7:("申", "阳", "金", "猴"),
            8:("酉", "阴", "金", "鸡"),
            9:("戌", "阳", "土", "狗"),
            10:("亥", "阴", "水", "猪"),
            11:("子", "阳", "水", "鼠"),
            12:("丑", "阴", "土", "牛")
}

SHI_CHEN_DICT = {
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