N, L = map(int, input().split())

ans = 0

for i in range(N):

    A, B = input().split()

    if B == 'E':
        ans = max(ans, L - int(A))
    else:
        ans = max(ans, int(A))

print(ans)
