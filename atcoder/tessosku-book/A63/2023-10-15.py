from collections import deque
N, M = map(int, input().split())

m = {}
for i in range(N):
    m[i+1] = []

for _ in range(M):
    A, B = map(int, input().split())
    m[A].append(B)
    m[B].append(A)

s = deque()
s.append(1)
dist = {}
for i in range(N):
    dist[i+1] = -1
dist[1] = 0

while len(s) >= 1:

    pos = s.popleft()

    for next_pos in m[pos]:
        if dist[next_pos] == -1:
            dist[next_pos] = dist[pos] + 1
            s.append(next_pos)

for k in range(N):
    print(dist[k+1])
