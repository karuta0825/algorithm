H, W, N = map(int, input().split())

acm = [[0] * (W+2) for _ in range(H+2)]

for _ in range(N):
    A, B, C, D = map(int, input().split())

    acm[A][B] += 1
    acm[A][D+1] -= 1
    acm[C+1][B] -= 1
    acm[C+1][D+1] += 1

# 二次元配列の累積和を求める
for i in range(1, H+1):
    for j in range(1, W+1):
        acm[i][j] += -acm[i-1][j-1] + acm[i][j-1] + acm[i-1][j]


for i in acm[1:H+1]:
    print(*i[1:W+1])
