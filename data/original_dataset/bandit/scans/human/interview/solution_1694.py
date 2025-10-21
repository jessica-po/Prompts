import sys
n,m,s,f=list(map(int,sys.stdin.readline().split()))
L=[]
R=[]
T=[]
for i in range(m):
    t,l,r=list(map(int,sys.stdin.readline().split()))
    T.append(t)
    L.append(l)
    R.append(r)

if(f>s):
    i=s
    step=1
    ind=0
    Ans=""
    while(i!=f):
        if(ind>=m or T[ind]!=step):
            Ans+="R"
            i+=1
        else:
            if((i>=L[ind] and i<=R[ind]) or (i+1>=L[ind] and i+1<=R[ind])):
                Ans+="X"
            else:
                Ans+="R"
                i+=1
            ind+=1
        step+=1
else:
    i=s
    step=1
    ind=0
    Ans=""
    while(i!=f):
        if(ind>=m or T[ind]!=step):
            Ans+="L"
            i-=1
        else:
            if((i>=L[ind] and i<=R[ind]) or (i-1>=L[ind] and i-1<=R[ind])):
                Ans+="X"
            else:
                Ans+="L"
                i-=1
            ind+=1
        step+=1
sys.stdout.write(Ans+"\n")