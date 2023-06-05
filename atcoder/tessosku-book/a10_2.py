N = int(input())
A = list(map(int, input().split()))
D = int(input())

LM = [0] * (N+2)
RM = [0] * (N+2)

for i in range(N):
    LM[i+1] = max(A[i], LM[i])

for i in range(N, 0, -1):
    RM[i] = max(A[i-1], RM[i+1])
    
for i in range(D):
    L, R = map(int, input().split())
    print(max(LM[L-1], RM[R+1]))
