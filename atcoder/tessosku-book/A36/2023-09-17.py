N, K = map(int, input().split())

ans = "No"

zan = K - (N-1) * 2
if zan >= 0 and zan % 2 == 0:
    ans = "Yes"

print(ans)
