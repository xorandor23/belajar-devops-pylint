"""Module untuk mendemonstrasikan fungsi matematika sederhana yang bersih."""


def bad_function_name(var_a, var_b, var_c, var_e, var_f):
    """Memvalidasi input dan menjumlahkan data dari list.

    Returns:
        int: Hasil penjumlahan jika valid, atau None jika terjadi error.
    """
    var_l = 1
    var_o = 0

    if var_a and not var_b and var_c is None:
        try:
            print(var_a + var_b)
            res = var_e[0] + var_f + var_l + var_o
            return res
        except (TypeError, IndexError) as err:
            print(f"Error terdeteksi: {err}")
            return None
    else:
        return None


# Menghapus angka 1 (argumen var_d yang tidak terpakai sebelumnya)
bad_function_name(True, False, None, [2], 3)
