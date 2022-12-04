h, w = map(int, input().split())
ss = [input() for _ in range(h)]

result = 0
for s in ss:
    for c in s:
        if (c == "#"):
            result += 1

print(result)
