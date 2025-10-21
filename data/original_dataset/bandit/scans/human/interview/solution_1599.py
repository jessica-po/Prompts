s=input()
t=int(input())

ans=[]
n=len(s)
clue=[0]*n
for i in range(n-1):
    if(s[i]==s[i+1]):
        clue[i]+=1
L=[clue[0]]
for i in range(1,n):
    L.append(L[i-1]+clue[i])

for i in range(t):
    A,B=input().split()
    A=int(A)-1
    B=int(B)-1
    r=0
    x=L[B-1]
    y=L[A-1]
    if(A-1<0):
        y=0
    ans.append(x-y)

for i in range(t):
    print(ans[i])