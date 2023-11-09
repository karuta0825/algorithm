# これ二分探索か? 逆関数だからな...
# もっとエレガントありそうだけど
B = int(input())

i = 1

while i ** i <= B:

    if i ** i == B:
        print(i)
        exit()

    i += 1

print(-1)
