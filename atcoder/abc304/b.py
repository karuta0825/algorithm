N = int(input())

m = {
    0: (0, 10 ** 3-1),
    1: (10 ** 3, 10 ** 4-1),
    2: (10 ** 4, 10 ** 5-1),
    3: (10 ** 5, 10 ** 6-1),
    4: (10 ** 6, 10 ** 7-1),
    5: (10 ** 7, 10 ** 8-1),
    6: (10 ** 8, 10 ** 9-1),
}

s = str(N)
target = 0

for k, mm in m.items():
    a, b = mm

    if a <= N <= b:
        target = k


if target == 0:
    print(N)
    exit()

g = list(reversed(s))

for i in range(target):
    g[i] = '0'


print("".join(reversed(g)))
