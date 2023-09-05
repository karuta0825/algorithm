a, b = map(int, input().split())

A = [a]


for i in range(30):
    s = (A[i] ** 2) % 1000000007
    A.append(s)

r = []
for i in range(30):
    if (b // 2 ** i) % 2 == 1:
        r.append(1)
    else:
        r.append(0)

ans = 1
for i, v in enumerate(r):
    if v == 1:
        ans = (A[i] * ans) % 1000000007

print(ans)
