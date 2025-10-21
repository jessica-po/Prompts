import sys
n=int(sys.stdin.readline())

A=list(map(int,sys.stdin.readline().split()))

s=0
m=0

case=True
for item in A:
    if(item==50 and s>=1):
        m+=1
        s-=1
        continue
    if(item==100 and m>=1 and s>=1):
        m-=1
        s-=1
        continue
    if(item==100 and s>=3):
        s-=3
        continue
    if(item==25):
        s+=1
        continue
    case=False
    break

if(case):
    print("YES")
else:
    print("NO")