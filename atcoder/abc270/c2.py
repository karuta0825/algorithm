import sys
sys.setrecursionlimit(10**9)

N, X, Y = map(int, input().split())

g = {}
for i in range(1, N+2):
    g[i] = []


for _ in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = [0] * (N+1)
visited[0] = 1

def dfs(i, r):

    visited[i] = 1
    r.append(i)

    for j in g[i][:]:
        if (visited[j] == 1):
            continue
        else:
            dfs(j, r)

    if not (r[-1] == Y):
        r.pop()

    return r

print(*dfs(X, []))

# 解法part2
# import sys
# sys.setrecursionlimit(10**9)

# N, X, Y = map(int, input().split())
# g = [[] for _ in range(N+1)]

# for _ in range(N-1):
#     u, v = map(int, input().split())
#     g[u].append(v)
#     g[v].append(u)

# ans = []
# def dfs(v, p = -1):
#     if (v == X):
#         ans.append(v)
#         return True

#     for u in g[v]:
#         if (u == p):
#             continue

#         if (dfs(u, v)):
#             ans.append(v)
#             return True

#     return False

# dfs(Y)

# print(*ans)
