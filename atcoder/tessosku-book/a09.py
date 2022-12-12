H, W, N = map(int, input().split())

accum = [[0] * (W + 1) for _ in range(H + 1)]

for [x1, y1, x2, y2] in [list(map(int, input().split())) for _ in range(N)]:
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    accum[x1][y1] += 1
    accum[x2 + 1][y1] -= 1
    accum[x1][y2 + 1] -= 1
    accum[x2 + 1][y2 + 1] += 1


# for i in accum:
#     print(*i)

# print('-----------------')

# val = 0
ary = []
zan = [0]  * (W)

for i in range(H):
    val = 0
    for j in range(W):
        val += accum[i][j]
        ary.append(val + zan[j])

    print(*ary)
    zan = ary.copy()
    ary = []
