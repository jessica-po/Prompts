n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a)
ans = 0
c = k - 0.5
while s / n < c:
    s += k
    n += 1
    ans += 1
print(ans)