N, M = map(int, input().split())

r = {}

for _ in range(M):
    A, B = map(int, input().split())

    if (A in r):
        r[A].append(B)
    else:
        r[A] = [B]

    if (B in r):
        r[B].append(A)
    else:
        r[B] = [A]

for i in range(1, N+1):

    if (i in r):
        print("{}: {}".format(i, set(r[i])))
    else:
        print("{}: {}".format(i, "{}"))
