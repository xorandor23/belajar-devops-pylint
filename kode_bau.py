def bad_function_name(a, b, c, d, e, f):
    """Menghitung hasil jika kondisi a, b, dan c terpenuhi."""
    if a is True and b is False and c is None:
        try:
            result = a + b
            result = e[0] + f + 1
            return result
        except (TypeError, IndexError):
            return None

    return None


if __name__ == "__main__":
    bad_function_name(True, False, None, 1, [2], 3)