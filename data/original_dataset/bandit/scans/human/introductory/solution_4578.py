n,x=list(map(int,input().split()))
y = [int(input()) for i in range(n)]
y.sort()
c = 0
for i in range(n):
  if c < x:
    c +=y[i]
  elif c > x:
    print((i-1))
    return
d = sum(y)
print((((x-d)//y[0])+n))