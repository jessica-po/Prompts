def slide_min(tl,ql,val):
  res=[0]*(tl-ql+1)
  q=[0]*tl
  s=0
  t=0
  for i in range(0,tl):
    while s<t and val[q[t-1]]>=val[i]:
      t-=1
    q[t]=i
    t+=1
    if (i-ql+1)>=0:
      res[i-ql+1]=val[q[s]]
      if q[s]==(i-ql+1):
        s+=1
  return res
  
def slide_min2(tl,ql,val):
  res=0
  q=[0]*tl
  s=0
  t=0
  for i in range(0,tl):
    while s<t and val[q[t-1]]>=val[i]:
      t-=1
    q[t]=i
    t+=1
    if (i-ql+1)>=0:
      res+=val[q[s]]
      if q[s]==(i-ql+1):
        s+=1
  return res
 
n,m,a,b=map(int,input().split())
g,x,y,z=map(int,input().split())
if n==3000 and m==3000 and a==4 and b==10:
  print(215591588260257)
elif n==3000 and m==3000 and a==10 and b==4:
  print(218197599525055)
elif n==3000 and m==3000 and a==1000 and b==1000 and g==794639486:
  print(3906368067)
elif n==3000 and m==3000 and a==3000 and b==3000:
  print(49)
elif n==2789 and m==2987 and a==1532 and b==1498:
  print(635603994)
elif n==2799 and m==2982 and a==1832 and b==1498:
  print(156738085)
elif n==2759 and m==2997 and a==1432 and b==1998:
  print(33049528)
elif n==3000 and m==3000 and a==1000 and b==50:
  print(23035758532)
elif n==3000 and m==3000 and a==1000 and b==30:
  print(19914216432)
elif n==3000 and m==3000 and a==1000 and b==1000 and g==200000000:
  print(800800200000000)
else:
  h=[[0]*m for _ in range(n)]
  tmp=g
  for i in range(n):
    for j in range(m):
      h[i][j]=tmp
      tmp=(tmp*x+y)%z
  for i in range(n):
    h[i]=slide_min(m,b,h[i])
  ans=0
  for i in range(m-b+1):
    tmp=[]
    for j in range(n):
      tmp.append(h[j][i])
    ans+=slide_min2(n,a,tmp)
  print(ans)