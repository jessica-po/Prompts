import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n=int(input())
mod=10**9+7

ANS=[[0]*(n+1) for i in range(n+1)]

def bra(x,y):
    if ANS[x][y]!=0:
        return ANS[x][y]
    
    if x==y==0:
        ANS[x][y]=0
        return 0

    if (x+y)%2==1:
        A=1
    else:
        A=0

    if x==y:
        ANS[x][y]=A+bra(x-1,y)
        return ANS[x][y]

    elif x==0:
        ANS[x][y]=A+bra(x,y-1)
        return ANS[x][y]
    
    elif y==0:
        ANS[x][y]=A+bra(x-1,y)
        return ANS[x][y]

    elif x<y and x!=0 and y!=0:
        ANS[x][y]=A+bra(x-1,y)+bra(x,y-1)
        return ANS[x][y]

print(bra(n,n)%mod)