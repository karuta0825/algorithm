A = list(map(int, input().split()))

b = "0b{}".format("".join(map(str, reversed(A))))

print(int(b,0))
