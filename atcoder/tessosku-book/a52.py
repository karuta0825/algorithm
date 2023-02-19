Q = int(input())

queue = []

for _ in range(Q):
    query = input().split()

    if (int(query[0]) == 1):
        queue.append(query[1])

    if (int(query[0]) == 2):
        title  = queue[0]
        print(title)

    if (int(query[0]) == 3):
        queue.pop(0)
