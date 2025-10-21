a = input().split()
n = int(a[0])
p = float(a[1])
t = int(a[2])
den = 100 ** t
p = round(p * 100 + 1e-9)
q = 100 - p
ncr = [1 for i in range(2001)]
for i in range(1, t + 1):
        ncr[i] = ncr[i - 1] * (t - i + 1) // i
ans = 0
for i in range(2001):
        ans += min(i, n) * ncr[i] * (p ** i) * (q ** (t - i)) if t >= i else 0
ans /= den
print(ans)