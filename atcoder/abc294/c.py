N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A = [3, 14, 15, 92]

# B = [6, 53, 58]

a = list(map(lambda x: (A[x], "A"), range(len(A))))
b = list(map(lambda x: (B[x], "B"), range(len(B))))

C = [*a, *b]
c = sorted(C, key=lambda x: x[0])

ansA = []
ansB = []
for i in range(len(c)):

    (_, g) = c[i]

    if g == "A":
        ansA.append(i+1)
    else:
        ansB.append(i+1)

print(*ansA)
print(*ansB)
