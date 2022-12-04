n = input()
ss = list(map(int, input().split()))


a = []

for i in range(len(ss)):
    if (i == 0):
        a.append(ss[i])
    else:
        pI = i - 1
        pV = ss[i] - ss[pI]
        a.append(pV)

print(*a)
