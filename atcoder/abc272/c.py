N = int(input())
A = list(map(int, input().split()))

# 以下の場合よき
# 偶数同士
# 奇数同士

# すべて偶数・奇数一つずつしかないならばアウト
# Nが2で偶数・奇数ならばアウト
# Nが3以上のときはパターンを考えないといけない

# どうやって全パターンをみるのか？
# 全探索だとN(N-1) = N ^ 2となり、今回アウト
# 始めの3つをみればわかる？

if (N == 2):
    if (sum(A) % 2 == 1):
        print(-1)
    else:
        print(sum(A))

    exit()

# これらでやればよいのでは？
# k k k
# k k g
# k g k
# g k k
# g g k
# g k g
# k g g
# g g g

A = sorted(A, reverse=True)
g = []
k = []
for a in A:
    if a % 2 == 0:
        g.append(a)
    else:
        k.append(a)

ans = max(sum(g[0:2]), sum(k[0:2]))

print(ans)
