a=int(input())
b=int(input())
n=a+b+1
L=list(range(n-a,n+1))
for item in L:
    print(item,end=" ")
x=n-a-1
while(x>0):
    print(x,end=" ")
    x-=1