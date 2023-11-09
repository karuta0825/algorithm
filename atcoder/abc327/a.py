import re
N = int(input())
S = input()

p1 = re.compile("{}".format("ab"))
p2 = re.compile("{}".format("ba"))


if re.search(p1, S) or re.search(p2, S):
    print("Yes")
else:
    print("No")
