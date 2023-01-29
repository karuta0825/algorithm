N = int(input())

ans = 0
for _ in range(N):
    word = input()
    if (word == 'For'):
        ans += 1


if (N // 2 < ans):
    print("Yes")
else:
    print("No")
