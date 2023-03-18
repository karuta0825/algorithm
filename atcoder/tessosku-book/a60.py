stack = []

N = int(input())
A = list(map(int, input().split()))

ans = []

for d in range(len(A)):

    while stack and A[d] >= A[stack[-1]]:
        stack.pop()

    if stack:
        ans.append(stack[-1] + 1)
    else:
        ans.append(-1)

    stack.append(d)

print(*ans)
