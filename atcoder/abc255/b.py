import math
n, k = map(int, input().split())
Ls = list(map(int, input().split()))
Ps = [list(map(int, input().split())) for _ in range(n)]

MIN = 10000000000000000000000000000000000000

def kyori(p1, p2):
    return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

mlist = []
for i in range(len(Ps)):
    if (i+1 in Ls):
        continue

    p = Ps[i]
    m = MIN
    for l in Ls:
        tmp = kyori(Ps[l-1], p)
        if (tmp < m):
            m = tmp

    mlist.append(m)

print(math.sqrt(max(mlist)))
