n,a,b = map(int,input().split())
if a+b>n+1 or a*b<n:
  print(-1)
  return
ans = []
for i in range(1,a+1):
  ans.append(i*b)
if b == 1:
  x = list(range(1,n+1))
  print(*x)
  return
x = (n-a)//(b-1)
y = (n-a)%(b-1)
for i in range(1,b):
  for j in range(1,x+1):
    ans.append(j*b-i)
  if i <= y:
    ans.append((x+1)*b-i)
ans_true = []
for i,x in enumerate(ans):
  ans_true.append((i+1,x))
ans_true.sort(key=lambda x:x[1])
x = list(zip(*ans_true))[0]
print(*x)