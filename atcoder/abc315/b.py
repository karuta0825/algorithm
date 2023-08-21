M = int(input())
D = list(map(int, input().split()))

m = (sum(D) + 1) // 2



s = 0
ans = 0

# この場合ぬけてるかーー
# もっと賢いやり方ありそうだけど、
ansd = 0

if len(D) == 1:
    print(1, m)
    exit(0)

for (i, d) in enumerate(D):

    s += d

    if s >= m:
        ans = i + 1
        # print([s, s-d, m])

        ansd = m - (s - d)
        break


print(ans, ansd)
