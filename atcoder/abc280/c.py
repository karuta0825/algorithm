S = input()
T = input()
# S = "atcoder"
# T = "atcoderr"

for i in range(len(T)):
    if len(S) <= i:
        print(i+1)
        break

    if (S[i] != T[i]):
        print(i + 1)
        break

# # 二部探索でいけるはずなんだ。
# # どうやってとめるかということですな. 終了条件は間違えてる文字列が1つになるまで
# n = (0 + len(S)) // 2
# m = (n + len(S)) // 2
# l = (n + m) // 2
# S[n:m]
# T[n:m]


# S = "vvwvw"
# T = "vvwvwv"

# n = (0 + len(S)) // 2
# m = (n + len(S)) // 2
# l = (n + m) // 2


# S[n:m+1]
# T[n:m+1]
