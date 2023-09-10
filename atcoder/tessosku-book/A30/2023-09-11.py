n, r = map(int, input().split())

M = 1000000007

bunshi = 1
for i in range(1, n+1):
    bunshi = (bunshi * i) % M

bunbo = 1
for i in range(1, r+1):
    bunbo = (bunbo * i) % M

for i in range(1, n-r+1):
    bunbo = (bunbo * i) % M


def power(a, b, m):
    ans = 1
    p = a
    for i in range(30):
        if (b // (1 << i)) % 2 == 1:
            ans = (ans * p) % m

        p = (p * p) % m

    return ans

ans = (bunshi * power(bunbo, M-2, M)) % M
print(ans)
