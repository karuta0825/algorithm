H, W = map(int, input().split())
cs = [input() for _ in range(H)]

# 0で初期化
cols = [0 for _ in range(W)]

for r in cs:
    for k in range(len(r)):
        if (r[k] == "#"):
            cols[k] += 1

print(*cols)
