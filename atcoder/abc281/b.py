import re
S = input()

p = re.compile("{}".format("^[A-Z][1-9][0-9]*[A-Z]$"))

# p = re.compile("{}".format("[A-Z][1-9]{1}[0-9]*[A-Z]"))
# このようにかくとre.match(p, "A101XX")でアウトになる
# 先頭から一致していて最後が違う場合もヒットしてしまうため

result = "Yes"
if (re.match(p, S)):
    num = int(S[1:len(S)-1])
    if (100000 <= num <= 999999):
        result = "Yes"
    else:
        result = "No"
else:
    result = "No"

print(result)
