def gcd(a, b):
    if b < a:
        a, b = b, a

    if a == 0:
        return b

    c = b % a
    return gcd(c, a)


gcd(33, 88)
