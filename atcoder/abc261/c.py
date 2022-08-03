num = int(input())

strings = [
    input() for i in range(num)
]

result = []
stringMap = {}

for i in range(num):

    str = strings[i]
    if str in stringMap:
        stringMap[str] += 1
    else:
        stringMap[str] = 0
            
    result.append({"value": str, "count": stringMap[str]})            
    

# for i in result:
#     if i["count"] == 0:
#         print("{}".format(i["value"]))
#     else:
#         print("{}({})".format(i["value"], i["count"]))


# もしmapを使うならば次のように書く必要がある
def cprint(v):
    r = "{}".format(v["value"]) if v["count"] == 0 else "{}({})".format(v["value"], v["count"])
    print(r)


list(map(cprint, result))



