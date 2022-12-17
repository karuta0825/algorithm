import re
N = int(input())
S = input()

pattern = re.compile("{}".format(","))

ary = [[]]
for n in range(N):
    if (S[n] == '"'):
        last_element = ary[-1]
        if (len(last_element) < 2):
            last_element.append(n)
        else:
            new_element = [n]
            ary.append(new_element)
            
result = ""
index = 0
for a in ary:
    if (len(a) == 0):
        continue
    
    [start, end] =a 
    tmp = S[index:start]
    newstr = tmp.replace(",", ".")
    result += newstr
    result += S[start:(end+1)]
    index = end + 1

if (index < len(S)):
    tmp = S[index:]
    newstr = tmp.replace(",", ".")
    result += newstr
    
print(result)    
    
    
    
    
