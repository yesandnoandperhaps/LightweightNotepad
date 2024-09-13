import decimal
import math
import random

from function.ProjectVariables import l_path, m_path, q_path, u_path, v_path

"l->m->q"
def load(path):
    try:
        with open(path, 'r',encoding='utf-8') as f:
                return f.read()
    except FileNotFoundError:
        pass
def load_decimal():
    try:
        with open(q_path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass
def combobox_load(path):
    try:
        with open(path, 'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        pass

v5 = int(load(l_path) or 0)
v6 = int(load(m_path) or 0)

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

class Num:
    def __init__(self,t=0,r=0,d=0):
        self.t = t
        self.r = r
        self.d = d
    
    def D(self):
        d_num1 = round(random.uniform(0, 3), 2)
        d_num2 = round(random.uniform(0, 3-d_num1), 2)
        d_num3 = round(3-d_num1-d_num2, 2)
        return d_num1, d_num2, d_num3
    
    def L(self):
        l_num1 = round(random.uniform(0, -1), 2)
        l_num2 = round(random.uniform(0, -1-l_num1), 2)
        l_num3 = round(-1-l_num1-l_num2, 2)
        return l_num1, l_num2, l_num3
    
    def S(self):
        s_num1 = round(random.uniform(0, 2), 2)
        s_num2 = round(random.uniform(0, 2-s_num1), 2)
        s_num3 = round(2-s_num1-s_num2, 2)
        return s_num1, s_num2, s_num3
    
    def C(self):
        c_num1 = round(random.uniform(0, -2), 2)
        c_num2 = round(random.uniform(0, -2-c_num1), 2)
        c_num3 = round(-2-c_num1-c_num2, 2)
        return c_num1, c_num2, c_num3
    
    def X(self):
        x_num1 = round(random.uniform(0, 1), 2)
        x_num2 = round(random.uniform(0, 1-x_num1), 2)
        x_num3 = round(1-x_num1-x_num2, 2)
        return x_num1, x_num2, x_num3
    
    def K(self):
        c_num1 = round(random.uniform(0, -3), 2)
        c_num2 = round(random.uniform(0, -3-c_num1), 2)
        c_num3 = round(-3-c_num1-c_num2, 2)
        return c_num1, c_num2, c_num3

    def judgment_f(self):
        t_r_d_list = [self.t, self.r, self.d]
        sorted_trd_list = sorted(t_r_d_list)
        listj = [0,1,2,3,4,5]

        def compare_list():

            if len(list(set(sorted_trd_list).intersection(set(listj)))) == 3:

                counter = 0

                for _ in sorted_trd_list:
                    if counter == 0:
                        match _:
                            case 1:
                                pax,pay,paz = self.D()
                            case 2:
                                pax,pay,paz = self.L()
                            case 3:
                                pax,pay,paz = self.S()
                            case 4:
                                pax,pay,paz = self.C()
                            case 5:
                                pax,pay,paz = self.X()
                            case 0:
                                pax,pay,paz = self.K()
                        counter = counter + 1
                    elif counter == 1:
                        match _:
                            case 1:
                                pbx,pby,pbz = self.D()
                            case 2:
                                pbx,pby,pbz = self.L()
                            case 3:
                                pbx,pby,pbz = self.S()
                            case 4:
                                pbx,pby,pbz = self.C()
                            case 5:
                                pbx,pby,pbz = self.X()
                            case 0:
                                pbx,pby,pbz = self.K()
                        counter = counter + 1
                    elif counter == 2:
                        match _:
                            case 1:
                                pcx,pcy,pcz = self.D()
                            case 2:
                                pcx,pcy,pcz = self.L()
                            case 3:
                                pcx,pcy,pcz = self.S()
                            case 4:
                                pcx,pcy,pcz = self.C()
                            case 5:
                                pcx,pcy,pcz = self.X()
                            case 0:
                                pcx,pcy,pcz = self.K()
                        counter = counter + 1
                    else:
                        break
        
            elif len(list(set(sorted_trd_list).intersection(set(listj)))) == 2:

                h = list(set(sorted_trd_list).intersection(set(listj)))

                c = sorted_trd_list.count(h[0])

                def h0():
                    match h[0]:
                        case 1:
                            pcx,pcy,pcz = self.D()
                        case 2:
                            pcx,pcy,pcz = self.L()
                        case 3:
                            pcx,pcy,pcz = self.S()
                        case 4:
                            pcx,pcy,pcz = self.C()
                        case 5:
                            pcx,pcy,pcz = self.X()
                        case 0:
                            pcx,pcy,pcz = self.K()
                    return pcx,pcy,pcz
            
                def h1():
                    match h[0]:
                        case 1:
                            pbx,pby,pbz = self.D()
                            pcx,pcy,pcz = self.D()
                        case 2:
                            pbx,pby,pbz = self.L()
                            pcx,pcy,pcz = self.L()
                        case 3:
                            pbx,pby,pbz = self.S()
                            pcx,pcy,pcz = self.S()
                        case 4:
                            pbx,pby,pbz = self.C()
                            pcx,pcy,pcz = self.C()
                        case 5:
                            pbx,pby,pbz = self.X()
                            pcx,pcy,pcz = self.X()
                        case 0:
                            pbx,pby,pbz = self.K()
                            pcx,pcy,pcz = self.K()
                    return pbx,pby,pbz,pcx,pcy,pcz
            
                def c_():
                    match c:
                        case 1:
                            #h[1]-2
                            match h[1]:
                                case 1:
                                    pax,pay,paz = self.D()
                                    pbx,pby,pbz = self.D()
                                    pcx,pcy,pcz = h0()
                                case 2:
                                    pax,pay,paz = self.L()
                                    pbx,pby,pbz = self.L()
                                    pcx,pcy,pcz = h0()
                                case 3:
                                    pax,pay,paz = self.S()
                                    pbx,pby,pbz = self.S()
                                    pcx,pcy,pcz = h0()
                                case 4:
                                    pax,pay,paz = self.C()
                                    pbx,pby,pbz = self.C()
                                    pcx,pcy,pcz = h0()
                                case 5:
                                    pax,pay,paz = self.X()
                                    pbx,pby,pbz = self.X()
                                    pcx,pcy,pcz = h0()
                                case 0:
                                    pax,pay,paz = self.K()
                                    pbx,pby,pbz = self.K()
                                    pcx,pcy,pcz = h0()
                        case 2:
                            #h[0]-1
                            match h[0]:
                                case 1:
                                    pax,pay,paz = self.D()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 2:
                                    pax,pay,paz = self.L()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 3:
                                    pax,pay,paz = self.S()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 4:
                                    pax,pay,paz = self.C()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 5:
                                    pax,pay,paz = self.X()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 0:
                                    pax,pay,paz = self.K()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                
                    return pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz
            
                pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = c_()

            else:
                match self.t:
                    case 1:
                        pax,pay,paz = self.D()
                        pbx,pby,pbz = self.D()
                        pcx,pcy,pcz = self.D()
                    case 2:
                        pax,pay,paz = self.L()
                        pbx,pby,pbz = self.L()
                        pcx,pcy,pcz = self.L()
                    case 3:
                        pax,pay,paz = self.S()
                        pbx,pby,pbz = self.S()
                        pcx,pcy,pcz = self.S()
                    case 4:
                        pax,pay,paz = self.C()
                        pbx,pby,pbz = self.C()
                        pcx,pcy,pcz = self.C()
                    case 5:
                        pax,pay,paz = self.X()
                        pbx,pby,pbz = self.X()
                        pcx,pcy,pcz = self.X()
                    case 0:
                        pax,pay,paz = self.K()
                        pbx,pby,pbz = self.K()
                        pcx,pcy,pcz = self.K()
            
            return pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz
        
        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = compare_list()

        t = T(pax=pax,pay=pay,paz=paz,pbx=pbx,pby=pby,pbz=pbz,pcx=pcx,pcy=pcy,pcz=pcz)
        
        return t.incentre()

class ReturnNum:
    def __init__(self,t=0,r=0,d=0):
        self.t = t
        self.r = r
        self.d = d
    
    def D(self):
        d_num1 = round(random.uniform(0, 3), 2)
        d_num2 = round(random.uniform(0, 3-d_num1), 2)
        d_num3 = round(3-d_num1-d_num2, 2)
        return d_num1, d_num2, d_num3
    
    def L(self):
        l_num1 = round(random.uniform(0, -1), 2)
        l_num2 = round(random.uniform(0, -1-l_num1), 2)
        l_num3 = round(-1-l_num1-l_num2, 2)
        return l_num1, l_num2, l_num3
    
    def S(self):
        s_num1 = round(random.uniform(0, 2), 2)
        s_num2 = round(random.uniform(0, 2-s_num1), 2)
        s_num3 = round(2-s_num1-s_num2, 2)
        return s_num1, s_num2, s_num3
    
    def C(self):
        c_num1 = round(random.uniform(0, -2), 2)
        c_num2 = round(random.uniform(0, -2-c_num1), 2)
        c_num3 = round(-2-c_num1-c_num2, 2)
        return c_num1, c_num2, c_num3
    
    def X(self):
        x_num1 = round(random.uniform(0, 1), 2)
        x_num2 = round(random.uniform(0, 1-x_num1), 2)
        x_num3 = round(1-x_num1-x_num2, 2)
        return x_num1, x_num2, x_num3
    
    def K(self):
        c_num1 = round(random.uniform(0, -3), 2)
        c_num2 = round(random.uniform(0, -3-c_num1), 2)
        c_num3 = round(-3-c_num1-c_num2, 2)
        return c_num1, c_num2, c_num3

    def judgment_f(self):
        t_r_d_list = [self.t, self.r, self.d]
        sorted_trd_list = sorted(t_r_d_list)
        listj = [0,1,2,3,4,5]

        def compare_list():

            if len(list(set(sorted_trd_list).intersection(set(listj)))) == 3:

                counter = 0

                for _ in sorted_trd_list:
                    if counter == 0:
                        match _:
                            case 1:
                                pax,pay,paz = self.D()
                            case 2:
                                pax,pay,paz = self.L()
                            case 3:
                                pax,pay,paz = self.S()
                            case 4:
                                pax,pay,paz = self.C()
                            case 5:
                                pax,pay,paz = self.X()
                            case 0:
                                pax,pay,paz = self.K()
                        counter = counter + 1
                    elif counter == 1:
                        match _:
                            case 1:
                                pbx,pby,pbz = self.D()
                            case 2:
                                pbx,pby,pbz = self.L()
                            case 3:
                                pbx,pby,pbz = self.S()
                            case 4:
                                pbx,pby,pbz = self.C()
                            case 5:
                                pbx,pby,pbz = self.X()
                            case 0:
                                pbx,pby,pbz = self.K()
                        counter = counter + 1
                    elif counter == 2:
                        match _:
                            case 1:
                                pcx,pcy,pcz = self.D()
                            case 2:
                                pcx,pcy,pcz = self.L()
                            case 3:
                                pcx,pcy,pcz = self.S()
                            case 4:
                                pcx,pcy,pcz = self.C()
                            case 5:
                                pcx,pcy,pcz = self.X()
                            case 0:
                                pcx,pcy,pcz = self.K()
                        counter = counter + 1
                    else:
                        break
        
            elif len(list(set(sorted_trd_list).intersection(set(listj)))) == 2:

                h = list(set(sorted_trd_list).intersection(set(listj)))

                c = sorted_trd_list.count(h[0])

                def h0():
                    match h[0]:
                        case 1:
                            pcx,pcy,pcz = self.D()
                        case 2:
                            pcx,pcy,pcz = self.L()
                        case 3:
                            pcx,pcy,pcz = self.S()
                        case 4:
                            pcx,pcy,pcz = self.C()
                        case 5:
                            pcx,pcy,pcz = self.X()
                        case 0:
                            pcx,pcy,pcz = self.K()
                    return pcx,pcy,pcz
            
                def h1():
                    match h[0]:
                        case 1:
                            pbx,pby,pbz = self.D()
                            pcx,pcy,pcz = self.D()
                        case 2:
                            pbx,pby,pbz = self.L()
                            pcx,pcy,pcz = self.L()
                        case 3:
                            pbx,pby,pbz = self.S()
                            pcx,pcy,pcz = self.S()
                        case 4:
                            pbx,pby,pbz = self.C()
                            pcx,pcy,pcz = self.C()
                        case 5:
                            pbx,pby,pbz = self.X()
                            pcx,pcy,pcz = self.X()
                        case 0:
                            pbx,pby,pbz = self.K()
                            pcx,pcy,pcz = self.K()
                    return pbx,pby,pbz,pcx,pcy,pcz
            
                def c_():
                    match c:
                        case 1:
                            #h[1]-2
                            match h[1]:
                                case 1:
                                    pax,pay,paz = self.D()
                                    pbx,pby,pbz = self.D()
                                    pcx,pcy,pcz = h0()
                                case 2:
                                    pax,pay,paz = self.L()
                                    pbx,pby,pbz = self.L()
                                    pcx,pcy,pcz = h0()
                                case 3:
                                    pax,pay,paz = self.S()
                                    pbx,pby,pbz = self.S()
                                    pcx,pcy,pcz = h0()
                                case 4:
                                    pax,pay,paz = self.C()
                                    pbx,pby,pbz = self.C()
                                    pcx,pcy,pcz = h0()
                                case 5:
                                    pax,pay,paz = self.X()
                                    pbx,pby,pbz = self.X()
                                    pcx,pcy,pcz = h0()
                                case 0:
                                    pax,pay,paz = self.K()
                                    pbx,pby,pbz = self.K()
                                    pcx,pcy,pcz = h0()
                        case 2:
                            #h[0]-1
                            match h[0]:
                                case 1:
                                    pax,pay,paz = self.D()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 2:
                                    pax,pay,paz = self.L()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 3:
                                    pax,pay,paz = self.S()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 4:
                                    pax,pay,paz = self.C()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 5:
                                    pax,pay,paz = self.X()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                case 0:
                                    pax,pay,paz = self.K()
                                    pbx,pby,pbz,pcx,pcy,pcz = h1()
                                
                    return pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz
            
                pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = c_()

            else:
                match self.t:
                    case 1:
                        pax,pay,paz = self.D()
                        pbx,pby,pbz = self.D()
                        pcx,pcy,pcz = self.D()
                    case 2:
                        pax,pay,paz = self.L()
                        pbx,pby,pbz = self.L()
                        pcx,pcy,pcz = self.L()
                    case 3:
                        pax,pay,paz = self.S()
                        pbx,pby,pbz = self.S()
                        pcx,pcy,pcz = self.S()
                    case 4:
                        pax,pay,paz = self.C()
                        pbx,pby,pbz = self.C()
                        pcx,pcy,pcz = self.C()
                    case 5:
                        pax,pay,paz = self.X()
                        pbx,pby,pbz = self.X()
                        pcx,pcy,pcz = self.X()
                    case 0:
                        pax,pay,paz = self.K()
                        pbx,pby,pbz = self.K()
                        pcx,pcy,pcz = self.K()
            
            return pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz
        
        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = compare_list()

        t = T(pax=pax,pay=pay,paz=paz,pbx=pbx,pby=pby,pbz=pbz,pcx=pcx,pcy=pcy,pcz=pcz)
        
        return t.incentre(),pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz            

def numqgua():
    new_num1 = round(random.uniform(0, 5))
    new_num2 = round(random.uniform(0, 5))
    new_num3 = round(random.uniform(0, 5))
    t = new_num1 % 6
    r = (new_num1 + new_num2 - 1) % 6
    d = (new_num1 + new_num2 + new_num3 - 2) % 6
    return t,r,d

'''
def numqgua_2():
    new_num1 = round(random.uniform(0, 5))
    new_num2 = round(random.uniform(0, 5))
    new_num3 = round(random.uniform(0, 5))
    t = new_num1 % 6
    r = (new_num1 + new_num2) % 6
    d = (new_num1 + new_num2 + new_num3) % 6
    return t, r, d
'''

def numgua2_2():
    t,r,d = numqgua()
    num_t = Num(t=t, r=r, d=d)
    a = str(num_t.judgment_f())
    a_ = decimal.Decimal(a)
    num_t_text = "{}\n".format(a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN))
    if num_t_text == str(-0):
        num_t_text = 0
        return num_t_text
    return num_t_text

def numgua2_1():
    t,r,d = numqgua()
    num_t = Num(t=t, r=r, d=d)
    a = num_t.judgment_f()
    num_t_text = "{}\n".format(a)
    if num_t_text == str(-0):
        num_t_text = 0
        return num_t_text
    return num_t_text

def numgua2_0():
    t,r,d = numqgua()
    num_t = Num(t=t, r=r, d=d)
    a = str(num_t.judgment_f())
    a_ = decimal.Decimal(a)
    num_t_text = "{}\n".format(a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN))
    if num_t_text == str(-0):
        num_t_text = 0
        return num_t_text
    return num_t_text

def numgua():
    t,r,d = numqgua()
    g = {1: "大安",2: "流连",3: "速喜",4: "赤口",5: "小吉",0: "空亡"}
    num_t = Num(t=t, r=r, d=d)

    vc5 = v5 % 2
    vc6 = v6 % 2

    match vc5:
        case 1:
            match vc6:
                case 0:
                    initial_text1 = "未完成\n"
                    #三宫定义，并计算吉值
                case 1:
                    #三宫定义，不计算吉值
                    pass
            pass
        case 0:
            match vc6:
                case 0:
                    t_rule_num2 = int(load_decimal() or 2)
                    match t_rule_num2:
                        case 1:
                            yes = num_t.judgment_f()
                            if str(yes) == str(-0):
                                yes = 0
                                return yes
                            initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                            initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                            initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                            initial_text1 += "吉值：{}\n".format(yes)
                        case 0:
                            a = str(num_t.judgment_f())
                            a_ = decimal.Decimal(a)
                            a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                            if a__ == str(-0):
                                a__ = 0
                                return a__
                            initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                            initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                            initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                            initial_text1 += "吉值：{}\n".format(a__)
                        case 2:
                            a = str(num_t.judgment_f())
                            a_ = decimal.Decimal(a)
                            a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                            if a__ == str(-0):
                                a__ = 0
                                return a__
                            initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                            initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                            initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                            initial_text1 += "吉值：{}\n".format(a__)
                    #非三宫定义，并计算吉值
                case 1:
                    #非三宫定义，不计算吉值
                    pass
    return initial_text1

def numgua2_3():
    t,r,d = numqgua()
    print(t)
    g = {1: "大安",2: "流连",3: "速喜",4: "赤口",5: "小吉",0: "空亡"}
    num_t = Num(t=t, r=r, d=d)
    vc5 = v5 % 2
    vc6 = v6 % 2

    match vc5:
        case 1:
            match vc6:
                case 0:
                    initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                    initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                    initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                    initial_text1 += "未完成\n"
                    #三宫定义，并计算吉值
                case 1:
                    #三宫定义，不计算吉值
                    pass
            pass
        case 0:
            match vc6:
                case 0:
                    t_rule_num2 = int(load_decimal() or 2)
                    match t_rule_num2:
                        case 1:
                            yes = num_t.judgment_f()
                            if str(yes) == str(-0):
                                yes = 0
                                return yes
                            initial_text1 = "{},{},{},{}\n".format(g.get(t, "空亡"),g.get(r, "空亡"),g.get(d, "空亡"),yes)
                        case 0:
                            a = str(num_t.judgment_f())
                            a_ = decimal.Decimal(a)
                            a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                            if a__ == str(-0):
                                a__ = 0
                                return a__
                            initial_text1 = "{},{},{},{}\n".format(g.get(t, "空亡"),g.get(r, "空亡"),g.get(d, "空亡"),a__)
                        case 2:
                            a = str(num_t.judgment_f())
                            a_ = decimal.Decimal(a)
                            a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                            if a__ == str(-0):
                                a__ = 0
                                return a__
                            initial_text1 = "{},{},{},{}\n".format(g.get(t, "空亡"),g.get(r, "空亡"),g.get(d, "空亡"),a__)
                    #非三宫定义，并计算吉值
                case 1:
                    #非三宫定义，不计算吉值
                    pass
    return initial_text1

def numgua2_4():
    t,r,d = numqgua()
    g = {1: "大安",2: "流连",3: "速喜",4: "赤口",5: "小吉",0: "空亡"}
    g_ = {1:"1",2:"2",3:"3",4:"4",5:"5",0:"6"}
    g__ = {1:"3",2:"-1",3:"2",4:"-2",5:"1",0:"-3"}
    num_t = Num(t=t, r=r, d=d)
    return_num_t = ReturnNum(t=t, r=r, d=d)
    vc5 = v5 % 2
    vc6 = v6 % 2

    match vc5:
        case 1:
            match vc6:
                case 0:
                    initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                    initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                    initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                    initial_text1 += "未完成\n"
                    #三宫定义，并计算吉值
                case 1:
                    #三宫定义，不计算吉值
                    pass
            pass
        case 0:
            match vc6:
                case 0:
                    t_rule_num2 = int(load_decimal() or 2)
                    t_ = str(combobox_load(u_path) or "顺序数据【空亡定为6】")
                    match t_:
                        case "顺序数据【空亡定为6】":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),a__)
                        case "顺序数据【空亡定为0】":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,a__)
                        case "值数据":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),a__)
                        case "详细值数据【四列式】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,a__)
                        case "详细值数据【十列式】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,a__
                                        )
                        case "全部【空亡定为6】【十六列】":
                             match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                        case "全部【空亡定为6】【四列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                        case "全部【空亡定为0】【十六列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                        case "全部【空亡定为0】【四列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                        case "真全部【十九列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                    #非三宫定义，并计算吉值
                case 1:
                    #非三宫定义，不计算吉值
                    pass
    return initial_text1

def numgua2_5():
    t,r,d = numqgua()
    g = {1: "大安",2: "流连",3: "速喜",4: "赤口",5: "小吉",0: "空亡"}
    g_ = {1:"1",2:"2",3:"3",4:"4",5:"5",0:"6"}
    g__ = {1:"3",2:"-1",3:"2",4:"-2",5:"1",0:"-3"}
    num_t = Num(t=t, r=r, d=d)
    return_num_t = ReturnNum(t=t, r=r, d=d)
    vc5 = v5 % 2
    vc6 = v6 % 2
    match vc5:
        case 1:
            match vc6:
                case 0:
                    initial_text1 = "天宫：{}\n".format(g.get(t, "空亡，"))
                    initial_text1 += "人宫：{}\n".format(g.get(r, "空亡，"))
                    initial_text1 += "地宫：{}\n".format(g.get(d, "空亡，"))
                    initial_text1 += "未完成\n"
                    #三宫定义，并计算吉值
                case 1:
                    #三宫定义，不计算吉值
                    pass
            pass
        case 0:
            match vc6:
                case 0:
                    t_rule_num2 = int(load_decimal() or 2)
                    t_ = str(combobox_load(v_path) or "顺序数据【空亡定为6】")
                    match t_:
                        case "顺序数据【空亡定为6】":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),a__)
                        case "顺序数据【空亡定为0】":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(t,r,d,a__)
                        case "值数据":
                            match t_rule_num2:
                                case 1:
                                    yes = num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),yes)
                                case 0:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),a__)
                                case 2:
                                    a = str(num_t.judgment_f())
                                    a_ = decimal.Decimal(a)
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),a__)
                        case "详细值数据【四列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    pa = str(pax) + "，" + str(pay) + "，" + str(paz)
                                    pb = str(pbx) + "，" + str(pby) + "，" + str(pbz)
                                    pc = str(pcx) + "，" + str(pcy) + "，" + str(pcz)
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{}\n".format(pa,pb,pc,a__)
                        case "详细值数据【十列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{}\n".format(
                                        pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz,a__
                                        )
                        case "全部【空亡定为6】【十六列】":
                             match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                        case "全部【空亡定为6】【四列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = g_.get(t, "6") + "，" + g_.get(r, "6") + "，" + g_.get(d, "6")
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = pax+ "，" +pay+ "，" +paz+ "，" +pbx+ "，" +pby+ "，" +pbz+ "，" +pcx+ "，" +pcy+ "，" +pcz
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                        case "全部【空亡定为0】【十六列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                        case "全部【空亡定为0】【四列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,yes)
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    t_g_ = str(t) + "，" + str(r) + "，" + str(d)
                                    t_g__ = g__.get(t, "-3") + "，" + g__.get(r, "-3") + "，" + g__.get(d, "-3")
                                    pabc = str(pax)+ "，" +str(pay)+ "，" +str(paz)+ "，" +str(pbx)+ "，" +str(pby)+ "，" +str(pbz)+ "，" +str(pcx)+ "，" +str(pcy)+ "，" +str(pcz)
                                    initial_text1 = "{},{},{},{}\n".format(t_g_,t_g__,pabc,a__)
                        case "真全部【十九列】":
                            match t_rule_num2:
                                case 1:
                                    yes,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    if str(yes) == str(-0):
                                        yes = 0
                                        return yes
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        yes
                                        )
                                case 0:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                                case 2:
                                    a,pax,pay,paz,pbx,pby,pbz,pcx,pcy,pcz = return_num_t.judgment_f()
                                    a_ = decimal.Decimal(str(a))
                                    a__ = a_.quantize(decimal.Decimal("0.00"),decimal.ROUND_HALF_EVEN)
                                    if a__ == str(-0):
                                        a__ = 0
                                        return a__
                                    initial_text1 = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(
                                        g_.get(t, "6"),g_.get(r, "6"),g_.get(d, "6"),
                                        t,r,d,
                                        g__.get(t, "-3"),g__.get(r, "-3"),g__.get(d, "-3"),
                                        pax,pay,paz,
                                        pbx,pby,pbz,
                                        pcx,pcy,pcz,
                                        a__
                                        )
                            
                    #非三宫定义，并计算吉值
                case 1:
                    #非三宫定义，不计算吉值
                    pass
    return initial_text1
