N, Q = map(int, input().split())
A = list(map(int, input().split()))

L = 30
dp =  [[0] * N for _ in range(L)]

for i in range(N):
    dp[0][i] = A[i] - 1

for d in range(1, L):
    for i in range(0, N):
        dp[d][i] = dp[d-1][dp[d-1][i]]


for _ in range(Q):
    X, Y = map(int, input().split())
    X -= 1

    current_pos = X
    for i in range(L):
        if (Y // (1 << i)) % 2 == 1:
            current_pos = dp[i][current_pos]

    print(current_pos + 1)
    




