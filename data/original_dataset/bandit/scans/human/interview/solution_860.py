n=int(input())
c=[[] for i in range(n)]
[c[int(x)].append(i+1) for i,x in enumerate(input().split())]
s=0;r=[]
for i in range(n):
    while len(c[s])==0 and s>=0:
        s-=3
    if s<0:
        print('Impossible')
        break
    else:
        r+=[c[s].pop()]
        s+=1
else:
     print('Possible')
     print(*r)