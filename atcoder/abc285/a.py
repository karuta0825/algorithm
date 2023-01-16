g = {
    1: [2,3],
    2: [4,5],
    3: [6,7],
    4: [8,9],
    5: [10,11],
    6: [12, 13],
    7: [14,15]
}

a, b = map(int, input().split())

result = "No"

if a in g and b in g[a]:
    print("Yes")
    exit()


if b in g and a in g[b]:
    print("Yes")
    exit()

print("No")
