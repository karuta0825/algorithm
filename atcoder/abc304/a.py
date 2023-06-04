N = int(input())

p = []
m = 10 ** 9
a = 0

for i in range(N):

    name, age = input().split()
    age = int(age)

    p.append((name, age))

    if m > age:
        m = age
        a = i

for i in range(a, N):
    print(p[i][0])

for i in range(a):
    print(p[i][0])
