from collections import Counter
N = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)

    return a

def searchFactor(n):
    ans = 1
    for i in Counter(prime_factorize(n)).values():
        ans *= i + 1
    return ans

ans = 0

for i in range(1, (N // 2) + 1):

    AB = i
    CD = N - i

    ab = searchFactor(AB)

    if (AB == CD):
        ans += ab * ab
    else:
        cd = searchFactor(CD)
        ans += (ab * cd) * 2

print(ans)
