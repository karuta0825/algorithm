import sys
sys.setrecursionlimit(10**9)

from collections import  defaultdict
N, M = map(int, input().split())

visited = [0] * (N+1)
visited[0] = 1

m = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    m[A].append(B)
    m[B].append(A)


def dfs(pos):

    if visited[pos]:
        return

    visited[pos] = 1

    for next_pos in m[pos]:
        dfs(next_pos)


dfs(1)

if all(visited):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
