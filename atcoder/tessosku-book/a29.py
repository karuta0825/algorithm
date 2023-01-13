a, b = map(int, input().split())

divisor = 10 ** 9 + 7

# a = a % divisor

# print((a ** b) % divisor)


# 17 // 2
# 8 // 2
# 4 // 2
# 2 // 2
# どうやって30をもとめるのか？
# 2, 4, 8, 16, 32
#

def modpow(a, b, mod):
    if (b == 0):
        return 1 % mod

    if (b % 2 == 0):
        return modpow(a * a % mod, b // 2, mod)

    if (b % 2 == 1):
        return modpow(a, b - 1, mod) * a % mod

print(modpow(a, b , divisor))
