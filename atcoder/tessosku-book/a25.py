# なるほどルート計算の問題か！
# まず全探索するとどうなるのかを考えてみよう。

H, W = map(int, input().split())
bads = []
for i in range(H):
    row = input()
    for j in range(len(row)):
        if (row[j] == "#"):
            bads.append((i+1,j+1))


dp = [[0] * (W+1) for _ in range(H+1)]
dp[1][1] = 1


for h in range(1, H+1):
    for w in range(1, W+1):
        if (h == 1 and w == 1):
            continue

        if ((h,w) in bads):
            continue

        if ((h-1, w) in bads and (h, w-1) in bads):
            continue

        if ((h-1, w) in bads):
            dp[h][w] = dp[h][w-1]

        if ((h, w-1) in bads):
            dp[h][w] = dp[h-1][w]

        dp[h][w] = dp[h-1][w] + dp[h][w-1]

print(dp[H][W])
