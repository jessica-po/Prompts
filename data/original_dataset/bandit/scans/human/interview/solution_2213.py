n,m,k=map(int,input().split())
print(m*(m-1)//2)
for i in range(n):
    a=list(map(int,input().split()))
if k==0:
    for i in range(m):
        for j in range(i+1,m):
            print(i+1,j+1)
else:
    for i in range(m):
        for j in range(i+1,m):
            print(j+1,i+1)