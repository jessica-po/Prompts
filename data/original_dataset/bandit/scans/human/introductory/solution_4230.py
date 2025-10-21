x,n=map(int,input().split())
p=list(map(int,input().split()))
a=101
m=101-x
for i in range(102):
  i=100-i
  if i in p:
    continue
  M=abs(i-x)
  if M<=m:
    m=M
    a=i
print(a)