# sizをどうやって求めるのか
# 2 ^ k >= Nとなるkの最小値をどうやって求めるのかということになる。
# 数学的にはlog2Nの切り上げた数になるね
# 再帰関数で求められそうだけどね

class Segtree:
    # ここも見事って感じなんだよな。
    # そうなるんだろうけど、ぱっとはでない
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (self.size * 2)

    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return -1000000000000000

        if l <= a and b <= r:
            return self.dat[u]

        m = (a + b) // 2
        ansl = self.query(l, r, a, m, u * 2)
        ansr = self.query(l, r, m, b, u * 2 + 1)
        return max(ansl, ansr)


N, Q = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(Q)]

Z = Segtree(N)
for q in qs:
    tp, *cont = q
    if tp == 1:
        pos, x  = cont
        Z.update(pos-1, x)

    if tp == 2:
        l, r = cont
        ans = Z.query(l-1, r-1, 0, Z.size, 1)
        print(ans)
