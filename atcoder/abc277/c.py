import sys
sys.setrecursionlimit(10**9)

N = int(input())

G = {}
visited = {}

max_value = 0
for _ in range(N):
    A, B = map(int, input().split())

    if (A in G):
        G[A].append(B)
    else:
        G[A] = [B]

    if (B in G):
        G[B].append(A)
    else:
        G[B] = [A]

    max_value = max(max_value, A, B)
    visited[A] = 0
    visited[B] = 0

def dfs(i, r):

    visited[i] = 1
    r.append(i)

    if not (i in G):
        return r

    for j in G[i][:]:
        if (visited[j] == 1):
            continue
        else:
            dfs(j, r)

    return r


print(max(dfs(1, [])))
