from collections import defaultdict

dic = defaultdict(int)

Q = int(input())

for _ in range(Q):
    i = input().split()


    if i[0] == '1':
        dic[i[1]] = int(i[2])

    if i[0] == '2':
        print(dic[i[1]])
