__author__ = 'User'
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = arr[i] % m
d = [0] * m
for e in arr:
    t = [0] * m
    t[e] = 1
    for i in range(m):
        if d[i] == 1:
            #print("T", i + e)
            t[(i + e) % m] = 1
    for i in range(m):
        if t[i] == 1:
            d[i] = 1
    #print(d)
    if d[0] == 1:
        break
if d[0] == 1:
    print("YES")
else:
    print("NO")
#print(d)
#print(arr)