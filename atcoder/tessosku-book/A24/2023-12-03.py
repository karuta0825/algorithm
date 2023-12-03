from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

INF = 10 ** 8
dp = [INF] * (N+1)
ans = [0] * (N)

for i, v in enumerate(A):
    pos = bisect_left(dp, v)
    dp[pos] = v
    ans[i] = pos + 1

print(max(ans))
