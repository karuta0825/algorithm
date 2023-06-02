N = int(input())
A = list(map(int, input().split()))

candidates = []

def f(d):

    if d == 0:
        return -1

    if A[d-1] > A[d]:
        candidates.append(d-1)
        return d-1+1

    # これでいけたな！うれしいぞ
    while len(candidates):
        c = candidates.pop()
        if A[c] > A[d]:
            candidates.append(c)
            return c+1

    return -1

g = []
for d in range(N):
    v = f(d)
    g.append(v)

print(*g)
