# import random

# for i in range(40):
#     print(",".join(map(str, [random.randint(1, 40) for i in range(40)])))

n, m = map(int, input().split())
festivals = [list(map(int, input().split()))[1:] for _ in range(m)]

# 問題の考え方が違う。
# 組み合わせが大切なんだ。全組み合わせがあるかどうかってことね。
# これはかんがえよ

def bitAndByStr(a, b):
    length = len(a)
    result = int("0b{}".format(a), 0) & int("0b{}".format(b), 0)
    return format(result,'b').zfill(length) == a

def bitor(a, b):
    length = len(a)
    result = int("0b{}".format(a), 0) | int("0b{}".format(b), 0)
    return format(result,'b').zfill(length);

conbination = {};
obj = []

# print("start")
# for i in range(1 << n):
#     s = format(i, 'b').zfill(n)

#     a = 0
#     print(s)
#     for c in s:
#         if (c == '1'):
#             a += 1

#     if (a == 2):
#         conbination[s] = 0

def generateStr(s, i):
    "sのi番目に1する"
    ss = list(s)
    ss[-1 * i] = "1"    
    return "".join(ss)


for i in range(n):
    a = "".zfill(n)
    a = generateStr(a, i + 1)
    for j in range(n):
        if (i < j):
            b = generateStr(a, j + 1)
            conbination[b] = 0

        # obj[s] = 0
# print(conbination)

def generateBinray(n, ary):
    result = "".zfill(n);
    cnt = 0
    for v in ary:
        result = generateStr(result, v)
        cnt += 1
    return [cnt, result]

result = False    
# for p in conbination:
#     for f in festivals:
#         member = generateBinray(n, f)
#         print(p, member, p == bitAndByStr(p, member))
#         if (p == bitAndByStr(p, member)):
#             if (p in obj):
#                 obj.pop(p)
#                 if (len(obj) == 0):
#                     result = True    
#                 break

#     if (len(obj) == 0):
#         result = True
#         break        

# すべてのor条件でいいんじゃないか？
# ちがう。それではひとりが参加したかどうかになってしまう。
# むずかしいな。進んでる感じがしないので辛い。答えを見てしまうのがいいんだけど粘りたい何かがある
# 好きなんですなってわかる。
# acm = "".zfill(n);
for f in festivals:

    [cnt, member] = generateBinray(n, f);    

    # acm = bitor(member, acm)
    # print(acm)    

    # if (all(map(int, list(acm)))):
    #     result = True
    #     break
    
    # print(conbination)                
    # for k in conbination:
    #     print(k, member, bitAndByStr(k, member))
    #     if (bitAndByStr(k, member)):
    #         obj.append(k)
    #         if (len(obj) == cnt):
    #             break
    # print(f)
    oks = list(filter(lambda x: bitAndByStr(x, member), conbination))

    # print(oks)
    for k in oks:
        if (k in conbination):
            conbination.pop(k)

    obj = []

    # print(conbination)
    if (len(conbination) == 0):
        result = True
        break
    
if (result):
    print("Yes")
else:
    print("No")

