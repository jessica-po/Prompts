n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
b = []
for i in range(0, n-1):
    b.append((a[i]-(n-a[i+1]), i))
b.append((a[n-1]-(n-a[0]), n-1))
b = sorted(b)
ans = n*[0]
for i in range(n):
    # the line segment at index b[i][1]
    ans[b[i][1]] = i
for i in range(n):
    print(ans[i], end = ' ')