N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cd=[list(map(int,input().split())) for i in range(M)]
li=[[] for i in range(N+1)]
for i in range(M):
    li[cd[i][0]].append(cd[i][1])
    li[cd[i][1]].append(cd[i][0])
li2=[0]*(N+1)
num=0
for i in range(1,N+1):
    deque=[i]
    if li2[i]!=0:
        break
    li2[i]=i
    num=i
    while deque:
        x=deque.pop(0)
        for j in li[x]:
            if li2[j]==0:
                li2[j]=i
                deque.append(j)
li3=[[] for i in range(num)]
for i in range(1,N+1):
    li3[li2[i]-1].append(i-1)
for i in range(len(li3)):
    A=0
    B=0
    for j in range(len(li3[i])):
        A+=a[li3[i][j]]
        B+=b[li3[i][j]]
    if A!=B:
        print("No")
        break
    elif i==len(li3)-1:
        print("Yes")