from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)
ans = 0

for i in A:

    if (dic[i] == 1):
        ans += 1
        dic[i] = 0
    else:
        dic[i] += 1


print(ans)
