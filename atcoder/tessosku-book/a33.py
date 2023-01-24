N = int(input())
A = list(map(int, input().split()))


grandy = 0
for i in A:
    grandy ^= i

if grandy == 0:
    print("Second")
else:
    print("First")    

