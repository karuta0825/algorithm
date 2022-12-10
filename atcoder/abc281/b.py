import re
S = input()

p = re.compile("{}".format("[A-Z][1-9]{1}[0-9]*[A-Z]"))

# p = re.compile("".format("(?P<A>[A-Z])(?P<V>[0-9]{6})(?P<B>[A-Z])"))

# p.findall("")

# "A0B"[1:2]
# "010".isdigit()

result = "Yes"
if (re.match(p, S)):
    length = len(S)
    num = int(S[1:length-1])
    if (100000 <= num <= 999999):
        result = "Yes"
    else:
        result = "No"
else:
    result = "No"

print(result)
