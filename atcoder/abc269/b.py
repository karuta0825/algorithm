ss = [input() for _ in range(10)]
 
INF = 1000000000000
a = INF
b = 0
c = INF
d = 0
x = []
y = []
 
 
for i in range(len(ss)):
    s = ss[i]
    for j in range(len(s)):
        if (s[j] == "#"):
            x.append(i)
            y.append(j)
            if (a > i):
                a = i
 
            if (b < i):
                b = i
 
            if (c > j):
                c = j
 
            if (d < j):
                d = j
                
print(a + 1, b + 1)
print(c + 1, d + 1)
# print(min(x) + 1, max(x) + 1)
# print(min(y) + 1, max(y) + 1)
