import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())

r = {}
visited = [0] * (N+1)

r = {}
for i in range(1, N+1):
    r[i] = []

for _ in range(M):
    A, B = map(int, input().split())

    r[A].append(B)
    r[B].append(A)


def dfs(pos):
    if (visited[pos]):
        return

    visited[pos] = 1

    for n in r[pos]:
        dfs(n)

start = list(r.keys())[0]
dfs(start)


if (all(visited[1:])):
    print('The graph is connected.')
else:
    print("The graph is not connected.")
