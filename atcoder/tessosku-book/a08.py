H, W = map(int, input().split())
Xs = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]


for abcd in ABCD:
    a = abcd[0] - 1
    b = abcd[1] - 1
    c = abcd[2] - 1
    d = abcd[3] - 1

    value = 0
    for h in range(a, c + 1):
        for w in range(b, d + 1):
            value += Xs[h][w]
    print(value)





