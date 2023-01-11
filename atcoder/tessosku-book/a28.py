qlgT = int(input())

ans = 0
divisor = 10000

for _ in range(T):
    T, A = input().split()

    if (T == "+"):
        ans += int(A)

    if (T == "-"):
        ans -= int(A)

    if (T == "*"):
        ans *= int(A)

    ans = ans % divisor

    print(ans)
