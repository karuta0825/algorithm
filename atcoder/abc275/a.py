n = int(input())

bridges = list(map(int, input().split()))

minv = 0
for i in range(len(bridges)):
    if (bridges[minv] < bridges[i]):
        minv = i

print(minv + 1)
