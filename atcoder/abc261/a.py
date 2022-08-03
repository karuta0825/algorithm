
l1, r1, l2, r2 = map(int, input().split())

left = {i for i in range(l1, (r1 + 1))}
right = {i for i in range(l2, (r2+ 1))}

inter = left.intersection(right)

if len(inter) > 0:
    print(len(inter) - 1)
else:
    print(0)


