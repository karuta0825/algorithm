num, point = map(int, input().split())
num_len = len(str(num))

# 桁を抽出する方法は？
# 321
# 文字列にしてループするのがよいね
# for c in reversed(str(321)):
#     print(c)

# 各桁に対してある操作をかんがえる
# それを一つずつ集計していって最後にマージすれば良い。
#

# 三項演算子の使い方知りたいな
def hantei(v, prev):
    if (v + prev > 4):
        return True
    else:
        return False
    
str_num = str(num)
temp = []
results = []

if (point > num_len):
    print(0)
    exit(0)

for i in range(num_len):
    
    digit = str_num[(-1 * (i + 1))]
    if i <= point - 1:    
        prev = 0 if len(temp) == 0 else temp.pop()

        if (hantei(int(digit), prev)):
            temp.append(1)
            
        results.append(0)            
    else:
        v = 0 if len(temp) == 0 else temp.pop();
        d = int(digit) + v
        if (d == 10):
            temp.append(1)
            results.append(0);
        else:                
            results.append(int(digit) + v);

if (len(temp) == 0 and sum(results) == 0):
    print(0)
    exit(0)

print("".join(map(str, [*results, *temp][::-1])))         

# いかのケースが問題っぽいな
# 314159265358979 15
# 000000000000000

# このケースがおかしい
# 14159265358979 2
# 14159265359009
# 141592653581000 こっちが出力されてしまう
