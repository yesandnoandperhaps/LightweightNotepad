from LightweightNotepad.function.ProjectFunctions import t_load
from LightweightNotepad.function.ProjectPathVariables import C_PATH, H_PATH, I_PATH, J_PATH, \
    K_PATH, N_PATH, Z_PATH, AA_PATH, AB_PATH, E_PATH, D_PATH, F_PATH


v = int(t_load(C_PATH) or 0)
v2 = int(t_load(D_PATH) or 1)
v3 = int(t_load(E_PATH) or 0)
v4 = int(t_load(F_PATH) or 0)
num_wv1 = int(t_load(N_PATH) or 0)
var_num_w_4_3 = int(t_load(Z_PATH) or 1)
var2_num_w_4_3 = int(t_load(AA_PATH) or 0)
var3_num_w_4_3 = int(t_load(AB_PATH) or 0)
size__ = (t_load(H_PATH) or "70MB")
divide_up = (t_load(I_PATH) or "等于大文件定义")
# noinspection SpellCheckingInspection
onandoff = (t_load(J_PATH) or "开启")
circular = (t_load(K_PATH) or "30MB")

t_size = 0
t_divide_up = 0
circular_num = 31457280
size_map = {
    "70MB": 73400320,
    "50MB": 52428800,
    "128MB": 134217728,
    "256MB": 268435456,
    "512MB": 536870912
}
divide_map = {
    "5MB": 5242880,
    "10MB": 10485760,
    "15MB": 15728640,
    "30MB": 31457280,
    "等于大文件定义": None
}

if size__ in size_map:
    t_size = size_map[size__]
    if divide_up == "等于大文件定义":
        t_divide_up = t_size
    else:
        t_divide_up = divide_map.get(divide_up, 31457280)
circular_map = {
    "5MB": 5242880,
    "10MB": 10485760,
    "30MB": 31457280,
    "50MB": 52428800,
    "70MB": 73400320,
    "128MB": 134217728,
    "256MB": 268435456,
    "512MB": 536870912
}
circular_num = circular_map.get(circular, 31457280)