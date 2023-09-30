import string
N, Q =  map(int, input().split())
s = input()

dic = {}
for (i, c) in enumerate(string.ascii_letters):
    dic[c] = i + 1

mod = 2147483647

power100 = [ None ] * (N + 1)
power100[0] = 1
for i in range(N):
    power100[i + 1] = power100[i] * 100 % mod

def Hash(l, r):
    val = (S[r] - power100[r-l+1] * S[l-1]) % mod
    if val < 0:
        val += mod
        return val
    return val



B = 100
S = [0] * (N+1)
for i in range(N):
    S[i+1] = (dic[s[i]] + (B * S[i])) % mod


for _ in range(Q):
    l1, r1, l2, r2 = map(int, input().split())

    if Hash(l1, r1) == Hash(l2, r2):
        print("Yes")
    else:
        print("No")
