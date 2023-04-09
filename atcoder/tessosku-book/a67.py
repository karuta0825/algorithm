class Unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n+1)
        self.size = [1] * (n+1)


    def find(self, x):

        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):

        ru = self.find(u)
        rv = self.find(v)

        if (ru != rv):
            if self.size[ru] > self.size[rv]:
                self.par[rv] = ru
                self.size[ru] += self.size[rv]
            else:
                self.par[ru] = rv
                self.size[rv] += self.size[ru]

    def same(self, u, v):
        return self.find(u) == self.find(v)


N, M = map(int, input().split())

uf = Unionfind(N)
ans = 0

# part1
# g = {}
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     path = "{}-{}".format(a,b) if a < b else "{}-{}".format(b,a)
#     g[path] = c

# for path, cost in sorted(g.items(), key=lambda x:x[1]):
#     a, b = map(int, path.split('-'))
#     if not uf.same(a,b):
#         uf.unite(a,b)
#         ans += cost

# part2
t = []
for _ in range(M):
    a, b, c = map(int, input().split())
    t.append((c, a, b))

t.sort()
for c, a, b in t:
    if not uf.same(a,b):
        uf.unite(a,b)
        ans += c

        
print(ans)
