# import sys
# sys.setrecursionlimit(10**9)

# N, K = map(int, input().split())
# A = [0] + list(map(int, input().split()))

# def bb(l,r,x):
#     if r - l <= 1:
#         return r
    
#     m = (l + r) // 2

#     if A[m] < x:
#         return bb(m,r,x)
#     else:
#         return bb(l,m,x)

# ans = 0
# for i in range(1, N+1):


#     idx = bb(i, N, K + A[i])

#     if idx == N:
#         if A[idx] - A[i] >= K:
#             ans += (N - idx) + 1
#         continue
        
#     ans += (N - idx) + 1

# print(ans)

from bisect import bisect_left

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

ans = 0
for i in range(1, N):

    idx = bisect_left(A, A[i] + K)



    if idx <= N:
        if A[idx] == A[i] + K:
            idx += 1
        ans += idx - i - 1
    else:
        ans += N - i
        


print(ans)
