N, M, B = map(int, input().split())
A = sum(map(lambda x: int(x) * M, input().split()))
C = sum(map(lambda x: int(x) * N, input().split()))



print(A + C + (B * N * M))
