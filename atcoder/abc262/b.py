
N, M = map(int, input().split())
values = [list(map(int, input().split())) for i in range(M)]

def check(i,j):
    if i in streetMap:
        return j in streetMap[i]
    else:
        return False

streetMap = {}
for f,s in values:
    if not (f in streetMap):
        streetMap[f] = [s]
    else:
        streetMap[f] = [* streetMap[f], s]

    if not (s in streetMap):
        streetMap[s] = [f]
    else:
        streetMap[s] = [* streetMap[s], f]        

# 全探索だけど、三重ループでcontinueをつかってショートカットすれば良い。
result = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if (i >= j):
            continue
        for k in range(1,N+1):
            if (j >= k):
                continue
            if (check(i,j) and check(j,k) and check(k,i)):
                result += 1
                
print(result)
    
