from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

# i番目までの配列
# dp[i] = []
# 前の状態をもたないと使いできるかどうか判定できないね
# {cnt: 0, value: 0} みたいな状態でもとうかな？

# 遷移式
# dp[i] = max(len([*dp[i-1], i]), len(dp[i-1]))

# この問題の難しさは、一つ前からの追加が必ず良い選択かどうかわからないことであるな。
# i番目を追加するかi+1番目を追加したほうがいいのかがわからないってことなんだろうね。
# そういう意味で配る形式でやってみてもよいかもしれないな

# dp[i] dp[i+1]

# dp = [{"cnt": 0, "value": 0} for _ in range(N+1)]

# for i in range(1, N+1):
#     a = A[i-1]

#     dp[i] = dp[i-1]
#     if (dp[i-1]["value"] < a):
#         dp[i] = {"cnt": dp[i-1]["cnt"] + 1, "value": a}


# print(dp)

# 最後の要素がi番目のときの長さをdp[i]として表現する
# dp[i] = dp[i-1] + 1

INF = 10 ** 10

# dp[i]はi番目の要素を選択したときの長さ
dp = [INF] * (N)

# L[i] は長さiのときの最小値
L = [INF] * (N)
LEN = 0

for i in range(N):
    a = A[i]
    ind = bisect_left(L, a)

    # Lのindは、求めたい長さそのものである
    # L[i]は長さiのときの最小値というものだから
    dp[i] = ind + 1

    L[ind] = a

    if (dp[i] > LEN):
        LEN += 1

# print(dp)
# print(L)
print(max(dp))
