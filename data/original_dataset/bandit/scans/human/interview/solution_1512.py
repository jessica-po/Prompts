from sys import stdin, stdout

n = int(stdin.readline().rstrip())
p = list(map(int,stdin.readline().rstrip().split()))

if n==1:
    print(p[0])
else:
    removeDict={i:0 for i in range(1,n+1)}
    l1 = p[0]
    removeDict[l1]-=1
    l2 = 0
    for i in range(1,n):
        if p[i]>l2:
            if p[i]>l1:
                l2=l1
                l1=p[i]
                removeDict[l1]-=1
            else:
                l2=p[i]
                removeDict[l1]+=1
    maxN = 1
    maxRemove=-10
    for i in range(1,n+1):
        if removeDict[i]>maxRemove:
            maxN = i
            maxRemove = removeDict[i]
    
    print(maxN)