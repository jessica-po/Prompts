n,m=map(int,input().split()) 
x,y,z=map(int,input().split())
edge=[[]for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  edge[a].append(b)
  edge[b].append(a)
color=[0]*n
def bfs(v,c):
  color[v]=c
  h=w=0
  if c==1:h=1
  else:w=1
  for i in edge[v]:
    if color[i]==c:return [False,h,w]
    elif color[i]==0:
      f,hh,ww=bfs(i,-c)
      h+=hh
      w+=ww
      if not f:return [False,h,w]
  return [True,h,w]
q=[]
for i in range(n):
  if color[i]==0:
    f,h,w=bfs(i,1)
    if not f:print("NO");return
    q.append([i,min(h,w),max(h,w)-min(h,w),1-2*(h<w)])
yy=y
for _,i,__,___ in q:yy-=i
if yy<0:print("NO");return
dp=[(yy+1)*[0]for _ in range(len(q)+1)]
dp[0][0]=1
for i in range(len(q)):
  _,__,ii,___=q[i]
  for j in range(yy+1):dp[i+1][j]=dp[i][j]
  for j in range(yy+1):
    if ii+j>yy:break
    dp[i+1][ii+j]|=dp[i][j]
if dp[-1][-1]==0:print("NO");return
k=yy
qq=[]
for i in range(len(q),0,-1):
  if dp[i][k]==dp[i-1][k]:qq.append((q[i-1][0],-q[i-1][3]))
  else:
    qq.append((q[i-1][0],q[i-1][3]))
    k-=q[i-1][2]
color=[0]*n
visited=set()
for i,c in qq:
  stack=[i]
  visited.add(i)
  color[i]=c
  for j in stack:
    for k in edge[j]:
      if k in visited:continue
      visited.add(k)
      color[k]=-color[j]
      stack.append(k)
for i in range(n):
  if color[i]==1:color[i]="2"
  elif x:color[i]="1";x-=1
  else:color[i]="3"
print("YES")
print("".join(color))