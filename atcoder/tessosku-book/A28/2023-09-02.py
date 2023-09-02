N = int(input())

ans = 0
syo = 10 ** 4

def proc(ope, num, ans):

    if ope == "+":
        return num + ans

    if ope == '-':
        return ans - num

    if ope == "*":
        return num * ans


for _ in range(N):

    ope, num = input().split()

    ans = proc(ope, int(num), ans) % syo
    print(ans)
