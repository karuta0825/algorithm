H, W = map(int, input().split())

X = [[0] * (W+1)]

for _ in range(H):
    X.append([0] + list(map(int, input().split())))

acm = []
for i in range(H+1):
    tmp = 0
    a = []
    for j in X[i]:
        tmp += j
        a.append(tmp)

    acm.append(a)

for i in range(W+1):
    tmp = 0
    for j in range(H+1):
        tmp += acm[j][i]
        acm[j][i] = tmp

# for i in acm:
#     print(i)
        
def sumSquare(a,b,c,d):
    sd = acm[c][d]
    sa = acm[c][b-1]
    sb = acm[a-1][d]
    ss = acm[a-1][b-1]
    return sd - sa - sb + ss    

    
Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())

    print(sumSquare(A, B, C, D))


