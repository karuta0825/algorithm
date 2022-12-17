N, M = map(int, input().split())

obj = {}
for n in range(N):
    s = input()
    obj[n] = s


# ビット演算を使いたい

result = 0
for i in range(N):
    for j in range(N):
        if (j <= i):
            continue
        
        a = obj[i]
        b = obj[j]
        length = len(a)
        accum = 0
        for k in range(len(a)):
            if (a[k] == 'o' or b[k] == 'o'):
                accum += 1

        if (accum == length):
            result += 1

print(result)
