H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
target = []

for i in range(2 ** (H+W-2)-1):

    val = format(i,'b')
    oneSum = 0
    for c in val:
        if (c == "1"):
            oneSum += 1

    if oneSum == H-1:
        target.append(val.zfill(H+W-2))

# なるほど長方形か！
for t in target:

    x = 0
    y = 0
    v = set([A[0][0]])

    for c in t:
        if (c == "1"):
            x += 1
        else:
            y += 1

        v.add(A[x][y])

    if H+W-2 == len(v)-1:
        ans += 1

print(ans)
