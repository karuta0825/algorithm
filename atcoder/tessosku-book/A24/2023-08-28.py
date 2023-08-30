from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

INF = 10 ** 8
L = [INF] * N
dp = [0] * N


for i in range(N):

    pos = bisect_left(L, A[i])

    L[pos] = A[i]

    dp[i] = pos + 1

print(max(dp))
