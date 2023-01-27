X, Y, Z = map(int, input().split())

if (X > 0): 
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
else:
    if not (X >= Y >= 0):
        print(abs(X))
        exit()

    if (Z < Y):
        print(-1)
    else:
        if (Z > 0):
            print(2 * Z + abs(X))
        else:
            print(abs(X))


