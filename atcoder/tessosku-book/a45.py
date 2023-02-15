N, C = input().split()

# cards = {"R": 0, "B":0, "W": 0}
# for c in input():
#     cards[c] += 1

# Cのためには、最後の状態がわかる
# 1回の操作ごとに1枚消えていくことがわかる。
# いやーこれ難しいな。どうやってとくのかな？
# 計算量的にNで終わらせないといけないね

values = {"R": 2, "B":1, "W": 0}
A = sum(map(lambda x: values[x], input())) % 3

if (values[C] == A):
    print("Yes")
else:
    print("No")

