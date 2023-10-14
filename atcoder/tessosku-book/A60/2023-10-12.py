N = int(input())
A = list(map(int, input().split()))

stack = []
ans = []

for i in range(N):

    a = A[i]

    if len(stack) < 1:
        stack.append((i+1, a))
        ans.append(-1)
        continue

    while len(stack):

        pos, top = stack.pop()

        if top > a:
            ans.append(pos)
            stack.append((pos, top))
            break

    if len(stack) == 0:
        ans.append(-1)

    stack.append((i+1, a))


print(*ans)
