N, A, B = map(int, input().split())
s = input()
inits = s[:]

#
def a(s):
    l = s[0]
    return s[1:] + l


def diff(s, t):
    cnt = 0
    reverset = t[::-1]
    for i in range(len(s)):
        if (s[i] != reverset[i]):
            cnt += 1

    return cnt

def cost(s):
    length = len(s)
    mid = length // 2

    if (length % 2 == 1):
        left = s[0:mid]
        right = s[mid+1:]
    else:
        left = s[0:mid]
        right = s[mid:]

    return diff(left, right)

# まずN回やってみて一番コストがさがったときをさがす
# このやり方がまずいのは最小のがあるかもしれないことだよな。
# mincost = cost(s)
# num = 0
# for i in range(len(s)):
#     s = a(s)
#     newcost = cost(s)
#     if (newcost < mincost):
#         mincost = newcost
#         num = i + 1

# for _ in range(num):
#     s = a(s)

# print(min((num * A + cost(s) * B), cost(inits) * B))
# 全パターンから計算すればよいのか！よしといたぞ。
result = cost(inits) * B
length = len(s)
for i in range(length-1):

    s = a(s)
    ans = (i+1) * A + cost(s) * B
    result = min(ans, result)


print(result)
