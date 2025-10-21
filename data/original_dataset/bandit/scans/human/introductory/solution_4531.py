import traceback
import sys
sys.setrecursionlimit(200010)

try:
    # alpha = "abcdefghijklmnopqrstuvwxyz"

    n = int(input())
    a = [0]
    a.extend(list(map(int, input().split())))
    D = [[] for i in range(n+1)]
    for i in range(n-1):
        e1,e2 = (map(int, input().split()))
        D[e1].append(e2)
        D[e2].append(e1)

    # for i in range(1,n+1):
    #     if i not in D:
    #         D[i] = []

    visited = [False for i in range(n+1)]
    cost = [a[i] for i in range(n+1)]
    parent = [0 for i in range(n+1)]
    val = 0

    def dfs(s, depth):  
        nonlocal visited
        nonlocal cost  
        nonlocal val  
        nonlocal a
        nonlocal D
        stack = [(s,depth)]
        while stack:
            s, depth = stack[-1]
            if visited[s]:
                stack.pop()
                cost[parent[s]]+=cost[s]
                continue
            else:    
                visited[s] = True
                val += depth*a[s]
            for i in D[s]:
                if not visited[i]:   
                    parent[i] = s
                    stack.append((i, depth+1))
                    # cost[s]+=cost[i]

    dfs(1, 0)

    # ans = 1
    max_cost = val
    # print(max_cost)
    visited = [False for i in range(n+1)]
    cost[0] = sum(a)
    def trav(s, some_val):
        nonlocal cost  
        nonlocal visited
        nonlocal max_cost
        nonlocal D 
        stack = [(s,some_val)]
        while stack:
            s, some_val = stack.pop()
            visited[s] = True
            # print(some_val, s)
            if some_val>max_cost:
                max_cost = some_val

            for i in D[s]:
                if not visited[i]:     
                    # print(i, some_val, cost[s], cost[i])
                    stack.append((i, some_val+(cost[0]-cost[i])-cost[i] ))


    trav(1, val)
    print(max_cost)
except Exception as ex:
    traceback.print_tb(ex.__traceback__)
    print(ex)