n=int(input())
r = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
a=0
b=0
for i in range(n):
    if r[i]==1 and s[i]==0:
        a+=1
    if r[i]==0 and s[i]==1:
        b+=1
if a==0:
    print(-1)
else:
    print((b)//a+1)