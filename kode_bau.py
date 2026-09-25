def bad_function(a, b, c, d, e, f): 
    l = 1
    o = 0
    if a is True and b is False and c is None:
        try:
            print(a + b)
            res = d + e[0]
        except:
            pass
    else:
        return None

bad_function(True, False, None, 1, [2], 3)