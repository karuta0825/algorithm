inputs = input().split()

ary = []
for i in inputs:
    if (not i in ary):
        ary.append(i)

print(len(ary))
