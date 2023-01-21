wN, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

P -= 1
Q -= 1
R -= 1
S -= 1

f  = A[:P]
pq = A[P:Q+1]
mi = A[Q+1:R]
sr = A[R:S+1]
la = A[S+1:]

print(*[*f, *sr, *mi, *pq, *la])
