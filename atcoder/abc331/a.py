# できたけど、なんだか気持ちが悪いな。進数という考えと同じ気がするのでやってみたら？
M, D = map(int, input().split())
y, m, d = map(int, input().split())


def tomorrow(y,m,d):
    ny, nm, nd = y, m, d+1

    if nd > D:
        nd = 1
        nm = m + 1

    if nm > M:
        nm = 1
        ny = y + 1

    return [ny, nm, nd]


print(*tomorrow(y,m,d))
