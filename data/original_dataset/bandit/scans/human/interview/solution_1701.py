n, m = map(int, input().split())

a = {}
for i in range(n):
    x, y = input().split()
    a[y] = x
    
for i in range(m):
    x, y = input().split()
    
    print(x, y, "#" + a[y.replace(';', '')])