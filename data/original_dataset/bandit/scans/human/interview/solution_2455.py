T=int(input())

for t in range(T):
    s=input()
    ans=0
    L=[]
    for i in [1,2,3,4,6,12]:
        x=i
        y=12//x
        E=[]
        for j in range(12):
            if(j%y==0):
                E.append("")
            E[-1]+=s[j]
        for j in range(y):
            c=0
            for z in range(i):
                if(E[z][j]=='X'):
                    c+=1
            if(c==i):
                ans+=1
                L.append(i)
                break
    print(ans,end=" ")
    for item in L:
        print(item,end="x")
        print(12//item,end=" ")
    print()