# これは全探索でいけるレベルのもの
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0


for s in S:
    last3 = s[::-1][0:3][::-1]
    for t in T:
        if last3 == t:
            ans += 1
            break


print(ans)
