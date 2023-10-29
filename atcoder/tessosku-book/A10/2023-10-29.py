N = int(input())
A = list(map(int,input().split()))

D = int(input())


ml = []
tmp = -1 * (10 ** 8)
for i in range(N):
    tmp = max(tmp, A[i])
    ml.append(tmp)


mr = []
tmp = -1 * (10 ** 8)
for i in range(N):
    tmp = max(tmp, A[N-i-1])
    mr.append(tmp)


for i in range(D):
    L, R = map(int, input().split())

    r = N - R - 1
    print(max(ml[L-2], mr[r]))
