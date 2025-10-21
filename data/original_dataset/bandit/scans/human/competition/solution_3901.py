def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def gcda(a):
    ans = a[0]
    for i in range(1, len(a)):
        ans = gcd(a[i], ans)
    return ans

n = int(input())
a = list(map(int, input().split()))
if 1 in a:
    print(sum([1 for i in a if i != 1]))
    return
    
if gcda(a) != 1:
    print(-1)
    return

mr=n+1
for i in range(n):
    g = a[i]
    for j in range(i+1, n):
        g = gcd(g, a[j])
        if g == 1:
            mr = min(mr, j-i)
            break
            
print(mr + n - 1)