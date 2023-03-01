import re
S = input()

l = list(re.finditer(r'[A-Z]', S))

print(l[0].span()[0] + 1)
