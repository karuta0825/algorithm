N, M = map(int, input().split())

A = []

for i in range(M):

    a = list(map(int, input().split()))
    A.append(a)


INF = 10 ** 8
dp = [[INF] * (1 << N) for _ in range(M+1)]

dp[0][0] = 0

def toten(ary):
    ans = 0
    n = len(ary)
    for i in range(n):
        ans += (2 ** i) * ary[n-1-i]

    return ans

def trans(num, ary):

    c = toten(ary)

    ans = bin(num | c)

    return int(ans, 0)

for i in range(1, M+1):
    for j in range(1 << N):

        X = trans(j, A[i-1])
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][X] = min(dp[i][X], dp[i-1][j] + 1)

if dp[M][-1] == INF:
    print(-1)
else:
    print(dp[M][-1])
