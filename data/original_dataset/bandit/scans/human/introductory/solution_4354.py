n,m=list(map(int,input().split()))
ab=[[int(x) for x in input().split()] for _ in range(n)]
cd=[[int(x) for x in input().split()] for _ in range(m)]

for a,b in ab:
  ans=list()
  for c,d in cd:
    ans.append(abs(a-c)+abs(b-d))
  print((ans.index(min(ans))+1))