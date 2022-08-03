num = int(input())
ary = [
    input() for _ in range(num)
]

result = 'correct'

def ok(i,j):
    if ((ary[i][j] == "L" and ary[j][i] == "W") or
        (ary[i][j] == "W" and ary[j][i] == "L") or
        (ary[i][j] == "D" and ary[j][i] == "D") or
        (ary[i][j] == "-" and ary[j][i] == "-")):
        return True

    return False
    

for i in range(num):
    for j in range(num):
        if not ok(i,j):
            result = 'incorrect'
            break

print(result);
            

