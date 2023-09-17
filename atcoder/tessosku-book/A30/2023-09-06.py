M = 1000000007

n, r = map(int, input().split())

bunshi = 1
for i in range(1, n+1):
    bunshi = (bunshi * i) % M

bunbo = 1
for i in range(1, r+1):
    bunbo = (bunbo * i) % M

for i in range(1, n-r+1):
    bunbo = (bunbo * i) % M    

# この bunbo ** M-2は時間かかるな！これが前の計算を使わないといけない
# やっぱりこれを実装しないといけないか!
def Power(a, b, m):
	p = a
	Answer = 1
	for i in range(30):
		wari = 2 ** i
		if (b // wari) % 2 == 1:
			Answer = (Answer * p) % m # a の 2^i 乗が掛けられるとき
		p = (p * p) % m
	return Answer

ans = (bunshi * Power(bunbo, M-2, M)) % M
print(ans)
