n, m = map(int, input().split())
festivals = [list(map(int, input().split()))[1:] for _ in range(m)]

# 問題の考え方が違う。
# 組み合わせが大切なんだ。全組み合わせがあるかどうかってことね。
# これはかんがえよ

def bitAndByStr(a, b):
    length = len(a)
    result = int("0b{}".format(a), 0) & int("0b{}".format(b), 0)
    return format(result,'b').zfill(length)

conbination = {};
obj = {}
for i in range(1 << n):
    s = format(i, 'b').zfill(n)

    a = 0
    for idx, c in enumerate(s):
        if (c == '1'):
            a += 1

    if (a == 2):
        conbination[s] = 0
        obj[s] = 0


def generateStr(s, i):
    "sのi番目に1する"
    ss = list(s)
    ss.reverse()
    ss[i-1] = "1"
    ss.reverse()
    return "".join(ss)

def generateBinray(n, ary):
    result = "".zfill(n);
    for v in ary:
        result = generateStr(result, v)
    return result

result = False
# for p in conbination:
#     for f in festivals:
#         member = generateBinray(n, f)
#         # print(p, member, p == bitAndByStr(p, member))
#         if (p == bitAndByStr(p, member)):
#             if (p in obj):
#                 obj.pop(p)
#                 continue

#     if (len(obj) == 0):
#         result = True
#         break        

for f in festivals:

    member = generateBinray(n, f);

    for k in conbination:
        print(k, member, k == bitAndByStr(k, member))
        if (k == bitAndByStr(k, member)):
            if (k in obj):                
                obj.pop(k)

    # print(conbination)
    if (len(obj) == 0):
        result = True
        break
    
if (result):
    print("Yes")
else:
    print("No")

