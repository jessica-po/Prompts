k = 0
ans = 0
n = int(input())
a = input().split()
for i in range(2 * n):
    s = float(a[i])
    if s != int(s):
        k+=1
        ans += (int(s) + 1 - s)

if ans - int(ans) > 0.5:
    p = int(ans) + 1
else:
    p = int(ans)
if p > n:
    p = n
if (p + n >= k):
    print('%.3f'% abs(ans - p))
else:
    print('%.3f'% abs(ans - k + n))