

N = int(input())


def search(n):
    amari = n % 4
    if (amari == 2):
        return n
    else:
        return search(n + 1)

print(search(N))
    
