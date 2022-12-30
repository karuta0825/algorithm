N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

sumW = 0
for wv in WV:
    sumW += wv[0]
    
# i \ w
# dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i]])

dp = [[0] * (sumW+1) for _ in range(N+1)]

for i in range(1, N+1):
    [wgt,val] = WV[i-1]

    for w in range(sumW+1):
        if (w - wgt >= 0):
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-wgt] + val)
        else:
            dp[i][w] = dp[i-1][w]

# for x in range(len(dp)):
#     print(dp[x])
    
print(dp[N][W])
 

