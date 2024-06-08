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
l_path = os.path.join(p, "l")
m_path = os.path.join(p, "m")
def load9():
    try:
        with open(l_path, 'r',encoding='utf-8') as f:
                return f.read()
    except FileNotFoundError:
        pass
def load10():
    try:
        with open(m_path, 'r',encoding='utf-8') as f:
                return f.read()
    except FileNotFoundError:
        pass
v5 = int(load9() or 0)
v6 = int(load10() or 0)

class T:
    
    def __init__(self, pax=0, pbx=0, pcx=0, pay=0, pby=0, pcy=0, paz=0, pbz=0, pcz=0):
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
            spatial_incentre_xyz = spatial_incentre_x+spatial_incentre_y+spatial_incentre_z
            return spatial_incentre_xyz

class num:
    def __init__(self,t=0,r=0,d=0):
        self.t = t
        self.r = r
        self.d = d
    
    def judgment(self):
         match self.t:
              case 1:
                   #D
                   match self.r:
                        case 1:
                             #D
                             pass
                        case 2:
                             #L
                             pass
                        case 3:
                             #S
                             pass
                        case 4:
                             #C
                             pass
                        case 5:
                             #X
                             pass
                        case 0:
                             #K
                             pass
                   pass
              case 2:
                   #L
                   pass
              case 3:
                   #S
                   pass
              case 4:
                   #X
                   pass
              case 5:
                   #C
                   pass
              case 0:
                   #K
                   pass
                                   
                                       
                   

def numgua():
    new_num1 = round(random.uniform(0, 5))
    new_num2 = round(random.uniform(0, 5))
    new_num3 = round(random.uniform(0, 5))
    t = new_num1 % 6
    r = (new_num1 + new_num2 - 1) % 6
    d = (new_num1 + new_num2 + new_num3 - 2) % 6
    g = {1: "大安",2: "流连",3: "速喜",4: "赤口",5: "小吉",0: "空亡"}
    initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
    initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
    initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
    
    with open(g_path, 'w',encoding='utf-8') as f:
        f.write(initial_text1)

    vc5 = v5 % 2
    vc6 = v6 % 2

    match vc5:
        case 1:
            match vc6:
                case 0:
                    print("三宫定义，并计算吉值")
                case 1:
                    print("三宫定义，不计算吉值")
            pass
        case 0:
            match vc6:
                case 0:
                    print("非三宫定义，并计算吉值")
                case 1:
                    print("非三宫定义，不计算吉值")
    return initial_text1