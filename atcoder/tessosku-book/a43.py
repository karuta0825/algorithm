N, L = map(int, input().split())
ans = 0
for _ in range(N):
    A, B = map(lambda x:x, input().split())
    A = int(A)

    if (B == 'E'):
        ans = max(ans, L - A)
    else:
        ans = max(ans, A)

print(ans)
