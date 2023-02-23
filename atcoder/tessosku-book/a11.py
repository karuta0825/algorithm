N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = len(A)

# 1. while文でとく
# result = True
# while result:
#     middle = (left + right )//2
#     if (A[middle] > X):
#         right = middle
#     elif (A[middle] < X):
#         left = middle
#     else:
#         result = False
#         print(middle + 1)

# 2. 再帰関数でとく
# どうして左右の移動で偶数奇数問題はないのだろうか？とおもう。
# 移動してるのはindexであり、indexの値ではない。
# indexは必ず=1でならんでるから可能なのではないかね
def search(left, right):
    middle = (left + right) // 2
    if (A[middle] > X):
        return search(left, middle)
    elif (A[middle] < X):
        return search(middle, right)
    else:
        return middle + 1

print(search(L, R))
