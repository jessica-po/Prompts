x=int(input())
m=-1000
if 1<=x<=3:
  print((1))
  return
else:
  for b in range(2,x+1):
   for p in range(2,11):
    if x>=b**p:
      m=max(m,b**p)
   

print(m)