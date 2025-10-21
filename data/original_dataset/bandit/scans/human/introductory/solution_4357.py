a=input().split()
a.sort(reverse=True)
if len(set(a))==1:
  print(12*int(a[0]))
else:
  ans=int(a[0]+a[1])+int(a[2])
  print(ans)