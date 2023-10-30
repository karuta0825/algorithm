from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A = sorted(A)

for _ in range(Q):

    X = int(input())

    pos = bisect_left(A, X)

    print(pos)
