n, x = map(int, input().split())
ps = list(map(int, input().split()))

result = -1
for i in range(len(ps)):
    if (ps[i] == x):
        result = i + 1
        break;

print(result)
