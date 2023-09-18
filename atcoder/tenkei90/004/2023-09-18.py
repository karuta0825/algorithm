H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

rs = []
cs = []

# N
for a in A:
    rs.append(sum(a))

# N ^ 2
for i in range(W):
    c = 0
    for j in range(H):
        c += A[j][i]

    cs.append(c)

for i in range(H):
    col = []
    for j in range(W):
        col.append(rs[i] + cs[j] - A[i][j])

    print(*col)
    col = []
