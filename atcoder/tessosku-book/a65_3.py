# 幅優先探索をつかって一番枝にいるところをみつける。
# 幅優先の計算量っていくらなんだろうね？
# 木構造
from collections import deque
N = int(input())
A = list(map(int, input().split()))

G = {}
for i in range(1,N+1):
    G[i] = []

for i in range(N-1):
    G[A[i]].append(i+2)

dist = {1: 0}

que = deque([1])

while len(que):

    q = que.popleft()

    for n in G[q]:
        dist[n] = dist[q] + 1
        que.append(n)

child = [0] * (N+1)

# あとはこれで大きいやつを順番で
for i, d in sorted(dist.items(), key=lambda x: x[1], reverse=True):

    kyori = child[i] + len(G[i])
    for s in G[i]:
        kyori += child[s]

    child[i] = kyori

print(*child[1:])
