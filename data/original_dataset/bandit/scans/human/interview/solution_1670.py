s1=input()
s2=input()
L={}
L['h']=s1
L['a']=s2

n=int(input())
D={}
F={}
for i in range(n):
    a=input().split()
    m=int(a[0])
    t=L[a[1]]
    num=int(a[2])
    c=a[3]
    if((t,num) in D):
        continue
    if(c=='r' or (c=='y' and ((t,num) in F))):
        D[(t,num)]=1
        print(t,num,m)
    else:
        F[(t,num)]=1