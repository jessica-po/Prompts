import copy

s=input()
l=len(s)
ans=0

if l==1:
  ans+=int(s)
  print(ans)
  
else:
  for i in range(2**(l-1)):
    t=copy.deepcopy(s)
    f=[]
    ch=0
    for j in range(l-1):
      if ((i>>j)&1):
        t=t[:j+1+ch]+'+'+t[j+1+ch:]
        ch+=1
     
    if '+' in t:
      
      y=list(map(int,t.split('+')))
      for u in y:
        ans+=u
    else:
      ans+=int(t)
      
  print(ans)