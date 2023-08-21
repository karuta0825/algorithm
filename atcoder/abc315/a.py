import re

s = input()
print(re.sub('(a|e|i|u|o)+', '', s))
