N, X = map(int, input().split())

ary = []
for _ in range(N):
    A, B = map(int, input().split())
    ary = [*ary, *[A]* B]


A = sorted(ary, reverse=True)

S = len(A)
dp = [[False] * (X+1) for _ in range(S+1)]

dp[0][0] = True

for i in range(1,S+1):
    val = A[i-1]

    for j in range(X+1):
        if (j - val >= 0):
            dp[i][j] = (dp[i-1][j] or
                        dp[i-1][j - val])
        else:
            dp[i][j] = dp[i-1][j]


if (dp[S][X]):
    print("Yes")
else:
    print("No")
