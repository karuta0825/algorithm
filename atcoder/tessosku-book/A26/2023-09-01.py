Q = int(input())

def isPrime(n):
    N = int(n ** (1/2))
    for i in range(1, N+1):
        if i == 1:
            continue

        if n % i == 0:
            return False

    return True


for _ in range(Q):

    x = int(input())


    print("Yes" if isPrime(x) else "No")
