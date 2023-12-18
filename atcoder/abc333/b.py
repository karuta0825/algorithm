S = input()
T = input()

S1, S2 = S[0], S[1]
T1, T2 = T[0], T[1]



pattern1 = {
    "A": ["B", "E"],
    "B": ["A", "C"],
    "C": ["B", "D"],
    "D": ["C", "E"],
    "E": ["D", "A"]
}

pattern2 = {
    "A": ["C", "D"],
    "B": ["E", "D"],
    "C": ["A", "E"],
    "D": ["A", "B"],
    "E": ["B", "C"]
}

def check(p0, p1):

    if p1 in pattern1[p0]:
        return 1

    if p1 in pattern2[p0]:
        return -1


h1 = check(S1, S2)
h2 = check(T1, T2)

if h1 * h2 == 1:
    print("Yes")
else:
    print("No")
