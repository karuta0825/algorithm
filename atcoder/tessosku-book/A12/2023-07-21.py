# N, K = 4, 10
# list(map(lambda x: 6 // x, [1,2,3,4]))
# sum(map(lambda x: 5 // x, [1,2,3,4])) => 9
# sum(map(lambda x: 6 // x, [1,2,3,4])) => 12

# こういうことだよね。はじめて上がればよい。
# 終了条件をどうするかがポイント。間の計算はらくだよ
# G = 10としても10にならないことがあるからね。そのときどうすればよいのかといういこと
# k-1, kといれて、kで超えたときやればいいんじゃないのか？

import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
A = list(map(int, input().split()))

def s(t):
    return sum(map(lambda x: t // x, A))


def f(t1, t2):

    m = (t1 + t2) // 2
    k = s(m)
    k2 = s(m-1)

    if k2 < K <= k:
        return m

    if k < K:
        return f(m, t2)
    else:
        return f(t1, m)


print(f(0, 10 ** 8))
