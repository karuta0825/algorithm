# 対角線上にあるかどうかの判定とかが必要になるのか？
# 正方形であることをどうやって判定するのかがポイントですな
# 4つの点を撮ってきて、それで正方形が作れるかどうかを判定するプログラムを考える

# たしかに難しいけど、これはアルゴリズムを考えるb一番楽しいところだな。
import itertools

lines = [input() for _ in range(9)]

plots = []

for l in range(len(lines)):
    for m in range(len(lines[l])):
        if (lines[l][m] == "#"):
            plots.append((l,m))

# この件数がおおくてできないケースだな
# pythonの限界か？
coms = list(itertools.combinations(plots, 4))

def distance(a, b):
    [a1, a2] = a
    [b1, b2] = b

    return ((a2 - b2) ** 2) + ((a1 - b1) ** 2)

def diffVector(a, b):
    return (a[0] - b[0], a[1] - b[1])

def kyori(a):
    return a[0] ** 2 + a[1] ** 2

def product(a, b):
    return a[0] * b[0] + a[1] * b[1]

def add(a,b):
    return (a[0] + b[0], a[1] + b[1])

cnt = 0
for cs in coms:

    [o, a, b, c] = cs

    oa = diffVector(a, o)
    ob = diffVector(b, o)
    oc = diffVector(c, o)

    ab = product(oa, ob)
    ac = product(oa, oc)

    if (ab == 0 and not ac == 0):
        if (oc == add(oa, ob) and kyori(oa) == kyori(ob)):
            cnt += 1

    elif (ac == 0 and not ab == 0):
        if (ob == add(oa, oc) and kyori(oa) == kyori(oc)):
            cnt += 1

    else:
        continue


print(cnt)
# ary = [(4,8),(5,6),(7,7),(6,9)]
# list(map(lambda x: distance(ary[0], x), ary[1:]))

# a = np.array(ary[0])
# b = np.array(ary[1])
# np.linalg.norm(b-a)
# distance(ary[0], ary[1])
# for i in range(9):
#     print("#########")
