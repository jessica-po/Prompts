import math
a,b,c=map(int,input().split())
D = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)
ans1=max(x1,x2)
ans=min(x1,x2)
print(ans1)
print(ans)