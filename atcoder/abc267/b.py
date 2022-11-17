import re
s = input()

if (s[0] == "1"):
    print("No")
    exit()

str = "0000000"
obj = {
    1: 3,
    2: 5,
    3: 2,
    4: 4,
    5: 6,
    6: 1,
    7: 3,
    8: 5,
    9: 7
}

for i in range(len(s[1:])):
    if(s[i+1] == "1"):
        tmp = list(str)
        tmp[obj[i+1] - 1] = "1"
        str = "".join(tmp)


pattern = re.compile("10+1")
# re.search(pattern, "0111011")
# re.search(pattern, "1011001")
# re.search(pattern, "0011100")
if (re.search(pattern, str)):
    print("Yes")
else:
    print("No")
