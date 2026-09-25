"""Modul untuk melakukan perhitungan berdasarkan kondisi tertentu."""


def bad_function_name(a, b, c, e, f):
    """Menghitung hasil apabila seluruh kondisi terpenuhi."""
    if a is True and b is False and c is None:
        try:
            result = a + b
            result = e[0] + f + 1
            return result
        except (TypeError, IndexError):
            return None

    return None


if __name__ == "__main__":
    bad_function_name(True, False, None, [2], 3)