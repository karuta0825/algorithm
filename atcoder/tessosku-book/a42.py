N, K = map(int, input().split())

P = []
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    P.append((a,b))

# # うーんむずかしい。でもよい問題だ。
# def diff(p1, p2):
#     return abs(p1 - p2) - K <= 0

# for i in range(N):
#     for j in range(N):
#         if (j <= i):
#             continue

#         p1 = persons[i]
#         p2 = persons[j]
#         print(p1, p2, i+1, j+1, diff(p1[0], p2[0]), diff(p1[1], p2[1]))
#         if (diff(p1[0], p2[0]) and diff(p1[1], p2[1])):
#             ans += 1


# print(ans)

def score(a, b):
    cnt = 0
    for i in range(N):
        if (a <= P[i][0] and P[i][0] <= a + K
            and
            b <= P[i][1] and P[i][1] <= b + K):
            cnt += 1

    return cnt


for i in range(1, 101):
    for j in range(1, 101):
        s = score(i,j)
        ans = max(s, ans)

print(ans)
