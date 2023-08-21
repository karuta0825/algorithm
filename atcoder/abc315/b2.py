from bisect import bisect_left
M = int(input())
D = list(map(int, input().split()))

m = (sum(D) + 1) // 2

S = []
for d in D:
    b = S[-1] if len(S) else 0
    S.append(b+d)

i = bisect_left(S, m)

# mを減らしていく発想ね！それは面白い
for n in range(i):
    m -= D[n]

print(i+1, m)
