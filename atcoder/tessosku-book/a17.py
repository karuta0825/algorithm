N = int(input())
A = [0, *list(map(int, input().split()))]
B = [0, 0, *list(map(int, input().split()))]

dp = [0] * N
routes = [0] * N

# なぜ1から開始するのか？なぜN-1でとまるのか？
for i in range(1, N):
    if (i == 1):
        dp[i] = dp[i-1] + A[i]
        routes[i] = i-1
    else:
        if (dp[i-1] + A[i] < dp[i-2] + B[i]):
            dp[i] = dp[i-1] + A[i]
            routes[i] = i-1
        else:
            dp[i] = dp[i-2] + B[i]
            routes[i] = i-2




# 0indexにしてるためN-1が一番最後の値となる
ans = [N-1]
now = N-1
while now != 0:
    now = routes[now]
    ans.append(now)

ans.reverse()

print(len(ans))
print(*[x + 1 for x in ans])
