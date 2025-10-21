l=input().strip().split(" ");
n=int(l[0]);
m=int(l[1]);
t=m;
v=[];
for i in range(n+1):
  v.append([]);
while t>0:
  l=input().strip().split(" ");
  a=int(l[0]);
  b=int(l[1]);
  v[a].append(b);
  t-=1;

ans=0 ;
for p in range(1,n+1):
  gp={};
  for ch in range(1,n+1):
    gp[ch]=0;
  
  for u in v[p]:
    for x in v[u]:
      if(x!=p):
        gp[x]+=1;
  #print(gp);
   
  for ch in gp:
    ans+=(gp[ch]*(gp[ch]-1))//2;
  
print (ans);