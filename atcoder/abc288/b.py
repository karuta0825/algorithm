N, K = map(int, input().split())

ary = []
for i in range(N):
    s = input()
    if (i+1 <= K):
        ary.append(s);

print(*sorted(ary), sep="\n")
