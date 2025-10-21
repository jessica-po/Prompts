n, k = map(int, input().split())
h = list(map(int, input().split()))
a = [0]*(n-k+1)
a[0] = sum(h[0:k])
for i in range(1,n-k+1):
    a[i] = a[i-1]+h[i+k-1]-h[i-1]
m = min(a)
print(a.index(m)+1)