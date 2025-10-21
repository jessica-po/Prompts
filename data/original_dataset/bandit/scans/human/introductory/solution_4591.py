a,b,c,x,y = list(map(int,input().split()))

if (a + b) <= 2 * c:
  print((a * x + b * y))
else:
  max_c = max(x,y)
  min_c = min(x,y)
  AB = 2 * c * max_c
  if x > y:
    SP = ((x - min_c) * a) + (2 * c * min_c)
  else:
    SP = ((y - min_c) * b) + (2 * c * min_c)
  print((min(AB,SP)))