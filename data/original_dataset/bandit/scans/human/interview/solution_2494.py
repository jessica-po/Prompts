from collections import deque
K=int(input())


INF=10**9
res=[INF]*(K)
res[1]=1
q=deque()
q.append(1)
while q:
    r=q.popleft()
    if r==0:
        break
    nr=(r+1)%K
    if res[r]<res[nr]:
        res[nr]=res[r]+1
        q.append(nr)
    nr=(10*r)%K
    if res[r]<res[nr]:
        res[nr]=res[r]
        q.appendleft(nr)
print(res[0])