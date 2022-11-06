str = input()

seq = []
for i in range(len(str)):
    if ( str[i] == "a"):
        seq.append(i + 1)

if (len(seq) == 0):
    print(-1)
else:
    print(seq[-1])    

