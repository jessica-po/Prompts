# cook your dish here
n, m, k =map(int, input().split())
blasters=[]
for _ in range(k):
    blasters.append(list(map(int, input().split())))
grid=[[0 for _ in range(m)] for _ in range(n)]
for blaster in blasters:
    flag=0
    x, y, t, f = blaster
    x-=1 
    y-=1
    grid[x][y]=-1
    for i in range(n):
        if i+y-t-abs(x-i)>=0 and (i+y-t-abs(x-i))%f==0:
            if i>x:
                flag=1
            grid[i][y]=-1
        if i>x and flag==0:
            break
    flag=0
    for j in range(m):
        if j+x-t-abs(y-j)>=0 and (j+x-t-abs(y-j))%f==0:
            if j>y:
                flag=1
            grid[x][j]=-1
        if j>y and flag==0:
            break
for i in range(1,n):
    if grid[i-1][0]==-1:
        grid[i][0]=-1
for j in range(1,m):
    if grid[0][j-1]==-1:
        grid[0][j]=grid[0][j-1]
for i in range(1,n):
    for j in range(1,m):
        if grid[i][j-1]==-1 and grid[i-1][j]==-1:
            grid[i][j]=-1
if grid[-1][-1]==0:
    print('YES')
    print(n+m-2)
else:
    print('NO')