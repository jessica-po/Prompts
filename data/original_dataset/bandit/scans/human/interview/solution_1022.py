n=int(input())
#x,y,z,t1,t2,t3=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

s=[0]*n

ans=True

for i in range(n):
    ans=ans and a[i]<=i and b[i]<=(n-i-1)
    s[i]=n-a[i]-b[i]

def qwe(s,j):
    l,r=0,0
    for i in range(len(s)):
        if i<j and s[i]>s[j]: l+=1
        elif i>j and s[i]>s[j]: r+=1
    return l,r



if ans:
    for i in range(n):
        l,r=qwe(s,i)
        ans=ans and a[i]==l and b[i]==r
        
    

    
if ans:
    print('YES')
    for i in range(n):
        print(n-a[i]-b[i],end=' ')
else: print('NO')