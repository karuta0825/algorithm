# よしコンビネーションで経路総数を求める方法はわかった。
# 各経路の求め方がわからないな。1と0の組み合わせをもとめるってことであってるな。
# これ総当りで計算できるな！いや18桁あるとなるとむりである。
# 動的計画法か？それともあのーナントカ方法である。焼きなましみたいな。
# 難しいな!
# 動的計画法で行ける気がする
# 右方向に全部いく。
# その後全部したにいくようする。
# そのときに

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[0] * W  for _ in range(H)]
st = [[set()] * W  for _ in range(H)]
st[0][0] = {A[0][0]}

# print(st)
# あれわかっていないなー。これはつらいぞー
for i in range(H):
    for j in range(W):
        
        if i-1 >= 0:
            if not A[i][j] in st[i-1][j]:
                st[i][j] = {*st[i-1][j], A[i][j]}
                dp[i][j] = max(dp[i-1][j],1)
            else:
                dp[i][j] = 0

        if j-1 >= 0:
            if not A[i][j] in st[i][j-1]:
                st[i][j] = {*st[i][j-1], A[i][j]}
                dp[i][j] = max(dp[i][j-1], 1)
            else:
                dp[i][j] = 0

        if i-1 >= 0 and j-1 >= 0:
            if not A[i][j] in st[i-1][j] and not A[i][j] in st[i][j-1]:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print([i,j], A[i][j], st[i][j], dp[i][j])   
        
print(dp[H-1][W-1])

