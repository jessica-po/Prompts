T=int(input())
answer=[]
for t in range(T):
    A,B=input().split()
    A=int(A)
    B=int(B)
    x=0
    if(A>B):
        r=B
        B=A
        A=r
    while(A>0 and B>0):
        r=B//A
        x+=r
        r*=A
        B=B-r
        if(A>B):
            r=B
            B=A
            A=r
    answer.append(x)

for t in range(T):
    print(answer[t])