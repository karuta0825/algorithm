from collections import deque
N, M = map(int, input().split())

m = {}
for i in range(N):
n    m[i+1] = {}

for _ in range(M):
    A, B, C = map(int, input().split())
    m[A][B] = C
    m[B][A] = C

s = deque()
s.append(1)
dist = {}
MAX = 10 ** 9

for i in range(N):
    dist[i+1] = MAX
dist[1] = 0

while len(s):
    pos = s.popleft()

    for next_pos in m[pos]:
        if dist[next_pos] > dist[pos] + m[pos][next_pos]:
            dist[next_pos] = dist[pos] + m[pos][next_pos]
            s.append(next_pos)

for k in range(N):
    if dist[k+1] == MAX:
        print(-1)
    else:
        print(dist[k+1])
