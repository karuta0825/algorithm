N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# 組み合わせ問題
# A ~ Dをそれぞれ10 ** 3なので、全探索ならば、 10 ** 12になってしまう。みっつもアウトになってしまう。
# 並び替えたからだとうまく行くかな？
# 並び替えてからK以下の数字だけ撮ってきて、それだけで作ってみるのだ。
# 解答ができるかどうかの2宅ってこともきになるんだよね？

# なるほどグループするのか
# ２つの全通りを足し算する方法は以下で確認できる
# これはすごいな。
# [a + b for a in range(3) for b in range(3)]
AB = set([a + b for a in A for b in B])
CD = set([c + d for c in C for d in D])

result = "No"

# 検索するときにsetを使うことで1オーダでアクセスすることができる
# setを利用すると、自動で並び替えが発生して重複も消える
# O(1)でREADができてO(N)で更新できる
for ab in AB:
    if K - ab in CD:
        result = "Yes"
        break;

print(result)
