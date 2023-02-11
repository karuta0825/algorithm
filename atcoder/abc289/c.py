import itertools
N, M = map(int, input().split())

A = []
Goal = set(range(1, N+1))

for _ in range(M):
    c = int(input())
    a = list(map(int, input().split()))
    A.append(a)

# mC1 , mC2, ... mCmまでの組み合わせできた集合がGoalの集合と同じものかどうか
# combinationを使い方が知りたい。

ans = 0
for i in range(M):
    i += 1
    coms = list(itertools.combinations(A, i));

    for c in coms:
        cc = []
        for j in c:
            cc = cc + j

        if (set(cc) == Goal):
            ans += 1

print(ans)
