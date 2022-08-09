N, M = list(map(int, input().split()))


N, M = [3,5]
ary = [i for i in range(1, M +1)]
for i in range(1, M+1):
    for j in range(1, M+1):
        if (i < j):
            print(i,j)
            
for i in range(1 << M):
    str = format(i, 'b').zfill(M)
    
    if (len(list(filter(lambda v: v == '1', str))) == 3):
         print(str);
         


for i in "00111":



