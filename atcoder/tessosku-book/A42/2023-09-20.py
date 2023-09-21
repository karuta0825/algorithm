N, K = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(N)]


def cnt(i,j):
    r = 0

    for a, b in A:

        if i <= a <= i + K and j <= b <= j + K:
            r += 1

    return r


ans = 0
for i in range(1, 100-K+1):
    for j in range(100-K+1):
        ans = max(ans, cnt(i,j))

print(ans)
