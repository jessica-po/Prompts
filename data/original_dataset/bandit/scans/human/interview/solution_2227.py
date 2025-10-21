s=input()
ans=0
s=s.replace("heavy","1")
s=s.replace("metal","2")
heavy=[]
metal=[]
n=len(s)
for i in range(n):
    if(s[i]=="1"):
        heavy.append(i)
    elif(s[i]=="2"):
        metal.append(i)

n=len(heavy)
nn=len(metal)
x=0
l=nn
for item in heavy:
    for i in range(x,nn):
        if(metal[i]>item):
            ans+=(nn-i)
            l=i
            break
    x=l;

print(ans)