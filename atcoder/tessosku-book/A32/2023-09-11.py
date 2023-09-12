n, a ,b = map(int, input().split())

dp = [0] * (n+1)

f = 1
s = -1
for i in range(n+1):

    x = dp[i-a] if i - a >= 0 else 0
    y = dp[i-b] if i - b >= 0 else 0

    if x == 0 and y == 0:
        dp[i] = s
        continue

    if x == 0 or y == 0:
        if x == 0:
            dp[i] = -1 * y
            continue

        if y == 0:
            dp[i] = -1 * x
            continue

    if x * y == -1:
        dp[i] = f
    else:
        dp[i] = -1 * x

if dp[-1] == f:
    print('First')
else:
    print('Second')
