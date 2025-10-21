M = 0x3b800001
wa = 0;
n = int(input())
a = list(map(int, input().split()))
now = 1
wa += a[-1]
for i in range(n - 1)[::-1]:
    wa += (now * (n - i - 1) + now * 2) * a[i]
    wa %= M
    now *= 2
    now %= M
print(wa % M)