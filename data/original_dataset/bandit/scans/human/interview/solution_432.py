import sys

rd = lambda : sys.stdin.readline().rstrip()

n = int(rd())
c = list(map(int, rd().split()))
a = list([int(x)-1 for x in rd().split()])

visited = [-1] * (n)
res = 0

for i in range(n):
    trace = []
    
    t = i
    mn = 1e9
    while visited[t] == -1:
        visited[t] = i
        trace.append(t)
        t = a[t]
        
    if visited[t] != i:
        continue
        
    while len(trace) > 0:
        v = trace.pop()
        mn = min(mn, c[v]) 
        
        if t == v: break
    
    res += mn
    
print(res)