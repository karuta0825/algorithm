# 素数判定プログラムか
# これは難しいなというか、知ってるかどうかなんだよなこれは。
# なるほど、素朴に考えたらという発想ね。そこからどうやって早くするのかを考えるのか！
N = int(input())

# これが単純実装である
# これを早くする方法を考える
# O(N)でNが10**6がQ(10000)回実行なので、10**11になり駄目なわけだ。
# O(logN)とかにできればな

# たとえば、4以上の偶数はすべて削除する -> これは駄目だった
# なるほど、ここであれがでてくるのか！試し割りね
# pypyでようやく解くことができた。なるほどギリギリなのね!
def isPrime(num):

    # for i in range(2, int(num ** 1/2)):
    #     if (num % i == 0):
    #         return False

    # return True
    i = 2
    while i ** 2 <= num:

        if (num % i == 0):
            return False

        i += 1

    return True

for i in range(N):
    x = int(input())

    result = isPrime(x)
    print("Yes" if result else "No")
