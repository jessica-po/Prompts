n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
l2=[0]*(n+1)
for i in a:
    l[i]+=1

for i in range(1,n+1):
    l2[i]=l[i]*(l[i]-1)//2
sum_l=sum(l2)
for i in range(1,n+1):
    print((sum_l-(l[a[i-1]]-1)))