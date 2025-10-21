n=int(input())
a,b=2,1
for i in range(n):
    nxt=a+b
    a,b=b,nxt
print(a)