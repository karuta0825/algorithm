N = int(input())

P = []
A = []

for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [[0] * (N+1) for _ in range(N+1)]

for l in range(N):
    for r in range(N-1, -1, -1):

        # print([l,r])
        if l-1 >= 0:
            if l <= P[l-1]-1 <= r:
                L = dp[l-1][r] + A[l-1]
            else:
                L = dp[l-1][r]
        else:
            L = 0

        if r+1 <= N-1:
            if l <= P[r+1]-1 <= r:
                R = dp[l][r+1] + A[r+1]
            else:
                R = dp[l][r+1]
        else:
            R = 0

        dp[l][r] = max(L, R)


ans = 0
for i in range(N):
    ans = max(dp[i][i], ans)



print(ans)
