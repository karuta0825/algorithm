import sys
sys.setrecursionlimit(10**9)

N = int(input())

def f(x):
    return x ** 3 + x


def bb(l, r):

    if r - l <= 0.001:
        return r

    m = (l + r) / 2

    if f(m) < N:
        return bb(m,r)
    else:
        return bb(l,m)


print(bb(0, 10 ** 10))
