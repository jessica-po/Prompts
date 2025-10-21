n,m = map(int,input().split())

min_i = 1
max_i = n

for i in range(m):
    l,r = map(int,input().split())
    min_i = max(min_i,l)
    max_i = min(max_i,r)

if max_i-min_i>=0:
    print(max_i-min_i+1)
else:
    print(0)