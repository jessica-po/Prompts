q=int(input())
for t in range(q):
    n,k=map(int,input().split())
    a=input()
    ko=0
    used=[0]*n
    ans=''
    g=True
    for i in range(n):
        if a[i]=='1':
            ko+=1
        else:
            if ko<=k:
                k-=ko
                ans=ans+'0'
            else:
                for j in range(ko-k):
                    ans=ans+'1'
                ans=ans+'0'
                for j in range(k):
                    ans=ans+'1'
                for j in range(i+1,n):
                    ans=ans+a[j]
                print(ans)
                g=False
                break
    if g==True:
        for j in range(ko):
            ans=ans+'1'
        print(ans)