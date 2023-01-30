# これではとけなかった
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]

visited = [0] * (N+1)
visited[0] = 1

for _ in range(M):
    u, v = map(int, input().split())

    G[u].append(v)
    G[v].append(u)


def dfs(r, now, prev = -1):
    r.append(now)

    if (visited[now]):
        return r

    visited[now] = 1

    for g in G[now]:

        if (g == prev):
            continue

        r = dfs(r, g, now)

    return r

if (len(G[1]) == 0):
    print("No")
    exit()

# これをつけてうまく行った。 なるほど他の漢字があるのね
for g in G:
    if (len(g) > 2):
        print("No")
        exit()


path = dfs([], G[1][0])
# ここをもうすこし厳密にしてみる？
if (sum(path) == sum(range(1, N+1)) and sum(visited) == N+1):
    print("Yes")
else:
    print("No")
