INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
from collections import deque

class Graph():
    def __init__(self, v):
        from heapq import heappop, heappush
        self.v = v
        self.graph = [[] for _ in range(v)]
        self.INF = 10 ** 9
    
    def addEdge(self, start, end, edge):
        self.graph[start].append((end, edge))
        self.graph[end].append((start, edge))

def do():
    n=INT()
    g=Graph(n)
    for i in range(n-1):
        a,b=INTM()
        a-=1
        b-=1
        g.addEdge(a,b,i)

    
    que=deque()
    check=[True]*n
    clrs=[0]*(n-1)
    que.append([0,0])
    check[0]=False
    while que:
        clr=1
        now,clr_f=que.popleft()
        if clr_f==1:
            clr=2
        for next,i in g.graph[now]:
            if check[next]:
                check[next]=False
                que.append([next,clr])
                clrs[i]=clr
                clr+=1
                if clr==clr_f:
                    clr+=1
    
    print(max(clrs))
    for i in range(n-1):
        print(clrs[i])








def __starting_point():
    do()
__starting_point()