T = int(input())


def cnt(ary):

    c = 0
    for i in ary:
        if (i % 2 == 1):
            c += 1

    return c

for _ in range(T):
   N = int(input())
   A = list(map(int, input().split()))
   print(cnt(A))
