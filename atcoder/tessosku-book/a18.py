N, S = map(int, input().split())
A = list(map(int, input().split()))
SA = sorted(A, reverse=True)

dp = [[False] * (S+1) for _ in range(N+1)]


dp[0][0] = True

# dp[i][j]
# i番目をつかって、総数jを作ることができるかどうか

# i-1が登場するので1からスタートする
for i in range(1,N+1):
    val = A[i-1]

    for j in range(S+1):
        if (j - val >= 0):
            dp[i][j] = (dp[i-1][j] or
                        dp[i-1][j - val])
        else:
            dp[i][j] = dp[i-1][j]


if (dp[N][S]):
    print("Yes")
else:
    print("No")
