# 問題
# A 円硬貨、B 円硬貨、C 円硬貨をそれぞれ 0 枚以上使ってちょうど N 円を支払うとき、
# 使う硬貨の枚数として考えられる最小値を求めてください。

# ただし、それぞれの硬貨は無数にあるものとします。

# 制約
# 1≤A,B,C,N≤10**9 
# A,B,C はすべて異なる
# 合計 9999 枚以下の硬貨でちょうど N 円を支払うことができる
# 入力はすべて整数


N = 227
coins = [21, 47, 56]

# Idea1: 全探索
# 10**9なので全探索は難しそう

# Idea2: 動的計画法

# Idea3: 貪欲法

def search(w, acm, choices):
    if (w < 0):
        return False
    
    if (len(choices) == 0):
        if (w == 0):
            return True
        else:
            return False

    select = choices[0]
    print(acm)
    
    # 選ぶ
    if(search(w - select, [* acm, select], choices)):
        return acm


    # 選ばない
    if(search(w, acm, choices[1:])):
        return acm
    
    return acm

# つかうかつかわないか
# 使う場合
result = search(N, [], sorted(coins, reverse=True))

