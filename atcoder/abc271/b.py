N, Q = map(int, input().split())

lines = {}
for i in range(N):
    lines[i+1] = list(map(int, input().split()))[1:]

for qs in range(Q):
    [l, i] = map(int, input().split())
    print(lines[l][i-1])
