N, X = map(int,input().split())

alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = ""
for c in alp:
    str += c * N

print(str[X-1])



