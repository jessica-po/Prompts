import random
def S(L):
    Ans=[]
    s=0
    for item in L:
        s+=item
        Ans.append(s)
    return Ans

n,k=map(int,input().split())

B=list(map(int,input().split()))



Sums=[]
s=0
for i in range(n):
    s+=B[i]
    Sums.append(s)

if(k<=n):
    for i in range(k):
        print(i+1,end="")
        for j in range(i+1):
            print(" "+str(B[j]),end="")
        print()

else:
    Ans=[]
    length=1
    Taken={}
    Sums=S(B)
    while(len(Ans)<k):
        if(length>n):
            length=1
            random.shuffle(B)
            Sums=S(B)
        for i in range(n):
            if(i+length-1>=n):
                break
            x=Sums[i+length-1]-Sums[i]+B[i]
            if(x in Taken):
                continue
            Taken[x]=True
            L=[length]
            done=True
            for j in range(i,i+length):
                if(B[j] in L[1:]):
                    done=False
                    break
                L.append(B[j])
            if(done):
                Ans.append(list(L))
        length+=1
    for i in range(k):
        item=Ans[i]
        print(item[0],end="")
        for z in range(1,len(item)):
            print(" "+str(item[z]),end="")
        print()