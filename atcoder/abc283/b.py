N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    ans = 0
    inputs = list(map(int, input().split()))
    if (inputs[0] == 1):
        A[inputs[1]-1] = inputs[2]
    else:
        ans = A[inputs[1]-1]
        A[inputs[1]-1] = ans
        print(A[inputs[1]-1])
