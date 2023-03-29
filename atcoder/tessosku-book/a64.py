from collections import deque
# 重みのグラフってどういうデータ構造だろうね？

# {
#     1: [{2: 20}]
#     2: [{1: 20}]
# }

# こういうデータ構造じゃないかな？
# {
#     1: {2: 20}
# }

N, M = map(int, input().split())

MAX = 10 ** 9
g = {}
dist = {}
visited = {}

for i in range(1, N+1):
    g[i] = {}
    dist[i] = MAX
    visited[i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    g[A][B] = C
    g[B][A] = C

Q = deque()
Q.append(1)
dist[1] = 0

while len(Q) > 0:
    pos = Q.popleft()

    # if (visited[pos]):
    #     continue

    # visited[pos] = 1
    for to in g[pos]:

        w = g[pos][to]

        if dist[to] > dist[pos] + w:
            dist[to] = dist[pos] + w
            Q.append(to)

for i in range(1, N+1):
    if dist[i] == MAX:
        print(-1)
    else:
        print(dist[i])
