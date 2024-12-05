import os

from function.JsonFile import File
from function.variables.ProjectDictionaryVariables import XLR_DATA,XLR_DATA_WU_XING,XLR_DATA_WU_XING_JI_LU

p_ = os.path.dirname(__file__)
PATH = os.path.abspath(os.path.join(p_, '..', '..'))
DATA_FILE_PATH = os.path.join(PATH, "data")
ICON_FILE_PATH = os.path.join(PATH, "icon")
os.makedirs(DATA_FILE_PATH, exist_ok=True)
A_PATH = os.path.join(DATA_FILE_PATH, "a")
B_PATH = os.path.join(DATA_FILE_PATH, "b")
C_PATH = os.path.join(DATA_FILE_PATH, "c")
D_PATH = os.path.join(DATA_FILE_PATH, "d")
E_PATH = os.path.join(DATA_FILE_PATH, "e")
F_PATH = os.path.join(DATA_FILE_PATH, "f")
G_PATH = os.path.join(DATA_FILE_PATH, "g")
H_PATH = os.path.join(DATA_FILE_PATH, "h")
I_PATH = os.path.join(DATA_FILE_PATH, "i")
J_PATH = os.path.join(DATA_FILE_PATH, "j")
K_PATH = os.path.join(DATA_FILE_PATH, "k")
N_PATH = os.path.join(DATA_FILE_PATH, "n")
O_PATH = os.path.join(DATA_FILE_PATH, "o")
P_PATH = os.path.join(DATA_FILE_PATH, "p")
Q_PATH = os.path.join(DATA_FILE_PATH, "q")
R_PATH = os.path.join(DATA_FILE_PATH, "r")
S_PATH = os.path.join(DATA_FILE_PATH, "s")
T_PATH = os.path.join(DATA_FILE_PATH, "t")
U_PATH = os.path.join(DATA_FILE_PATH, "u")
V_PATH = os.path.join(DATA_FILE_PATH, "v")
W_PATH = os.path.join(DATA_FILE_PATH, "w")
X_PATH = os.path.join(DATA_FILE_PATH, "x")
Y_PATH = os.path.join(DATA_FILE_PATH, "y")
Z_PATH = os.path.join(DATA_FILE_PATH, "z")
AA_PATH = os.path.join(DATA_FILE_PATH, "aa")
AB_PATH = os.path.join(DATA_FILE_PATH, "ab")

W_ROOT2_C_VAR_2_PATH = os.path.join(DATA_FILE_PATH, "w_root2_c_var_2_path")
ICON_PATH = os.path.join(ICON_FILE_PATH, "main_icon.ico")

XLR_DATA_PATH = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_data.json")
XLR_DATA_WU_XING_PATH = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_wu_xing_data.json")
XLR_DATA_WU_XING_JI_LU_PATH = os.path.join(DATA_FILE_PATH, "xiao_liu_ren_wu_xing_ji_lu_data.json")

XLR_JSON = File.dict_load(XLR_DATA_PATH, XLR_DATA)
XLR_WU_XING_JSON = File.dict_load(XLR_DATA_WU_XING_PATH, XLR_DATA_WU_XING)
XLR_WU_XING_JI_LU_JSON = File.dict_load(XLR_DATA_WU_XING_JI_LU_PATH , XLR_DATA_WU_XING_JI_LU)

TEXT_TEMP_PATH = os.path.join(DATA_FILE_PATH, "text-temp")

RECONSTRUCTIONS_PAGE = os.path.join(DATA_FILE_PATH, "reconstructions_page")
os.makedirs(RECONSTRUCTIONS_PAGE, exist_ok=True)
RECONSTRUCTIONS = os.path.join(RECONSTRUCTIONS_PAGE, 'reconstructions')
os.makedirs(RECONSTRUCTIONS, exist_ok=True)

RECONSTRUCTIONS_LIST_PATH = os.path.join(RECONSTRUCTIONS, 'reconstructions_list')
os.makedirs(RECONSTRUCTIONS_LIST_PATH, exist_ok=True)
RECONSTRUCTIONS_LIST = os.path.join(RECONSTRUCTIONS_LIST_PATH, 'reconstructions_list.json')
