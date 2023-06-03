# これはむずかしいな
N, M = map(int, input().split())
edge = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A][B] = C


come = [False] * (N+1)

# 第三引数のflowは、nowからgoalに流すことのできる水量を表す
def dfs(now, goal, flow):

    come[now] = True

    if now == goal:
        return flow

    for to in range(1, N+1):

        # edge[now][to] == 0はパスが存在しないことを意味する
        if come[to] or edge[now][to] == 0:
            continue

        f = dfs(to, goal, min(flow, edge[now][to]))

        # １つ目の経路を見つけたけど、その先の経路が全て駄目だったときこの関数の最後のreturn 0に入る
        # これのときf = 0になる
        # 上のedge[now][to]の違いは、continueかどうかである
        # continueになる結果return 0を通過するのでその処理を意味してる
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
