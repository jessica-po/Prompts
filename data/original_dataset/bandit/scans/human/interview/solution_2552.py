import sys
input = sys.stdin.readline
T = int(input())



for testcase in range(1,T+1):
    n,m = map(int,input().split())
    p = tuple(map(int,input().split()))
    h = tuple(map(int,input().split()))

    a = [0]*n
    b = [0]*n

    edge = [[] for i in range(n)]
    for _ in range(n-1):
        x,y = map(int,input().split())
        edge[x-1].append(y-1)
        edge[y-1].append(x-1)
    
    par = [-1]*n
    tank = [0]
    order = []
    while tank:
        now = tank.pop()
        order.append(now)
        for e in edge[now]:
            if par[now] != e:
                par[e] = now
                tank.append(e)
    flag = True
    for e in order[::-1]:
        if (a[e]-b[e]-p[e] <= h[e] <= a[e]+b[e]+p[e]) and (h[e]+a[e]+b[e]+p[e])%2 == 0:
            if e != 0:
                a[par[e]] += (h[e]+a[e]+b[e]+p[e])//2
                b[par[e]] += (h[e]+a[e]+b[e]+p[e])//2 - h[e]
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")