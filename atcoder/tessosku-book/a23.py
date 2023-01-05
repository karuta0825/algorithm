N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

# dpのときは、選択するかしないかでどうなればよい？
# 組み合わせが多すぎるんだよな。

# i番目までのチケットを使ってつくれるjに必要なチケット枚数
# dp[i][j]

# 遷移式はなにか？
# dp[i][j] = min(dp[i-1][j], dp[i][j-i] + 1)
# [j-i]というのは二進数的な意味である。111 - 100 => 011を意味してる。
# この操作は、積をしてそれを反転させたものになる。
# いやj-iではなくて、andでとったものが自身になる場合は含まれてるのでよいのだ

# 2進数の計算方法をしろうね。
INF = 10 ** 10
dp = [[INF] * (1 << N) for _ in range(M+1)]
dp[0][0] = 0

for i in range(1, M+1):
    for j in range(1 << N):
        a = A[i-1]
        bit = int("0b{}".format("".join(map(str,a))), 0)

        # 配る形式のDPということを理解することが大事ですね
        # dp[i-1][j] の状態からは次の2ステップがある。
        # 1. i番目を使用しない。i-1からiになるが未使用のためは変動しないため、dp[i][j]
        # 2. i番目を使用する。  更新後のjは、j | bitになるため、dp[i][j | bit]

        # 1.を表現すると、前の枚数であるdp[i-1][j]とすでに入ってる値の最小値を
        dp[i][j] = min(dp[i][j], dp[i-1][j])

        # 2.を表現すると、前の状態であるdp[i-1][j]に+1したものと、すでに入ってる値である(dp[i][j | bit])の最小値を取る
        dp[i][j | bit] = min(dp[i][j | bit], dp[i-1][j] + 1)


ans = dp[M][(1 << N) - 1]
if (ans >= INF):
    print(-1)
else:
    print(ans)
