x, y, n = map(int,input().split())

y_n = 3

if (x * y_n < y):
    print(x * n)
    exit()

syo = n // y_n

zan = n - (syo * y_n)

result = (zan * x) + (syo * y)

print(result)
