N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

A = [0, *list(map(int, input().split()))]
B = [0, 0, *list(map(int, input().split()))]

# def getMin(pos, accm):
#     # どっちが選択されたのかわからない
#     # print(pos, A, B)
#     if (pos == 0):
#         accm += A[pos+1]
#         return getMin(pos + 1, accm)

#     if (pos == N - 2):
#         accm += A[pos+1]
#         return accm

#     if (pos == N - 3):
#         accm += B[pos+2]
#         return accm


#     if (A[pos + 1] + A[pos + 2] <= B[pos + 2]):
#         minuites = A[pos + 1]
#         next_pos = pos + 1
#     else:
#         minuites = B[pos + 2]
#         next_pos = pos + 2

#     # print(minuites)
#     accm += minuites
#     return getMin(next_pos, accm)

# print(getMin(0, 0))

dp = [0] * N

for i in range(1, N):
    if (i == 1):
        dp[i] = dp[i-1] + A[i]
    else:
        dp[i] = min(dp[i-1] + A[i],
                    dp[i-2] + B[i])

print(dp[-1])        
