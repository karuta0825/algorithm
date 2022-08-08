# N = int(input())
# values = list(map(int, input().split()))

# result = 0

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if (i < j):
#             if (
#                     (min(values[i-1], values[j-1]) == i)
#                     and
#                     (max(values[i-1], values[j-1]) == j)
#             ):
#                 result += 1

# print(result)

# こっちもだめです。
# N = int(input())
# values = list(map(int, input().split()))

# result = 0
# for j in range(N, 1,-1):
#     for i in range(1, j):
#         if (
#                 (min(values[i-1], values[j-1]) == i)
#                 and
#                 (max(values[i-1], values[j-1]) == j)
#             ):
#             result += 1

# print(result)                



# これで溶けるんだけど実行制限時間内では無理ということを知らないといけない
# そのためにどうやって工夫をするのかということである

# 工夫として条件を次の2つを満たすものだとかんがえる。
# 1. a_i = i ^ a_j = j
# 2. a_i = j ^ a_j = i

# 1. はindexとその中身が同じものを抜き出し、その数をnとする。
#    次に、nから2つの組み合わせを求めるため n * (n-1) // 2で求まる。

# 2. a_i = j ^ a_j = i

