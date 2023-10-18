from collections import defaultdict
N, M = map(int,input().split())

edge = {}
for i in range(N):
    edge[i+1] = defaultdict(int)

for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A][B] = C

# 1->2までの距離が10であるを示す
# {1: {2: 10}}
come = [0] * (N+1)

def dfs(now, goal, flow):
    come[now] = True

    if now == goal:
        return flow

    for to in edge[now]:

        if come[to] or edge[now][to] == 0:
            continue

        f = dfs(to, goal, min(flow, edge[now][to]))


        if f == 0:
            continue

        edge[now][to] -= f
        edge[to][now] += f

        return f

    return 0

ans = 0

while True:
    come = [0] * (N+1)
    f = dfs(1, N, 10 ** 10)

    if f == 0:
        break

    ans += f

print(ans)
