N, K = map(int, input().split())
A = list(map(int, input().split()))

a = sorted(set(A))

ans = 0
for v in a:
    if ans == v:
        ans += 1
    else:
        break


print(min(ans, K))
