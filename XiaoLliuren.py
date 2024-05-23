import random
import os
import math
import numpy as np
from sympy import *
import time
import warnings
import sys

p = os.path.dirname(__file__)
g_path = os.path.join(p,"g")
class T():
    def __init__(self, a=0, b=0, c=0, bottom=0, high=0, pax=0, pbx=0, pcx=0, pay=0, pby=0, pcy=0, paz=0, pbz=0, pcz=0,):
        self.SidesA = a
        self.SidesB = b
        self.SidesC = c
        self.bottom = bottom
        self.high = high
        self.CoordinatePointAX = pax
        self.CoordinatePointBX = pbx
        self.CoordinatePointCX = pcx
        self.CoordinatePointAY = pay
        self.CoordinatePointBY = pby
        self.CoordinatePointCY = pcy
        self.CoordinatePointAZ = paz
        self.CoordinatePointBZ = pbz
        self.CoordinatePointCZ = pcz

    def incentre(self):
            a = math.sqrt((self.CoordinatePointBX - self.CoordinatePointCX) ** 2 + (
                    self.CoordinatePointBY - self.CoordinatePointCY) ** 2 + (
                                  self.CoordinatePointBZ - self.CoordinatePointCZ) ** 2)
            b = math.sqrt((self.CoordinatePointCX - self.CoordinatePointAX) ** 2 + (
                    self.CoordinatePointCY - self.CoordinatePointAY) ** 2 + (
                                  self.CoordinatePointCZ - self.CoordinatePointAZ) ** 2)
            c = math.sqrt((self.CoordinatePointAX - self.CoordinatePointBX) ** 2 + (
                    self.CoordinatePointAY - self.CoordinatePointBY) ** 2 + (
                                  self.CoordinatePointAZ - self.CoordinatePointBZ) ** 2)

            spatial_incentre_x = (
                                         a * self.CoordinatePointAX + b * self.CoordinatePointBX + c * self.CoordinatePointCX) / (
                                         a + b + c)
            spatial_incentre_y = (
                                         a * self.CoordinatePointAY + b * self.CoordinatePointBY + c * self.CoordinatePointCY) / (
                                         a + b + c)
            spatial_incentre_z = (
                                         a * self.CoordinatePointAZ + b * self.CoordinatePointBZ + c * self.CoordinatePointCZ) / (
                                         a + b + c)
            spatial_incentre_xyz = (spatial_incentre_x, spatial_incentre_y, spatial_incentre_z)
            return spatial_incentre_xyz
def numgua():
    max_value = sys.maxsize
    min_value = -sys.maxsize - 1
    new_num1 = round(random.uniform(0, max_value))
    new_num2 = round(random.uniform(0, max_value))
    new_num3 = round(random.uniform(0, max_value))
    天宫 = new_num1 % 6
    人宫 = (new_num1 + new_num2 - 1) % 6
    地宫 = (new_num1 + new_num2 + new_num3 - 2) % 6
    宫位 = {1: "大安",
                     2: "流连",
                     3: "速喜",
                     4: "赤口",
                     5: "小吉",
                     6: "空亡",
                     0: "空亡"
                     }
    initial_text1 = "天宫：{}\n".format(宫位.get(天宫, "空亡，"))
    initial_text1 += "人宫：{}\n".format(宫位.get(人宫, "空亡，"))
    initial_text1 += "地宫：{}\n".format(宫位.get(地宫, "空亡，"))
    
    with open(g_path, 'w',encoding='utf-8') as file:file.write(initial_text1)
    return initial_text1