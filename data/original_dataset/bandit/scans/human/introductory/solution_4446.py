n, a, b, k = map(int, input().split())
H = list(map(int, input().split()))
for i in range(n):
    H[i] %= (a + b)
    if H[i] == 0:
        H[i] = a + b
H.sort()
ans = 0
for x in H:
    if x <= a:
        ans += 1
    else:
        tok = (x + a - 1) // a - 1
        if k >= tok:
            k -= tok
            ans += 1
print(ans)