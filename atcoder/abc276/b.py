N, M = map(int, input().split())
ds = [list(map(int, input().split())) for _ in range(M)]

obj = {}
for i in range(N):
    obj[i + 1] = []

for [s, g] in ds:
    obj[s].append(g)
    obj[g].append(s)


for k in obj:

    cnt = len(obj[k])

    if (cnt == 0):
        print(cnt)
    else:
        sortary = sorted(obj[k])
        print(*[cnt, *sortary])
