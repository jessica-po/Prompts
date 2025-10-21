def f(n,k):
    s=[]
    row=[[0 for i in range(n)] for i in range(n)]
    col=[[0 for i in range(n)] for i in range(n)]
    flag=0
    for i in range(n):
        s.append(list(input().strip()))
    for i in range(n):
        for j in range(n):
            if s[i][j]=="X":
                s[i][j]=1
            elif s[i][j]==".":
                s[i][j]=0
                flag=1
            else:
                s[i][j]=-1
            row[i][j]=col[j][i]=s[i][j]
            
    for i in range(n):
        temp=[]
        for j in range(n-k+1):
            temp=s[i][j:j+k]
            if sum(temp)>=k-1:
                return True
            temp=col[i][j:j+k]
            if sum(temp)>=k-1:
                return True
    d1=[0 for i in range(n)]
    d2=[0 for i in range(n)]
    for i in range(n):
        d1[i]=s[i][i]
        d2[i]=s[i][n-i-1]
    for i in range(n-k+1):
        if sum(d1[i:i+k])>=k-1 or sum(d2[i:i+k])>=k-1:
            return True
    return False
t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    if f(n,k):
        print("YES")
    else:
        print("NO")