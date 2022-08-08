import math
values = list(map(int, input().split()))

acm = {}

for v in values:
    if (v in acm):
        acm[v] += 1
    else:
        acm[v] = 1

result = "No"
# math.prodをしった
if (len(acm.keys()) == 2 and math.prod(acm.values()) == 6):
    result = "Yes"
        
print(result)
