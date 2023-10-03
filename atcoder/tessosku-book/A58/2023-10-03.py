class SegmentTree:
    def __init__(self, n):
        self.size = 1

        while self.size < n:
            self.size *= 2

        self.data = [0] * (self.size * 2)

    def update(self, pos, val):
        pos = self.size + pos
        self.data[pos] = val
        while pos >= 2:
            pos //= 2
            self.data[pos] = max(self.data[pos*2], self.data[(pos * 2)+1])

    # ここが一番むずかしいな。
    def query(self, l, r, a, b, u):

        if r <= a or b <= l:
            return -100000000000000

        if l <= a and b <= r:
            return self.data[u]

        m = (a + b) // 2
        ansl = self.query(l, r, a, m, u * 2)
        ansr = self.query(l, r, m, b, u * 2 + 1)
        return max(ansl, ansr)

N, Q = map(int, input().split())


seg = SegmentTree(N)

for i in range(Q):

    q, x, y = map(int, input().split())

    if q == 1:
        seg.update(x-1,y)

    if q == 2:
        # 引数のあ使い方がわからに
        print(seg.query(x-1, y-1, 0, seg.size, 1))
