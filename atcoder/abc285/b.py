N = int(input())
S = input()


for i in range(N-1):
    i += 1
    ans= 0
    for j in range(N-1):
        if (j+i < N):
            if (S[j] != S[j+i]):
                ans += 1
            else:
                break

    print(ans)
