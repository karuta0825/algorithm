from collectios import deque
N, D = map(int, input().split())

P = [0] + [list(map(int, input().split())) for _ in range(N)]

zs = deque(P[1])

def kyori(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (x1 - x2) ** 2 + (y1 - y2) ** 2

goal = [True] * (N+1)
goal[1] = False

while len(zs):
    z = zs.popleft()

    for i in range(1, N+1):
        if not goal[i]:
            continue

        if kyori(z, P[i]) <= D ** 2:
            goal[i] = False
            zs.append(P[i])

for i in goal[1:]:
    if i:
        print("No")
    else:
        print("Yes")
