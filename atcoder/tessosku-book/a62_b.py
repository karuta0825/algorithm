import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())

r = {}
visited = [0] * (N+1)

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


def dfs(pos):
    visited[pos] = 1

    for n in r[pos]:
        if (visited[n]):
            continue
        dfs(n)


if (M == 0):
    if (N == 1):
        print("The graph is connected.")
        exit()
    else:
        print("The graph is not connected.")
        exit()

start = list(r.keys())[0]
dfs(start)


if (all(visited[1:])):
    print('The graph is connected.')
else:
    print("The graph is not connected.")
