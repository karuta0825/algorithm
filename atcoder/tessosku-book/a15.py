# なるほど順位をつけろってことだな。
# ソートしてそれぞれのhashmapで順位がつけられるといいんだけどね
# 二分探索って考えもあってた。それをライブラリをつかって解くというかんじですね。
# 二分探索を自分でつくってみて徳と言うんはあり。

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

unique = sorted(list(set(A)))

# bisect_leftは
# python配列のコピーはどうやってつくる
B = A[:]
for i in range(N):
    B[i] = bisect_left(unique, A[i]) + 1


print(*B)
