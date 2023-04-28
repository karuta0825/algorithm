from collections import defaultdict
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



# どうやって連結成分をグルーピングするのかということなんだよね
# これはできたな。以下のようにすることで実現可能
N, M = map(int, input().split())

uf = Unionfind(N)
d = defaultdict(set)
cnt = defaultdict(int)
pairs = []

for _ in range(M):
    u, v = map(int, input().split())
    pairs.append((u,v))
    uf.unite(u,v)

# 二部グラフ
for i in range(1, uf.n + 1):
    if uf.par[i] == -1:
        d[i].add(i)
    else:
        par = uf.par[i]
        d[par].add(i)

for (u,v) in pairs:
    cnt[uf.find(u)] += 1


ans = "Yes"
for k in d:
    if cnt[k] != len(d[k]):
        ans = "No"

print(ans)
