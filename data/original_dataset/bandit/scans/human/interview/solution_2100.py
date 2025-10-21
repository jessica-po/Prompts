n=int(input())
R=[]
L=[]
for i in range(n):
    x,y=input().split()
    R.append(x)
    L.append(y)

a=R.count("0")
b=L.count("0")

answer=min(a,n-a)+min(b,n-b)

print(answer)