from collections import deque
N, M = map(int, input().split())
A = list(map(int, input().split()))

M = [list(map(lambda x: int(x)-1,input().split())) for _ in range(M)]

P = 2**N

G = [ list() for i in range(P)]



def get_next(pos, x, y, z):
    state = [ (pos // (2 ** i)) % 2 for i in range(N)]

    state[x] = 1 - state[x]
    state[y] = 1 - state[y]
    state[z] = 1 - state[z]

    ret = 0
    for i in range(N):
        if state[i] == 1:
            ret += 2**i

    return ret

for i in range(P):
    for x, y, z in M:
        nextstate = get_next(i, x, y, z)
        G[i].append(nextstate)


start = 0

for i in range(N):
    if A[i] == 1:
        start += 2 ** i

goal = 2 ** N - 1

dist = [-1] * P
dist[start] = 0

que = deque()
que.append(start)

while len(que) > 0:
    pos = que.popleft()

    for nxt in G[pos]:

        if dist[nxt] == -1:
            dist[nxt] = dist[pos] + 1
            que.append(nxt)

print(dist[goal])
