D = int(input())
N = int(input())

visitors = [0] * (D+1)

for i in range(N):
    L, R = map(int, input().split())

    visitors[L] += 1

    if R+1 <= D:
        visitors[R+1] -= 1

tmp = 0
for i in range(1, D+1):
    tmp += visitors[i]
    print(tmp)
