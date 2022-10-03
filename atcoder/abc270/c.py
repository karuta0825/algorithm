N, X, Y = map(int, input().split())
inputs = [list(map(int, input().split())) for i in range(N-1)]

# 親をキーにするデータ構造
# pmap = {
#     1: [2,3],
#     3: [4,5]
# }

# 子をキーにするデータ構造
# こっちを使えば探索ははやくなるな！
# cmap = {
#     2: 1,
#     3: 1,
#     4: 3,
#     5: 3
# }
cmap = {}
for [c, p] in inputs:
    cmap[p] = c

def c2p(breads, key):
    if (not (key in cmap)):
        breads.append(key)
        return breads    
    elif (key < cmap[key]):
        breads.append(key)        
        return breads;
    else:
        breads.append(key)
        nextv = cmap[key]
        return c2p(breads, nextv)
    

xroute = c2p([], X)
yroute = c2p([], Y)

# ２つの配列の共通要素を見つけるものはないか？集合であるよな
# print(set(xroute).intersection(yroute))
intersectionPoint = sorted(set(xroute).intersection(yroute), reverse=True)[0]
# print(intersectionPoint);

xx = []
for i in xroute:
    if ( i != intersectionPoint ):
        xx.append(i)
    else:
        xx.append(i);
        break;

yy = []
for i in yroute:
    if ( i != intersectionPoint ):
        yy.append(i)
    else:
        break;

yy.reverse()
xx.extend(yy);

print(" ".join(map(str,xx)))
