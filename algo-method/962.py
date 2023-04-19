from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    g[a].append(b)
    g[b].append(a)


color = [-1 for _ in range(N)]

ans = 'YES'

for v in range(N):

    if color[v] != -1:
        continue

    que = deque([])
    color[v] = 0
    que.append(v)

    while len(que) > 0:

        x = que.popleft()

        for nxt in g[x]:

            if color[nxt] != -1:
                if color[x] == color[nxt]:
                    ans = "No"
                continue

            color[nxt] = 1 - color[x]
            que.append(nxt)


print(ans)
