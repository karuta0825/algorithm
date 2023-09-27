Q = int(input())

q = []
for _ in range(Q):

    i = input().split()

    if i[0] == '1':        
        q.append(i[1])

    if i[0] == '2':
        print(q[-1])

    if i[0] == '3':
        q.pop()
