import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
yp=lambda:print('Yes')
np=lambda:print('No')

s=list(sp())
k=ip()

ans=set()

alpa=list(set(s))
alpa.sort()
ch=0
siyou=[]
for i in range(len(alpa)):
  if i<=2:
    siyou.append(alpa[i])
  else:
    break
    
for x in siyou:
  for i in range(len(s)):
    if s[i]==x:
      st=''
      for y in range(i,i+5):
        if y<len(s):
          st+=s[y]
          ans.add(st)
  if len(ans)>k:
    break
  
ans=list(ans)
ans.sort()
print(ans[k-1])