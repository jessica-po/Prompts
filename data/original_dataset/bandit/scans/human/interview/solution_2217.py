def main():
    import sys
    input=sys.stdin.readline
    mod=998244353
    N=10**5+3
    fac=[1]*(N+1)
    for i in range(1,N+1):
        fac[i]=fac[i-1]*i%mod
    inv_fac=[1]*(N+1)
    inv_fac[N]=pow(fac[N],mod-2,mod)
    for i in range(N-1,0,-1):
        inv_fac[i]=inv_fac[i+1]*(i+1)%mod
    D=int(input())
    A=[]
    for i in range(2,int(D**.5)+1):
        c=0
        while D%i==0:
            D//=i
            c+=1
        if c!=0:
        	A.append(i)
    if D>=2:
        A.append(D)
    l=len(A)
    q=int(input())
    for _ in range(q):
        u,v=map(int,input().split())
        l1=[0]*l
        l2=[0]*l
        l3=[0]*l
        for i in range(l):
            while u%A[i]==0:
                l1[i]+=1
                u//=A[i]
            while v%A[i]==0:
                l2[i]+=1
                v//=A[i]
            l3[i]=l1[i]-l2[i]
        ans1=1
        ans2=1
        s1=0
        s2=0
        for i in range(l):
            if l3[i]>=0:
                ans1=ans1*inv_fac[l3[i]]%mod
                s1+=l3[i]
            else:
                ans2=ans2*inv_fac[-l3[i]]%mod
                s2-=l3[i]
        ans1=ans1*fac[s1]%mod
        ans2=ans2*fac[s2]%mod
        print(ans1*ans2%mod)
def __starting_point():
    main()
__starting_point()