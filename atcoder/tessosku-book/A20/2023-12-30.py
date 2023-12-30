S = input()
T = input()

dp = [[0] * (len(S) + 1) for _ in range(len(T) + 1)]

# for d in dp:
#     print(d)

for i in range(1, len(T)+1):
    for j in range(1, len(S)+1):
        # print([i,j])
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + 1 if T[i-1] == S[j-1] else dp[i][j-1])

# for d in dp:
#     print(d)

print(dp[len(T)][len(S)])
