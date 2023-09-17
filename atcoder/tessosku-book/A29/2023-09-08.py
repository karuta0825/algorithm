a, b = map(int, input().split())

syo = 1000000007


def power(a, b, m):

    ans = 1
    for i in range(30):
        if (b // (1 << i) % 2) == 1:
            ans = (ans * a) % m

        a = (a * a) % m

    return ans


print(power(a, b, syo))
