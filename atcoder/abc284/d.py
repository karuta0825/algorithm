import math
T = int(input())


def searchPQ(n):
    i = 2
    p = 0
    q = 0
    while i ** 3 <= n:

        if (n % i == 0):

            if ((n / i) % i == 0):
                p = i
                q = n // i ** 2
            else:
                q = i
                p = int(math.sqrt(n//i))
                
            break
        i += 1

    return [p, q]

# なぜqが1通りに決まるのか？
# それは素数だからである。そういうことだな。
# あぁなるほど。素数をそういう意味に使うのか！
# これは悔しいな。素数かどうかの判定ではなくて割り切れないという特徴なんだ。
# def searchPQ2(n):

#     for i in range(2, int(n ** 1/3)):

#         if (not (n % i == 0)):
#             continue

#         if ((n / i) % i == 0):
#             p = i
#             q = int(n / i / i)
#         else:
#             q = i
#             p = int(math.sqrt(n/i))

#         break

#     return [p, q]



for _ in range(T):

    N = int(input())
    print(*searchPQ(N))
