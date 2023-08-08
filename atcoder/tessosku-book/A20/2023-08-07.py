S = input()
T = input()

s, t = len(S), len(T)

# この順番を間違うとだめですよ
dp = [[0] * (t+1) for _ in range(s+1)]

for k in range(1,s+1):
    for l in range(1,t+1):
        dp[k][l] = max(dp[k-1][l], dp[k][l-1])

        if S[k-1] == T[l-1]:
            dp[k][l] = max(dp[k-1][l-1]+1, dp[k][l])

print(dp[s][t])
