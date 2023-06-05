H, W = map(int, input().split())
X = [[0] * (W+1)] +
[
    [0] + list(map(int, input().split())) for _ in range(H)
]

Q = int(input())

# Z = [[0] * (W+1) for _ in range(H+1)]
# 横に足していく
# for i in range(1, H+1):
#     for j in range(1, W+1):
#         # 今入ってる値に前(左の)値を足してる
#         Z[i][j] = X[i-1][j-1] + Z[i][j-1]

# for i in range(1, W+1):
#     for j in range(1, H+1):
#         # 今入ってる値に前(上の)値を足してる
#         Z[i][j] = Z[i-1][j] + Z[i][j]

for i in range(1, H+1):
    for j in range(1, W+1):
        X[i][j] += -X[i-1][j-1] + X[i-1][j] + X[i][j-1]

for _ in range(Q):
    A, B, C, D = map(int, input().split())

    print(X[C][D] + X[A-1][B-1] - X[C][B-1] - X[A-1][D])
