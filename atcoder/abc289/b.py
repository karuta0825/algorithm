N, M = map(int, input().split())

A = list(map(int, input().split()))

visited = [0] * (N+1)
visited[0] = 1
removed = [0] * M

def find(v):
    ans = v
    for i in range(len(A)):
        if (removed[i]):
            continue

        if (A[i] == v):
            ans = find(v + 1)

    return ans

ans = []
i = 1
while sum(visited) < N+1:

    if (visited[i]):
        i += 1
        continue
    else:
        v= find(i)
        if (v-1 in A):
            A.remove(v-1)
        ans.append(v)
        visited[v] = 1
        i = 0

print(*ans)
