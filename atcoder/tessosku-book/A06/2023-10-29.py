N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
tmp = 0

for i in A:
    tmp += i
    S.append(tmp)

for _ in range(Q):

    L, R = map(int,input().split())

    SR = S[R]
    SL = S[L-1]

    print(SR-SL)
