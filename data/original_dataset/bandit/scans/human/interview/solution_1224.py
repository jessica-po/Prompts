n=int(input())
for i in range(1,100):
  if 3**i > n:
    print(-1)
    break
  x=n-3**i
  for j in range(1,100):
    if x==5**j:
      print(i,j)
      return