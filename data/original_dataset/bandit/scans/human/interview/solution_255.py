n=int(input())
a=sorted(map(int,input().split()))
m=int(input())
b=sorted(map(int,input().split()))
c=0
for i in range(n):
  for j in range(m):
    if abs(a[i]-b[j]) <= 1:
      b[j]=-10
      c+=1
      break
print(c)