from collections import deque

N = int(input())
A = list(map(int, input().split()))

m = {}
dist = {}
ans = {}
for i in range(N):
    m[i+1] = []
    dist[i+1] = -1
    ans[i+1] = 0

dist[1] = 0

for (i, top) in enumerate(A):
    i += 2
    m[top].append(i)

q = deque()
q.append(1)

while len(q):

    pos = q.popleft()

    for to in m[pos]:

        if dist[to] == -1:
            dist[to] = dist[pos] + 1
            q.append(to)

for pos, depth in sorted(dist.items(), key=lambda x: x[1], reverse=True):
    t = 0
    for i in m[pos]:
        t += ans[i] + 1

    ans[pos] = t


print(*list(ans.values()))
