Q = int(input())

stack = []

for _ in range(Q):
    query = input().split()

    if (int(query[0]) == 1):
        stack.append(query[1])

    if (int(query[0]) == 2):
        title  = stack[-1]
        print(title)

    if (int(query[0]) == 3):
        stack.pop()
