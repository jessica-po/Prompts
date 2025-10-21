import sys

n=int(sys.stdin.readline())
A=[]
B=[]
diff=0
Ans=""
for i in range(n):
    x,y=list(map(int,sys.stdin.readline().split()))
    if(diff+x<=500):
        diff+=x
        Ans+="A"
    else:
        diff-=y
        Ans+="G"
if(abs(diff)<=500):
    sys.stdout.write(Ans)
else:
    print(-1)