N, K = map(int, input().split())
A = list(map(int, input().split()))

# t秒後に何枚印刷されてるだろうか？
# S = A1 // t + A2 // t + ... An // t
# このSが求める枚数より、大きい場合小さい場合でtの値を変更していければよい
# どうやって更新しようかな？ 2倍あるいは1/2倍でよいのではないか？
# 逆関数をつくるのに、二部探索が使えるってことね。

def search(left, right, X):
    # 1のときというのは、隣の整数値ということになるので、それでゴール
    # 左右の間隔をどんどん減らしていく発想
    # 間隔がどのくらいになったときにストップするのかを決めておく
    if (right - left == 1):
        return right

    mid = (right + left) // 2
    result = 0
    for a in A:
        result += mid // a

    print([left, right, mid], result , X)
    if (result < X):
        return search(mid, right, X)
    else:
        return search(left, mid, X)
L = 0
R = 10 ** 10

print(search(L, R, K))
