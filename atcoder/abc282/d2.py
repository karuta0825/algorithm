from collections import deque
N, M = map(int, input().split())

g = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(lambda x: int(x) - 1 , input().split())

    g[u].append(v)
    g[v].append(u)


color = [-1 for _ in range(N)]

# なるほど、連結成分が複数存在することがありうるのか！
# だから連結成分ごとに計算しないといけないんだ！理解した
# あほだな

for i in range(N):
    if color[i] >= 0:
        continue

    que = deque()
    color[i] = 1
    que.append(i)

    # ここにないと駄目ですね。どうして？
    one = 0
    two = 0

    while que:
        x = que.popleft()

        if color[x]==1:
            one += 1
        else:
            two += 1

        for n in g[x]:
            if color[n] == color[x]:
                print(0)
                exit()

            if color[n]<0:
                color[n]=color[x]^1
                que.append(n)

ans=N*(N-1)//2-M
# one = 0
# two = 0
# for i in range(N):
#     if color[i] == 1:
#         one += 1
#     else:
#         two += 1

ans -= (one * (one-1))// 2 + (two * (two-1)) // 2
print(ans)
