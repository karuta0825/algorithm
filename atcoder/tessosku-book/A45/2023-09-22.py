N, C = input().split()

obj = {
    "W": 0,
    "B": 1,
    "R": 2
}

acm = 0

for c in input():
    acm += obj[c]


if acm % 3  == obj[C]:
    print("Yes")
else:
    print("No")
