"""Module untuk mendemonstrasikan fungsi matematika sederhana yang bersih."""


def calculate_sum_from_list(var_a, var_b, var_c, var_e, var_f):
    """Memvalidasi input dan menjumlahkan data dari list.

    Returns:
        int: Hasil penjumlahan jika valid, atau None jika terjadi error.
    """
    offset_one = 1
    offset_zero = 0

    if var_a and not var_b and var_c is None:
        try:
            print(var_a + var_b)
            res = var_e[0] + var_f + offset_one + offset_zero
            return res
        except (TypeError, IndexError) as err:
            print(f"Error terdeteksi: {err}")
            return None

    # Menghapus 'else:' karena tidak lagi diperlukan setelah 'return' di atas
    return None


# Menjalankan fungsi dengan nama yang sudah diperbaiki
calculate_sum_from_list(True, False, None, [2], 3)
