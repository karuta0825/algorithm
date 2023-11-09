N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1


for i in range(1, N+1):
    for j in range(S+1):
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            if (j + A[i-1] <= S):
                dp[i][j + A[i-1]] = 1


goal = S
ans = []
for i in range(N, 0, -1):
    if dp[i-1][goal] == dp[i][goal] == 1:
        continue

    if dp[i-1][goal] == 0 and dp[i][goal] == 1:
        ans.append(i)
        goal -= A[i-1]


ans.reverse()
# for d in dp:
#     print(d)

if len(ans):
    print(len(ans))
    print(*ans)
else:
    print(-1)
