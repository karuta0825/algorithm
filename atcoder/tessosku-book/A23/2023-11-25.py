# N: 品物の種類
# M: クーポンの種類
N, M = map(int, input().split())

coupons = [list(map(int, input().split())) for _ in range(M)]

def ten2two(val):
    ary = []
    for i in range(N):
        v = 1 if (val // (2 ** i)) % 2 == 1 else 0
        ary.append(v)
    return ary

def two2ten(ary):
    val = 0
    for i in range(N):
        val += ary[i] * (2 ** i)
    return val

def wa(x,y):
    ary = []
    for i in range(N):
        val = 0
        if x[i] == 1 or  y[i] == 1:
            val = 1

        ary.append(val)

    return ary

DEF = 10 ** 10
MAX = two2ten([1] * N)
dp = [[DEF] * (MAX+1) for _ in range(M+1)]
dp[0][0] = 0

for i in range(1, M+1):
    for j in range(MAX+1):

        nxt = two2ten(wa(ten2two(j), coupons[i-1]))

        dp[i][j] = min(dp[i-1][j], dp[i][j])
        dp[i][nxt] = min(dp[i][nxt], dp[i-1][j] + 1)

ans = dp[M][MAX]
print(-1 if ans == DEF else ans)
