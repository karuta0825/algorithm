# Grundy数なるものをしる
N, X, Y = map(int, input().split())

Z = 100000
grundy = [0] * (Z+1)

for i in range(X, Z+1):
    available = []
    for j in [X, Y]:
        nxt = i - j
        if nxt < 0: continue
        available.append(grundy[nxt])

    while grundy[i] in available:
        grundy[i] += 1

A = list(map(int, input().split()))

g = 0

for a in A:
    g ^= grundy[a]

if g == 0:
    print("Second")
else:
    print("First")
