N, X = map(int, input().split())

A = list(map(int, input().split()))

obj = {}

for a in A:
    obj[a] = 1


for a in obj:

    J = -1 * (X - a)

    if (J in obj):
        print("Yes")
        exit()

print("No")
