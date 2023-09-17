N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

sumA = sum(map(lambda x: M *x, A))
sumC = sum(map(lambda x: N *x, C))

sumB = (N * M) * B

print(sumA + sumB + sumC)
