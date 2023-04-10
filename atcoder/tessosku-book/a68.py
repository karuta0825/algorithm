# これはむずかしいな
N, M = map(int, input().split())
edge = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A][B] = C


come = [False] * (N+1)

def dfs(now, goal, flow):

    come[now] = True

    if now == goal:
        return flow

    for to in range(1, N+1):

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
    come = [False] * (N+1)
    f = dfs(1, N, 10**10)
    if f == 0:
        break

    ans += f


print(ans)
