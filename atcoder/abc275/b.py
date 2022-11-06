a, b, c,d,e,f = map(int, input().split())

diff = (a * b * c) - (d * e * f)
s = 998244353

print( diff % s)


