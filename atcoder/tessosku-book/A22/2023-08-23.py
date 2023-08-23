N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

INF = 10 ** 10
dp = [-INF] * (N+1)
dp[1] = 0


for i in range(1, N):

    dp[A[i]] = max(dp[i] + 100, dp[A[i]])    
    dp[B[i]] = max(dp[i] + 150, dp[B[i]])


print(dp[-1])

