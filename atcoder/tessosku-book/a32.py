# これはむずかしいな

# 8 2 3

# 少なくとも2つは取り除かないといけない。

# 8個目の石をとれるようにするにはどうしたらよいか？
# 2 or 3の選択がとれるので、
# 最後から1手前のとき5, 6個取り除かれていたら先手が価値
# 5,6になってるときは、


# やっぱりdpかという感はあたってる。
# dp[i]をどう定義するのかということと、i-1の状態を合わせてがえる

N, A, B = map(int, input().split())

# dp[i]: 残りi個のときに先手が勝つかどうか
dp = [False] * (N+1)

# 配る法のDPをしないといけない？
# これどうやって実装するんだっけ？qh

# Aより持ち手がすくないと先手は出せないのでまける
for i in range(A):
    dp[i] = False

for i in range(A, N+1):
    # デフォルト
    dp[i] = False

    # この条件分岐をもっと簡略することができないだろうか?
    # if i-A >= 0:
    #     dp[i] = not dp[i-A]

    # if i-B >= 0:
    #     dp[i] = not dp[i-B]

    # if (i-A >= 0 and i-B >= 0):
    #     dp[i] = not dp[i-B] or not dp[i-A]

    for j in [A, B]:
        nxt = i - j
        if nxt < 0: continue
        if not dp[nxt]:
            # このとき勝つって考えをとればよいのか!
            dp[i] = True


if dp[N]:
    print("First")
else:
    print("Second")
