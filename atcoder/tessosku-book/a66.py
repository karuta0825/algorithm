import sys
sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())

class UnionFind:
    n = []

    def __init__(self, n):
        self.n = [-1] * (n+1)

    def find(self, x):
        if (self.n[x] == -1):
            return x
        self.n[x] = self.find(self.n[x])
        return self.n[x]
        
    def unite(self, x, y):

        x = self.find(x)
        y = self.find(y)

        if (x == y): return

        self.n[x] = y
            
        
nf = UnionFind(N)
            
for _ in range(Q):
    n, u, v = map(int, input().split())

    if (n == 1):
        nf.unite(u,v)

    if (n == 2):
        if nf.find(u) == nf.find(v):
            print("Yes")
        else:
            print("No")
     
