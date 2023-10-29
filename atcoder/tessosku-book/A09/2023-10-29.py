H, W, N = map(int, input().split())

Z = [[0] * (W+2) for _ in range(H+2)]

for _ in range(N):
    A, B, C, D = map(int, input().split())

    Z[A][B] += 1
    Z[A][D+1] -= 1
    Z[C+1][B] -= 1
    Z[C+1][D+1] += 1

for i in range(1, H+1):
    tmp = 0
    for j in range(1, W+1):
        tmp += Z[i][j]
        Z[i][j] = tmp


for i in range(1, W+1):
    tmp = 0
    for j in range(1, H+1):
        tmp += Z[j][i]
        Z[j][i] = tmp

for i in range(1, H+1):
    print(*Z[i][1:W+1])
