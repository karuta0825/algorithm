H, W = map(int, input().split())

S = [[] for _ in range(W)]
T = [[] for _ in range(W)]

for _ in range(H):
    s = input()
    for j in range(len(s)):
        S[j].append(s[j])


for _ in range(H):
    t = input()
    for j in range(len(t)):
        T[j].append(t[j])

ss = sorted(S)
tt = sorted(T)

# print(ss)
# print(tt)

if (ss == tt):
    print("Yes")
else:
    print("No")

