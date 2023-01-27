X, Y, Z = map(int, input().split())

if (X < 0):
    X = -1 * X
    Y = -1 * Y
    Z = -1 * Z

if not (0 <= Y <= X):
    print(X)
    exit()


if (Z > Y):
    print(-1)
else:
    if (Z < 0):
        print(2 * abs(Z) + X)
    else:
        print(X)
