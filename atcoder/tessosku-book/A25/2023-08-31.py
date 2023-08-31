H, W = map(int, input().split())

dp = [[0] * (W+1) for _ in range(H+1)]
dp[1][1] = 1

bans = []

for i in range(H):
    for (j, c) in enumerate(input()):

        if c == "#":
            bans.append((i+1, j+1))


for i in range(1, H+1):
    for j in range(1, W+1):

        if i == 1 and j == 1:
            continue

        if (i,j) in bans:
            continue

        L = 0 if (i-1, j) in bans else dp[i-1][j]
        U = 0 if (i, j-1) in bans else dp[i][j-1]

        dp[i][j] = L + U


print(dp[H][W])
