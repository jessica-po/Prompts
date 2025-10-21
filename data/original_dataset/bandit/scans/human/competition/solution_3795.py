n = int(input())
d = int(input())
e = 5*int(input())

ans = n
d, e = min([d, e]), max([d, e])

for i in range(e):
    if (n-i*d) >= 0:
        ans = min([ans, (n-i*d)%e])
        
print(ans)