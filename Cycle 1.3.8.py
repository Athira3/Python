def char_mix(a, b):
    a1 = b[:1] + a[1:]
    b1 = a[:1] + b[1:]
    return a1 + " " + b1


print(char_mix('abcd', 'ABCD'))