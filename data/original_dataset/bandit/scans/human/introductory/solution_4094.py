K = int(input())

a = [7] * (K + 1)
a[0] %= K
for i in range(1, K+1):
    a[i] = (10*a[i-1] + 7) % K

ans = [i+1 for i, ai in enumerate(a) if ai == 0]

if len(ans) > 0:
    print((ans[0]))
else:
    print((-1))