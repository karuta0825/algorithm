N, M = list(map(int, input().split()))

ary = [i for i in range(1, M +1)]

r = []
for i in range(1 << M):
    s = format(i, 'b').zfill(M)

    a = []
    for idx, c in enumerate(s):
        if (c == '1'):
            a.append(ary[idx])

    if (len(a) == N):
        r.append(a)

for i in sorted(r):
    print(" ".join(map(str, i)))
