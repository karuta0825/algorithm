N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for b in B:
    b -= 1
    ans += A[b]

print(ans)
