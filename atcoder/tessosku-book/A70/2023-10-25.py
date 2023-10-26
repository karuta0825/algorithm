from collections import deque
from collections import defaultdict
N, M = map(int, input().split())

A = list(map(int, input().split()))

B = []

for _ in range(M):
    X, Y, Z = map(lambda x: int(x)-1, input().split())
    B.append([X,Y,Z])


def ten2two(num, n):
    ary = []
    for i in range(n):
        keta = 1 if (num // (1 << i)) % 2 == 1 else 0
        ary.append(keta)
    return ary

def two2ten(ary):
    ans = 0
    for i in range(N):
        ans += ary[i] * (1 << i)

    return ans

m = defaultdict(list)

for i in range(1 << N):

    l = ten2two(i, N)
    for X, Y, Z in B:
        c = l.copy()
        c[X] = 1 - l[X]
        c[Y] = 1 - l[Y]
        c[Z] = 1 - l[Z]

        j = two2ten(c)
        # print(i, list(reversed(l)), [X,Y,Z], list(reversed(c)), j)
        m[i].append(j)

start = two2ten(A)
goal = two2ten([1] * N)


visited = [0] * (goal+1)
visited[start] = 1

queue = deque()
queue.append(start)

kyori = {}
kyori[start] = 0


while len(queue) > 0:

    q = queue.popleft()

    if (q == goal):
        break

    for i in m[q]:
        if (visited[i] == 1):
            continue
        else:
            visited[i] = 1
            kyori[i] = kyori[q] + 1
            queue.append(i)

if goal in kyori:
    print(kyori[goal])
else:
    print(-1)
