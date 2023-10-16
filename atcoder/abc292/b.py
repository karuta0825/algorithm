N, Q = map(int, input().split())

p = {}
for i in range(N):
    p[i+1] = 0


for _ in range(Q):
    e, v = map(int, input().split())

    if e == 1:
        p[v] += 1

    if e == 2:
        p[v] += 2

    if e == 3:
        if p[v] > 1:
            print("Yes")
        else:
            print("No")
