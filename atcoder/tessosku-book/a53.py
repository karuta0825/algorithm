from heapq import heappop, heappush
Q = int(input())

heap = []

for _ in range(Q):
    query = input().split()

    if (int(query[0]) == 1):
        x = int(query[1])
        heappush(heap, x)

    if (int(query[0]) == 2):
        print(heap[0])

    if (int(query[0]) == 3):
        heappop(heap)
