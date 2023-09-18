D, N = map(int, input().split())

LRHs = [list(map(int, input().split())) for _ in range(N)]

INF = 24
ans = [INF] * D

for lrh in LRHs:

    L, R, H = lrh

    for i in range(L, R+1):
        ans[i-1] = min(ans[i-1], H)

print(sum(ans))
