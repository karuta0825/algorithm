import re

s = input()
t = input()

pattern = s

repattern = re.compile("^{}".format(pattern))

if (re.match(repattern, t)):
    print("Yes")
else:
    print("No")
