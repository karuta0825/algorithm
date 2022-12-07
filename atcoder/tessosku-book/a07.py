D = int(input())
N = int(input())

ary = [0] * D

for lr in [list(map(int, input().split())) for _ in range(N)]:
    L = lr[0] - 1
    R = lr[1] - 1
    for i in range(L, R+1):
        ary[i] += 1

print(*ary, sep='\n')
