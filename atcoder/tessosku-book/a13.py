N, K = map(int, input().split())
A = list(map(int, input().split()))

# ans = 0

# minj = 0
# for j in range(len(A)):
#     if (j > K):
#         minj = j
#         break

# # これが単純な組み合わせのやり方
# # だけどTLEになるので工夫しないといけない
# for i in range(minj, len(A)):
#     for j in range(i):
#         if (A[i] - A[j] <= K):
#             ans += 1

# print(ans)            

ans = 0
j = 0
for i in range(N):
    j = max(j, i + 1)
    # j = i + 1
    
    # jを毎回+1することに意味はない。一番端っこを知りたいだけだから。
    # 端っこがわかれば、ans += j - i - 1 のようにして求められるからである。
    # なぜ
    while j < N and A[j] - A[i] <= K:
        print([i, j])
        j += 1

    ans += j - i - 1

print(ans)    

