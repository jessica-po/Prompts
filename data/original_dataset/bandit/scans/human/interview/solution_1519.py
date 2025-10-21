n,L,a=list(map(int,input().split()))
count=0
last=0
for i in range(n):
    t,l=list(map(int,input().split()))
    count+=(t-last)//a
    last=t+l
count+=(L-last)//a
print(count)