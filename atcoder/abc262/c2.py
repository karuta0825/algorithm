N = int(input())
A = list(map(int, input().split()))


for i in range(N):
    A[i] -= 1

same = 0
# a_i = i and a_j = j

for (i, x) in enumerate(A):
    if (i == x):
        same += 1

ans = same * (same - 1) // 2
for (i, j) in enumerate(A):
    if (i < j and A[j] == i):
        ans += 1

print(ans)

