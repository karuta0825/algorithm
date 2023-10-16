N, M = map(int, input().split())


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

uf = UnionFind(N)

l = []
for i in range(M):

    A, B ,C = map(int, input().split())

    l.append((C, [A,B]))


nl = sorted(l, key=lambda x: x[0])

ans = 0
for C, Ps in nl:

    a, b = Ps

    if not uf.same(a, b):
        uf.unite(a, b)
        ans += C
    
print(ans)
