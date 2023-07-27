import sys
sys.setrecursionlimit(10**9)

N, X = map(int, input().split())
A = list(map(int, input().split()))

def bis(s, g):

    if g - s == 1:
        return g

    m = (s + g) // 2

    if X <= A[m]:
        return bis(s, m)
    else:
        return bis(m, g)


print(bis(0, len(A)) + 1)
