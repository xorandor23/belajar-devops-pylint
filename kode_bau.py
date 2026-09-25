x = 10


def bad_function_name(var_a, var_b, var_c, var_d, var_e, var_f):
    global x
    var_l = 1
    var_o = 0

    # Menggunakan 'and', 'not', dan 'is None' sesuai standar PEP 8
    if var_a and not var_b and var_c is None:
        try:
            print(var_a + var_b)
            res = var_e[0] + var_f + var_l + var_o
            return res
        except (TypeError, IndexError) as err:
            # Menentukan jenis error secara spesifik
            print(f"Error terdeteksi: {err}")
            return None
    else:
        return None


bad_function_name(True, False, None, 1, [2], 3)
