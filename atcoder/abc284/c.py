N, M = map(int, input().split())

# if (M == 0):
#     print(N)
#     exit()

# これでもよいけどvisitedという名前のほうがわかりやすい
# route = [0] * N
visited = [0] * (N+1)

obj = {}
for i in range(1, N+1):
    obj[i] = []

cnt = 0

# やっぱりDFSまたはBFSをつかわないといけないな。
# 今日はこれができるようになる訓練だな。
# できるようになれば成長したっていえるな。
for _ in range(M):
    u, v = map(int, input().split())
    obj[u].append(v)
    obj[v].append(u)


# dfsとbfsを実装してみよう
# 再帰が必要になるんだよな。。。
# dfsができない。
def bfs(i, r):
    global cnt
    # 終了条件を入れる
    if (visited[i] == 1):
        return r

    visited[i] = 1
    if (len(r) == 0):
        cnt += 1

    queue = obj[i][:]

    while (len(queue) > 0):
        q = queue.pop(0)
        if (visited[q] == 1):
            continue
        else:
            r.append(q)
            r = bfs(q, r)

    return r

# visited = [0] * 6
# obj = {
#     1: [2,3],
#     2: [1],
#     3: [1],
#     4: [5]
# }

# for i in range(1, N+2):
for i in range(1, N+1):
    r = []
    ary = bfs(i, r)
    # if(len(ary) > 0):
    #     cnt += 1

print(cnt)
