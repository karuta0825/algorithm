N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N)

# ここの添字を理解することが難しいな！
# もっと楽にかんがえる方法はないかな？
for i in range(N-1, 0, -1):
    pos = A[i-1] - 1
    dp[pos] += dp[i] + 1

print(*dp)
