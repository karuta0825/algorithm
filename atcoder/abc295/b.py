R, C = map(int, input().split())

row = [input() for _ in range(R)]

bombs = []

for i, r in enumerate(row):
    for j, c in enumerate(r):
        if (c != '.' and c != '#'):
            bombs.append((int(c), i,j))

# これの戦略はどうしたらいいんだろうんかね？
# マンハッタン距離というのを求められたらそれでいいのだろうか？
# 各ボムごとに点を求めていう全探索もありだな。計算量的に。

def kyori(r, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1-x2) + abs(y1-y2)) <= r

def kyorib(p):
    for h, x, y in bombs:
        if kyori(h, (x,y), p):
            return True
    return False


# これでいけるけども、なんだかエレガントじゃないなという反省があるね。
for i, r in enumerate(row):
    line = ""
    for j, c in enumerate(r):

        if (kyorib((i,j))):
            line += "."
        else:
            if c == "#":
                line += c
            else:
                line += "."

    print(line)
