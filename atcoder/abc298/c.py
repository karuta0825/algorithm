from collections import defaultdict
N = int(input())
Q = int(input())

boxes = [[] for _ in range(N+1)]
cards = defaultdict(set)

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        i = q[1]
        j = q[2]
        boxes[j].append(i)
        cards[i].add(j)

    if q[0] == 2:
        i = q[1]
        print(*sorted(boxes[i]))

    if q[0] == 3:
        i = q[1]
        print(*list(sorted(cards[i])))
    
