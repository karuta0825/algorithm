N = int(input())
PA = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]


# 1 <= l <= N
# 1 <= r <= N
for l in range(1, N+1):
    for r in range(N):
        r = N-r

        if l > r:
            continue

        if l-1 > 0:
            lp, la = PA[l-1-1]
            dp[l][r] = max(dp[l][r], dp[l-1][r] + (la if l <= lp <= r else 0))
            # print([l, lp, r], 'la', la)

        if r < N:
            rp, ra = PA[r+1-1]
            dp[l][r] = max(dp[l][r], dp[l][r+1] + (ra if l <= rp <= r else 0))
            # print([l, rp, r],'ra', ra)


# for i, d in enumerate(dp):
#     print((d[i]))
ans = 0
for i in range(N+1):
    ans = max(ans, dp[i][i])

print(ans)
