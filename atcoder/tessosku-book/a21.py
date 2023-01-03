N = int(input())
PA = [list(map(int, input().split())) for i in range(N)]

# print(PA)

dp = [[0] * (N+1) for _ in range(N+1)]

for width in range(N-1, -1, -1):
    for l in range(N):
        r = l + width

        if r > N:
            break

        # 左側
        if l-1 >= 0:
            p, a = PA[l-1]
            p -= 1
            dp[l][r] = max(
                dp[l-1][r] + (a if l-1 <= p < r else 0),
                dp[l][r])

        # 右側
        if r+1 <= N:
            p, a = PA[r]
            p -= 1
            dp[l][r] = max(
                dp[l][r+1] + (a if l <= p < r+1 else 0),
                dp[l][r])

        # print([l,r], dp[l][r])


# そうか(1,1)とはl,rが一致したときなので計算が終了したときなんだ！
# [[i,i] for i in range(5)]
print(max(dp[i][i] for i in range(N+1)))
