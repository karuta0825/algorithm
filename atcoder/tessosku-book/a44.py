N, Q = map(int, input().split())

ans = list(range(1, N+1))

# なるほどこれでいけるけど計算量でアウトになるのか！それは意識できていないな。
# まだまだ駄目だな。どうすればいいのかな？
# for _ in range(Q):
#     q = list(map(int, input().split()))

#     if (q[0] == 1):
#         ans[q[1]-1] = q[2]
#     elif (q[0] == 2) :
#         ans = list(reversed(ans))
#     else:
#         print(ans[q[1]-1])


# 連結リストだと変わるのかな？あれってpythonでどうやってアクセスできるんだ？
# 計算量は変わりそうにないな

# フラグをもらってインデックスのアクセスを変えればよいのか！ N-1-xで後ろからアクセスできるってことか
# [1,2,3,4,5]に対して後ろから2番目にアクセスするには、前からは3番目
# 5(長さ) - 2(番目 1index) - 1 = 2 あれだめだな！
# 5(長さ) - 1(番目 0index) + 1 = 3 これだな
flip = False

for _ in range(Q):
    q = list(map(int, input().split()))

    if (q[0] == 1):
        [_, x, y] = q
        x -= 1
        if (flip):
            ans[N-1-x] = y
        else:
            ans[x] = y

    if (q[0] == 2):
        flip = not flip

    if (q[0] == 3):
        [_, x] = q
        x -= 1
        if (flip):
            print(ans[N-1-x])
        else:
            print(ans[x])
