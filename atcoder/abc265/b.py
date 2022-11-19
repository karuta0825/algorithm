n, m, t = map(int, input().split())

an = list(map(int, input().split()))

obj = {}
for [i, y] in [list(map(int, input().split())) for _ in range(m)]:
    obj[i-1] = y

# print(obj)

result = "Yes"
for i in range(len(an)):
    t -= an[i]
    if (i in obj):
        t += obj[i]

    if (t < 1):
        result = "No"
        break

print(result)
