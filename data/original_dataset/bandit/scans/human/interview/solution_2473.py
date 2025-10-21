n,k=map(int,input().split())
points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
points.sort()
ans=float('inf')
for i in range(n-k+1):
    for j in range(i+k-1,n):
        y_sorted=sorted(points[i:j+1],key=lambda x:x[1])
        height_min=float('inf')
        for l in range(j-i-k+2):
            height_min=min(height_min,y_sorted[l+k-1][1]-y_sorted[l][1])
            ans=min(ans,(points[j][0]-points[i][0])*height_min)
print(ans)