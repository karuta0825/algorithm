N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    # そう二重配列になる。
    for j in range(S+1):
        dp[i][j] = dp[i-1][j]

        if j-A[i-1] >= 0:
            dp[i][j] = dp[i][j] or dp[i-1][j-A[i-1]]

if dp[N][S]:
    print("Yes")
else:
    print("No")

