N = int(input())
X = list(map(int, input().split()))

X.sort()


l = X[N:][::-1][N:][::-1]

def avg(l):
    return sum(l) / len(l)

print(avg(l))
