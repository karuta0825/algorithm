n, x, y, z = map(int, input().split())
math = map(int, input().split())
english = map(int, input().split())

grades = list(zip(math, english))
gradeWithIndex = list(map(lambda v:v, enumerate(grades)))

sort_math = sorted(gradeWithIndex, key=lambda v: v[1][0], reverse=True)
math_path = sort_math[:x]
math_not_path = sorted(sort_math[x:], key=lambda v: v[0])

sort_english = sorted(math_not_path, key=lambda v: v[1][1], reverse=True)
english_path = sort_english[:y]
english_not_path = sorted(sort_english[y:], key=lambda v:v[0])

sort_sum_math_english = sorted(english_not_path, key=lambda v: sum(v[1]), reverse=True)
sum_path = sorted(sort_sum_math_english[:z], key=lambda v: v[0])

result = sorted(list(map(lambda v: v + 1, [
 * list(map(lambda x: x[0], math_path)), 
 * list(map(lambda x: x[0], english_path)),
 * list(map(lambda x: x[0], sum_path))
])))

for i in result:
    print(i)









a = [1, 2, 4, 5, 11]
w = 10
result = 'NG'

for i in range(1 << len(a)):
    mysum = []
    print("はじまるよ: 10: {} 2: {}".format(i, bin(i)))
    for j in range(len(a)):
        if (i & 1 << j):
            # 何桁目かわからないな
            print(a[j])
            mysum.append(a[j])

    if (sum(mysum) == w):
        print(mysum)
        result = "OK"
        break
        
print(result)











