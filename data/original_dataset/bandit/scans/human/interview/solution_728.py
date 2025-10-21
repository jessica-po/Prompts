n=int(input())
a=list(map(int,input().split()))
b=0
a[1:]=sorted(a[1:])
while a[0]<=a[-1]:
    a[-1]-=1
    a[0]+=1
    b+=1
    a[1:]=sorted(a[1:])
print(b)