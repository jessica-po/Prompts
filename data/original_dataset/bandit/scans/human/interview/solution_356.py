n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

ptra = 1
ptrb = 1
sa = a[0] 
sb = b[0]
ans = 0

while ptra != n and ptrb != m:
    if sa == sb:
        ans += 1
        sa = a[ptra]
        sb = b[ptrb]
        ptra += 1
        ptrb += 1
        continue
    if sa < sb:
        sa += a[ptra]
        ptra += 1
    else:
        sb += b[ptrb]
        ptrb += 1
while ptra != n:
    sa += a[ptra]
    ptra += 1
while ptrb != m:
    sb += b[ptrb]
    ptrb += 1
if sa != sb:
    print(-1)
    return
print(ans + 1)