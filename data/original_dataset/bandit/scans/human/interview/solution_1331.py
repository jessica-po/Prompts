n,m,k = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a.sort()

count = 0

start = 0
konec = 0
ur = 0
while start < len(a):
    if a[start] is not None:
        v = a[start]
        while konec < len(a) and a[konec] - v < m :
            ur += 1
            if ur >= k:
                #print(a,start,konec,ur)
                a[konec] = None
                count += 1
                ur -= 1
            konec += 1
    if a[start] is not None:
        ur -= 1
    start += 1

print(count)