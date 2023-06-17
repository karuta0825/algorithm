N = int(input())
A = list(map(int, input().split()))

d = {}
ans = {}
for i in range(1, N+1):
    d[i] = []
    ans[i] = 0

for i, v in enumerate(A):
    d[v].append(i)

    if len(d[v]) == 2:
        ans[v] = i


print(*list(map(lambda x: x[0], sorted(ans.items(), key=lambda x: x[1]))))
