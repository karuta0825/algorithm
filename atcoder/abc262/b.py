
N, M = map(int, input().split())
values = [list(map(int, input().split())) for i in range(M)]

# Nから3つの組み合わせを取得する
for i in 1 << N:
    print(format(i, 'b'))


result = []
for i in range(1 << 5):
    str = format(i, 'b')
    if (len(list(filter(lambda v: v == '1', str))) == 3):
        r = []
        z = str.zfill(5)
        print(z)
        for j in range(len(z)):
            print(z[j])
            if (z[j] == '1'):
                r.append(j + 1)
        result.append(r)

# これでいいのかん？
def check(ary):
    return false;
        
for l in result:
    
    
