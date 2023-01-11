A, B = map(int, input().split())
# 35 15の最大公約数
# GTMだっけ？
# これ決まってるよね？

def gcd(a, b):
    if (b == 0):
        return a

    return gcd(b, a % b)



print(gcd(A,B))
