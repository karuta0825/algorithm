N = int(input())

LRs = [list(map(int, input().split())) for _ in range(N)]

lrs = sorted(LRs, key=lambda x: x[1])

cnt = 1
cL,cR  = lrs[0]

for m in lrs[1:]:

    l, r = m
    if cR <= l:
        cnt += 1
        cL, cR = l, r

print(cnt)
