N = int(input())
A = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]
dp[N-1] = A

for i in range(N-1, -1, -1):
    for j in range(i):
        if i % 2 == 1:
            dp[i-1][j] = max(dp[i][j], dp[i][j+1])
        else:
            dp[i-1][j] = min(dp[i][j], dp[i][j+1])

print(dp[0][0])

