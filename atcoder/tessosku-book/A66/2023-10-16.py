class UnionFind:
    def __init__(self, n):
        self.par = [-1] * (n+1)
        self.r = [-1] * (n+1)

    def find(self, x):
        while self.par[x] != -1:
            x = self.par[x]

        return x

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.r[px] > self.r[py]:
            # swap, python is beautiful
            px, py = py, px

        if self.r[px] == self.r[py]:
            self.r[py] += 1

        self.par[px] = py

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, Q = map(int, input().split())

uf = UnionFind(N)


for _ in range(Q):
    q, a, b = map(int, input().split())

    if (q == 1):
        uf.unite(a,b)

    if (q == 2):
        print("Yes" if uf.same(a, b) else "No")
