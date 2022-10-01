# これは全探索だな。下図が少ないから組み合わせすべて洗い出せばよい
a, b = map(int, input().split())

cobination = {
    0: [0,0,0],
    1: [1,0,0],
    2: [0,1,0],
    3: [1,1,0],
    4: [0,0,1],
    5: [1,0,1],
    6: [0,1,1],
    7: [1,1,1]
}

# 取得した２つの配列でどちらも0でないものを足し合わせたらよいね
taka = cobination[a]
aoki = cobination[b]

ha = []
for [x, y] in list(zip(taka, aoki)):
    if (x == 1 or y == 1):
       ha.append(1);
    else:
        ha.append(0);

sum = 0
for [i, v] in list(map(lambda v: v, enumerate([1,2,4]))):
    sum += ha[i] * v

print(sum)    
