import math
a = []
for i in range(5):
    a.append(int(input()))
sum = 0
r =10
for i in range(5):
  if a[i] % 10 ==0:
    sum+=a[i]
  elif a[i] % 10 !=0:
    r = min(r,a[i]%10)
    sum+= (10*math.ceil(a[i]/10))
print(sum-10+r)