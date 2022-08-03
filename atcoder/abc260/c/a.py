
str = input()

strMap = {}

for c in str:
    if c in strMap:
        # pythonでインクリメント
        strMap[c] += 1        
    else:
        strMap[c] = 1

# findすればよい.それをどうやってpythonで実現するのかが大事
target = next(filter(lambda item: item[1] == 1, strMap.items()), None)

# None対策をかんがえる。本当はもっとよいやり方がありそうだ
if target == None:
    print(-1)
else:
    print(target[0])

