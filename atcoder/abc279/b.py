import re
s = input()
t = input()


pattern = re.compile("{}".format(t))

if (re.search(pattern, s)):
    print("Yes")
else:
    print("No")
