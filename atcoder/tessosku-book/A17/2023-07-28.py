N = int(input())
A = [0] + list(map(int,input().split()))
B = [0, 0] + list(map(int,input().split()))

dp = [0] * (N)

for i in range(1, N):

    if i == 1:
        dp[i] = dp[i-1] + A[i]
    else:
        dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

    print(dp)

print(dp[N-1])
