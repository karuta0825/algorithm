input()
As = map(int, input().split())

# すごい関数型でいけそうな感じの処理だよね
p = 0
ary = [0] * 4

def add(ary, num):
    global p
    new_ary = [0] * 4
    ary[0] = 1
    for i in range(len(ary)):
        if (ary[i] == 1):
            ni = i + num
            if (ni < len(ary)):
                new_ary[ni] = 1
            else:
                p += 1

    return new_ary

for a in As:
    ary = add(ary, a)

print(p)
