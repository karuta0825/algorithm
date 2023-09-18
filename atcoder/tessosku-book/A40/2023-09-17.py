import math
N = int(input())

obj = {}

for i in list(map(int, input().split())):

    if not (i in obj):
        obj[i] = 1
    else:
        obj[i] +=1

ans = 0

for i in obj:
    if obj[i] < 3:
        continue

    ans += math.comb(obj[i], 3)

print(ans)
