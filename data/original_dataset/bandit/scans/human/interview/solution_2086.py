n = int(input())
a = [int(i) for i in input().split()]
s, f = [int(i) for i in input().split()]
a = a + a
ln = f - s
ans = sum(a[:ln])
mx = ans
h = s
for i in range(n - 1):
    ans = ans - a[i] + a[i + ln]
    if ans > mx:
        ans = mx
        k = s + (n - (i + 2) + 1)
        if k > n:
            k -= n  
        h = k
    elif ans == mx:
        k = s + (n - (i + 2) + 1)
        if k > n:
            k -= n    
        h = min(h, k)
print(h)