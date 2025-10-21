n=int(input())
a=[]
for i in range(n):
  t=list(input().split())
  t[1]=int(t[1])
  t.append(i)
  a.append(t)
a.sort(key=lambda x:(x[0],-x[1]))
for t in a:
  print(t[2]+1)