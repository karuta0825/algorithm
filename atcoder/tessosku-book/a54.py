Q = int(input())

obj = {}

for _ in range(Q):
   query = input().split()

   if (query[0] == '1'):
       obj[query[1]] = query[2]

   if (query[0] == '2'):
       print(obj[query[1]])
