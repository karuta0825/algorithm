N = int(input())
S = input()

d = {"00": 1}

now = (0,0)

ans = "No"

for s in S:

    x, y = now

    if (s == "R"):
        now = (x + 1, y)

    if (s == "L"):
        now = (x - 1, y)

    if (s == "U"):
        now = (x, y + 1)

    if (s == "D"):
        now = (x, y - 1)

    pos = "{}{}".format(now[0], now[1])
    if not (pos in d):
        d[pos] = 1
    else:
        d[pos] += 1

    if (d[pos] > 1):
        ans = "Yes"

print(ans)
