from collections import defaultdict
from collections import deque

N = int(input())
A = list(map(int, input().split()))

g = defaultdict(list)
h = defaultdict(int)
for i in range(len(A)):
    pos = i + 2
    v = A[i]

    g[v].append(pos)
    h[pos] = v

# print(g)
# print(h)

# 幅優先をつくってみる

dist = defaultdict(int)

que = deque()
que.append(1)

# emptyてきなメソッドはあるのだろうか？
while len(que) > 0:
    pos = que.popleft()

    for to in g[pos]:
        if dist[to-1] == 0:
            que.append(to)
            dist[to-1] = dist[pos-1] + 1

# print(dist)

d = [0] * N
# 多いやつから順番にやるってことだよな。sortをどうするのかな？っておもうけど
# for i, path in enumerate(reversed(dist)):
#     x = 6 - i    
#     print(x, path)
for i in sorted(dist.items(), key=lambda x:x[1], reverse=True):
    (pos, l) = i
    if (l != 0):
        to = h[pos+1]
        d[to-1] += d[pos] + 1

print(*d)
