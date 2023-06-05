D = int(input())
N = int(input())

Yo = [0] * (D+1)

for _ in range(N):
    L, R = map(int, input().split())

    Yo[L] += 1
    # これがないと駄目。
    if R <= D - 1:
        Yo[R+1] -= 1

for i in range(1, D+1):
    Yo[i] = Yo[i] + Yo[i-1]

for i in Yo[1:]:
    print(i)
