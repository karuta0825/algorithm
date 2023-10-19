from collections import defaultdict
N = int(input())
edge = {}

MAX = 200
for i in range(N+1):
    edge[i] = defaultdict(int)
    edge[i + MAX + 1] = defaultdict(int)

for i in range(1, N+1):
    # start
    edge[0][i] = 1
    # end
    edge[i + MAX][MAX + N + 1] = 1

for i in range(N):
    for j, v in enumerate(input()):
        if v == '#':
            edge[i+1][MAX + j + 1] = 1

come = [0] * (MAX + N + 2)


def dfs(now, goal, flow):
    come[now] = True

    if now == goal:
        return flow

    for to in edge[now]:

        if come[to] or edge[now][to] == 0:
            continue

        f = dfs(to, goal, min(flow, edge[now][to]))
        # print([goal, now, to, f])


        if f == 0:
            continue

        edge[now][to] -= f
        edge[to][now] += f

        return f

    return 0

ans = 0

while True:
    come = [0] * (MAX+N+2)
    f = dfs(0, MAX+N+1, 10 ** 10)

    if f == 0:
        break

    ans += f

print(ans)


