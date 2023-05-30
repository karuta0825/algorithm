S = [input() for _ in range(8)]

row = ["a", "b", "c", "d","e", "f", "g", 'h']
col = list(range(8,0,-1))

g = ''
for i, x in enumerate(S):
    for j, y in enumerate(x):
        if (y == "*"):
            g = (i,j)

x, y = g
print("{}{}".format(row[y],col[x]))
