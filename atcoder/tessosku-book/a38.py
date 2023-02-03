# サンプル問題をとくことはできたけど、どうやって抽象化しようかな？

# 5 3
# 1 2 22
# 2 3 16
# 3 5 23

# (+ 22 16 16 23 23)
# minの方を取得すればいいんじゃないか？
D, N = map(int, input().split())

INF = 24
ary = [0, *([INF] * (D))]

for _ in range(N):
    L, R, H = map(int, input().split())

    for i in range(L, R+1):
        ary[i] = min(ary[i], H)

print(sum(ary))
