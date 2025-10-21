N=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(N):
    if cnt+1==a[i]:
        cnt+=1
if cnt==0:
    print((-1))
else:
    print((N-cnt))