N = int(input())


#頂点xの根（親）を見つける関数：戻り値は根（親）の頂点番号
def find(x):
    #print(x, root)
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

#頂点xと頂点yが同じ根（親）を持つかを判定する関数：戻り値はBoolean（True or False）
def same(x,y):
    return find(x) == find(y)

#頂点xと頂点yが所属するグループを併合する関数
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    #浅い（木の高さとして低い）方を深い（高い）方に合併
    if rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

g = {}

n = 0

pair = []

for _ in range(N):
    s, t = input().split()

    if not s in g:
        n += 1
        g[s] = n

    if not t in g:
        n += 1
        g[t] = n

    pair.append((g[s], g[t]))


#各頂点（要素）の根（親）を管理する配列：初期値は各頂点自身, 頂点数は上述の N
root = [i for i in range(len(g)+1)]

#各頂点（要素）の高さを管理する配列：初期値は最下位の0
rank = [0]*(len(g)+1)


for (s,t) in pair:

    if not same(s,t):
        unite(s,t)
    else:
        print("No")
        exit()

print("Yes")
