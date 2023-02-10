N, L = map(int, input().split())

E = []
W = []

for _ in range(N):
    A, B = map(lambda x:x, input().split())
    A = int(A)

    if (B == 'E'):
        E.append(A)
    else:
        W.append(A)


e = abs(L - min(E)) if len(E) > 0 else 0
w = max(W) if len(W) > 0 else 0

print(max(e, w))
