N, X, Y = map(int, input().split())
inputs = [list(map(int, input().split())) for i in range(N-1)]

graph = [[] for i in range(N+1)] 
for [c, p] in inputs:
    graph[c].append(p);
    graph[p].append(c);    

# print(graph);
# routes = [False] * (N + 1)

# # 探索途中をstackをつかって表すって感じかな
# # だいぶよくなったな。そろそろ解答みてもよい時期だろうな
# # これでもRuntimeエラーが発生するｑ
# def c2p(start, goal, acm):
#     # print("start", start)
#     routes[start] = True

#     acm.append(start);
#     selections = graph[start]
    
#     for v in selections:
#         if routes[v]:
#             continue
#         if (v == goal):
#             acm.append(v)
#             break
        
#         tmp = c2p(v, goal, acm)

#         if (tmp[-1] != goal):
#             acm = tmp[:-1]
#         else:
#             acm = tmp
#             break

#     return acm

# # 誤ったルートは記録しないようにしたい
# goal_path = c2p(X,Y,[])

# print(" ".join(map(lambda x: str(x) , goal_path)));


##############
stop = False
deq = []
flag = [False] * (N + 1)

def dfs(k, to):
    global stop
    if (not stop):
        deq.append(k)
        
    if (k == to):
        stop = True;
        
    flag[k] = True;
    
    for v in graph[k]:
        if(not flag[v]):
            dfs(v,to)
        
    if(not stop and len(deq) > 0):
        deq.pop()    

dfs(X,Y)
print(*deq)
# print(" ".join(map(lambda x: str(x) , deq)));
