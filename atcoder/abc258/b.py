n = int(input())

# pythonで二次元配列つくる方法
ary = [[0] * n  for _ in range(n)]
M = 0
As = [input() for _ in range(n)]
pos = []

# 最大値のものが複数ある場合はいずれの場合も確認しないと
for a in As:
    for v in a:
        if (int(v) > M):
            M = int(v)

for i in range(len(As)):
    for j in range(len(As[i])):
        num = int(As[i][j])
        if (M == num):
            pos.append((i, j))

        ary[i][j] = num

# 左右上下斜をどうやってあらわすか？
# (0,0)のとき
# ( 1,-1), (-1,0), (1,1)
# ( 0,-1), ( 0,0), (0,1)
# (-1,-1), (-1,0), (-1,1)

# 貪欲法でよいのかどうかってはなしだよね。次の一手が一番大きいものを探したいわけだ
step = [(1,-1), (-1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]

M = 0
for p in pos:
    result = [ary[p[0]][p[1]]]
    for s in step:
        for [x, y] in map(lambda x: (s[0] *x,s[1]*x), range(1, n)):
            xx = (p[0] + x) % n
            yy = (p[1] + y) % n
            result.append(ary[xx][yy])

        tmp = int("".join(map(str, result)))
        if (tmp > M):
            M = tmp
        result = [ary[p[0]][p[1]]]

print(M)
