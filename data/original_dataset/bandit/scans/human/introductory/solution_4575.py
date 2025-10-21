n=int(input())
d,x=map(int,input().split())
for i in range(n):
  t=int(input())
  x+=(d+t-1)//t
print(x)