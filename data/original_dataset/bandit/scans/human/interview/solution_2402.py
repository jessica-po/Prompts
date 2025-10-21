t = int(input())
for _ in range(t):
  n,x,y = map(int,input().split())
  s = x+y
  mx = min(s-1,n)
  if s<=n:
    mn = 1
  else:
    mn = min(s,s-n+1,n)
  print(mn,mx)