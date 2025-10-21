n=int(input())
ar=list(map(int,input().split()))
pos=0
neg=0
for a in ar:
    if(a>0):pos+=1
    elif a<0:neg+=1
if(pos*2>=n):
    print(1)
elif neg*2>=n:
    print(-1)
else:
    print(0)