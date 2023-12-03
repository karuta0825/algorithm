N, S, M, L = map(int, input().split())

# え、結構むずかしくない？
# DPつかうの？
# 6s + 8m + 12l >= Nとなる。最小値を求める作業なのか。

# 全通り確かめるか？
# 計算量を考えたらそれでいいことがわかる。
# N <= 100なので3重ループでも 10 ** 6なので時間に間にあう。

ans = 10 ** 10

for s in range(N+1):
    for m in range(N+1):
        for l in range(N+1):

            if 6*s + 8*m + 12*l < N:
                continue

            ans = min(ans, s*S + m*M + l*L)

print(ans)
