N, Q = map(int, input().split())

# Asにしなくてよい。なぜならA[0]でA[i]が表現できる
# As = list(map(int, input().split()))

# LRs = [list(map(int, input().split())) for _ in range(Q)]

# なるほど時間かかるのか!
# どうやって減らすのか？
# memo化でしょうな、しかしいい勉強になるな

# どうやってはじめにそれに気がつけばよいのか？


# for lr in LRs:
#     print(sum(As[lr[0]-1:lr[1]]))


A = list(map(int, input().split()))

accum = [0] * N
accum[0] = A[0]

for i in range(1,N):
    accum[i] = accum[i-1] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    # 入出力でindexを考慮して、それ以外は0indexでかんがえる
    L -= 1
    R -= 1
    ans = accum[R] - (accum[L-1] if L > 0 else 0)
    print(ans)
