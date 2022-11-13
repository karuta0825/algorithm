n = int(input())
ss = [input() for _ in range(n)]

def p1(str):
    c = str[0]
    return c in ["H", "D", "C", "S"]

def p2(str):
    c = str[1]
    return c in ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]

tmp = []
def p3(s):
    if (s in tmp):
        return False
    else:
        tmp.append(s)
        return True

result = True
for s in ss:
    a = p1(s)
    b = p2(s)
    c = p3(s)
    # print(a,b,c)
    if (not a or not b or not c):
        result = False
        break

if (result):
    print("Yes")
else:
    print("No")
