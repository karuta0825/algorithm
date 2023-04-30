N, M = map(int, input().split())

A = list(map(lambda x: (int(x), "A"), input().split()))
B = list(map(lambda x: (int(x), "B"), input().split()))

C = sorted([*A, *B], key=lambda x: x[0])

ansA = []
ansB = []
for i in range(len(C)):

    (_, g) = C[i]

    if g == "A":
        ansA.append(i+1)
    else:
        ansB.append(i+1)

print(*ansA)
print(*ansB)
