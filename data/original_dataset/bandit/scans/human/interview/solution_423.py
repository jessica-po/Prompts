p=1048583
q=1048589
modd=p*q*p*q
n,k=tuple(map(int,input().split()))
a=[0]
wenhao=0
gai=0
for i in range(n+1):
    m=input()
    if m[0]=='?':
        a.append('?')
        wenhao+=1
    else:
        a.append(int(m))
        gai+=1

if k==0:
    if (a[1]=='?' and gai&1==1) or a[1]==0:
        print('Yes')
    else:
        print('No')
else:
    if wenhao!=0:
        if n&1==1:
            print('Yes')
        else:
            print('No')
    else:
        m=a[n+1]
        nn=a[n]
        for i in range(n,0,-1):
            m,nn=(nn+k*m)%modd,a[i-1]
        if m==0:
            print('Yes')
        else:
            print('No')