import numpy as np

n=int(input())
xy=[]
for i in range(n):
    xy.append(list(map(int,input().split())))

def naiseki(a,b):
    if (a[0]*b[0]+a[1]*b[1])>0.0:
        return True
    else:
        return False
    
ans=0

for i in range(1001):
    xl=np.cos(np.pi*2.0*i/1000.0)
    yl=np.sin(np.pi*2.0*i/1000.0)
    x=0
    y=0
    for j in range(n):
        if naiseki([xl,yl],xy[j]):
            x+=xy[j][0]
            y+=xy[j][1]
    ans=max(ans,np.sqrt(x**2+y**2))
print(ans)