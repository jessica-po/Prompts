n=int(input())
a=list(map(int,input().split()))
i=0
b=[]
while i+1<n:
    if a[i]==a[i+1]:
        a[i+1]=a[i]+1
        if len(b)>0:
            a[i]=b.pop()
        else:
            i=i+1
    else:
        b.append(a[i])
        i=i+1
b.append(a[-1])
print(len(b))
print(*b)