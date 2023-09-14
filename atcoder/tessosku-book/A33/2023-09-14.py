N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1,N):
    ans = (ans ^ A[i])

if ans:
    print("First")
else:
    print("Second")
