n, x = map(int, input().split())


result = "No"
for i in map(int, input().split()):
    if (i == x):
        result = "Yes"
        break

print(result)
