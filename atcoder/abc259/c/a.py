from itertools import takewhile
from functools import reduce

def ss (str, result):
    if len(str) == 0:
        return result
    else:
        c = str[0]
        num = len(list(takewhile(lambda x:x == c, str)))
        return ss(str[num:], [* result, [c, num]])

def tmp (acm, c):
    if len(acm) == 0:
        return [[c, 1]]
    
    [lc, ln] = acm[-1]
    
    if lc == c:
        newAcm = acm[:-1]
        newAcm.append([lc, ln + 1]);
        return newAcm;
    else:
        acm.append([c, 1])
        return acm
    
def ss2 (str):
    return reduce(tmp, str, [])

def ss3 (str):
    result = []
    for c in str:
        if len(result) == 0:
            result.append([c, 1])
            continue

        last = result[-1]
        if last[0] == c:
            last[1] = last[1] + 1
        else:
            result.append([c, 1])


    return result        


def check(a, b):
    astr = "".join(list(map(lambda x: x[0], a)))
    bstr = "".join(list(map(lambda x: x[0], b)))
    if (astr != bstr):
        return False
    
    for [f, g] in zip(a,b):
        if f[1] == 1 and g[1] >= 2:
            return False

        if f[1] != 1 and f[1] > g[1]:
            return False

    return True
        
one = input()
two = input()
# so = ss(one, [])
# st = ss(two, [])

so = ss3(one)
st = ss3(two)

if check(so, st):
    print("Yes")
else:
    print("No")
