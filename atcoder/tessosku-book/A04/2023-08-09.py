N = int(input())


ans = ""


for i in range(10):

    syo = N // (2 ** i)

    if syo % 2 == 1:
        ans += "1"
    else:
        ans += "0"

print(ans[::-1])
