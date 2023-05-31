import string
H, W = map(int, input().split())

als = ["."] + list(string.ascii_uppercase)

for _ in range(H):

    A = map(lambda x: als[int(x)] , input().split())

    print("".join(A))
