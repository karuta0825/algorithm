# 偶数個ならば、先手からスタート
# 奇数子ならば、後手からスタート
N = int(input())
A = list(map(int, input().split()))


# dpはどういう構造か？
# dp[i][j]
# i段目のj番目の数値e
dp = []

for i in range(1, N):
    dp.append([0] * i)


dp.append(A)

for i in range(N, 0, -1):
    i -= 1
    for j in range(len(dp[i])-1):

        if (i % 2 == 0):
            dp[i-1][j] = min(dp[i][j], dp[i][j+1])
        else:
            dp[i-1][j] = max(dp[i][j], dp[i][j+1])

print(dp[0][0])
