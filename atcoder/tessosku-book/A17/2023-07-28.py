N = int(input())
A = [0] + list(map(int,input().split()))
B = [0, 0] + list(map(int,input().split()))

dp = [0] * (N)

for i in range(1, N):

    if i == 1:
        dp[i] = dp[i-1] + A[i]
    else:
        dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])


i = N-1
t = [N]

while i > 0:

    if dp[i] == dp[i-1] + A[i]:
        i -= 1
        t.append(i+1)
    else:
        i -= 2
        t.append(i+1)

print(len(t))
print(*reversed(t))
