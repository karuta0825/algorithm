import heapq

Q = int(input())

que = []
for _ in range(Q):

    i = input().split()

    if i[0] == '1':
        heapq.heappush(que, int(i[1]))

    if i[0] == '2':
        print(que[0])

    if i[0] == '3':
        heapq.heappop(que)
