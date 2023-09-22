N, Q = map(int, input().split())

A = list(range(1, N+1))

R = 1

def index(i):
    if R == 1:
        return i-1

    return N-i

for _ in range(Q):

    q = input().split()

    if q[0] == '1':
        x, y = int(q[1]), int(q[2])
        A[index(x)] = y

    if q[0] == '2':
        R *= -1

    if q[0] == '3':
        i = int(q[1])
        print(A[index(i)])
