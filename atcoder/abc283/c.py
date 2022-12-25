S = input()

SS = S[::-1]

ans = 0
cnt = 0

while ans < len(S):
    display = SS[ans]
    if (0 < int(display) <= 9):
        ans += 1
    else:
        if (ans + 1 < len(S)):
            next_display = int(SS[ans+1])
            if (next_display == 0):
                ans += 2
            else:
                ans += 1

    cnt += 1

print(cnt)
