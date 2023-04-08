class UnionFind:

    def __init__(self,n):
        self.n = n
        # 親の値を格納する
        self.par = [-1] * (n+1)
        # グループの数を格納する
        self.size = [1] * (n+1)

    def find(self, x):
        # 再帰を使わずに変更しまくってる
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)

        if rootu != rootv:

            if self.size[rootu] > self.size[rootv]:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
            else:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]

    def same(self, u, v):
        return self.find(u) == self.find(v)


N, Q = map(int, input().split())

nf = UnionFind(N)


for _ in range(Q):
    n, u, v = map(int, input().split())

    if (n == 1):
        nf.unite(u,v)

    if (n == 2):
        if (nf.same(u, v)):
            print("Yes")
        else:
            print("No")
