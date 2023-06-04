W, H = map(int, input().split())
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

t1 = int(input())
A = [0] + list(map(int, input().split())) + [W]
t2 = int(input())
B = [0] + list(map(int, input().split())) + [H]

# 累積和を計算しておこう
# この時点でメモリ使いすぎてアウトになることを学ぼう！
# 発想は良かったんだけどね
X = [[0] * (W) for _ in range(H)]
Z = [[0] * (W+1) for _ in range(H+1)]

for (x, y) in P:
    X[x-1][y-1] = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        Z[i][j] = Z[i][j-1] + X[i-1][j-1]

# 縦方向に累積和をとる
for j in range(1, W+1):
    for i in range(1, H+1):
        Z[i][j] = Z[i-1][j] + Z[i][j]

# for x in X:
#     print(*x)

# print("----------")
# for z in Z:
#     print(*z)

def kosu(p1, p2):
    A, B = p1
    C, D = p2
    return Z[C][D] + Z[A][B] - Z[A][D] - Z[C][B]


# print(A)
# print(B)

g = []
for i in range(1, len(A)):
    for j in range(1, len(B)):
        # print((B[j-1], A[i-1]), (B[j], A[i]))
        # print(kosu((B[j-1], A[i-1]), (B[j], A[i])))
        g.append(kosu((B[j-1], A[i-1]), (B[j], A[i])))

print(min(g), max(g))
