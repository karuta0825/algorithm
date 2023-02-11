# いや想定と違うな。
# どうやってかぶらないようにするかって話だ
# つながってる必要はないんだ。
N = int(input())

# ならび変えたほうがよさそうね
# 並び替えてもむずかしい、長さとゴールをどう考えればよいのか？

# 二部探索でみつけたらいいのか。
# スタート地点で並び替えをする。若い準にゴールをとっては、そいつの次となるスタート地点を二部探索でみつける
# これを繰り返すことで最大値となるものをみつける
# 並び替えるのにNlogNとなり、それに二分探索の計算量をかけたものがよいのでは？


films = [
    list(map(int, input().split()))
    for _ in range(N)
]

films.sort(key=lambda x:x[1])

ans = 0
now = 0

for l, r in films:
    if (l < now):
        continue

    now = r
    ans += 1


print(ans)
