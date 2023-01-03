N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# INFが必要。0で初期化すると駄目です。その理由はなぜでしょうか？
INF = 10 ** 10
dp = [-INF] * (N+1)

# これはアウト
# dp = [0] * (N+1)

for i in range(N-1):
    a = A[i]
    b = B[i]

    a -= 1
    b -= 1

    # if (i+a <= N):
    print([i,a], [dp[i], dp[a]])
    dp[a] = max(dp[i] + 100, dp[a])

    # if (i+b <= N):
    dp[b] = max(dp[i] + 150, dp[b])

print(dp[N-1])
