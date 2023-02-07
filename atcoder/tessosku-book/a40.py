N = int(input())
A = list(map(int, input().split()))

def c(n):
    return int(n * (n-1) * (n-2) / 6)


obj = {}

for i in A:
    if (i in obj):
        obj[i] += 1
    else:
        obj[i] = 1


ans = 0
for k in obj:
    if obj[k] >= 3:
        ans += c(obj[k])

print(ans)
