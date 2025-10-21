n,k=list(map(int,input().split()))

x=(n-(k-1)+1)//2
STR="0"*(x-1)+"1"

ANS=STR*(n//x+1)
print(ANS[:n])