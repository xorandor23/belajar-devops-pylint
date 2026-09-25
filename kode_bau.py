def bad_function(var_A, var_B, var_C, var_E, var_F, var_G): 
    var_l = 1
    var_o = 0
    if var_A is True and var_B is False and var_C is None:
        try:
            print(var_A + var_B)
            res = var_E + var_F[0] + var_l + var_o
        except:
            pass
    else:
        return None

bad_function(True, False, None, 1, [2], 3)