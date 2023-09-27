from collections import deque
Q = int(input())

q = deque()
for _ in range(Q):

    i = input().split()

    if i[0] == '1':        
        q.append(i[1])

    if i[0] == '2':
        print(q[0])

    if i[0] == '3':
        q.pop(0)
