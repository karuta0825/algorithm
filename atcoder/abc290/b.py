N, K = map(int, input().split())
S = input()

cnt = 0
ans = ""
for c in S:

    if cnt < K and c == "o":
        ans += "o"
        cnt += 1
    else:
        ans += "x"


print(ans)
