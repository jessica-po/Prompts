n = int(input())
a = list(map(int, input().split()))
q = (10 ** 6) * [-1]
pnt = -1
ans = "YES"
for i in range(n):
    if pnt == -1:
        pnt += 1
        q[pnt] = a[i]
    else :
        if q[pnt] == a[i] or abs(q[pnt] - a[i]) % 2 == 0:
            q[pnt] = -1
            pnt -= 1
        else:
            pnt += 1
            q[pnt] = a[i]
if pnt > 0 :
    ans = "NO"
print(ans)