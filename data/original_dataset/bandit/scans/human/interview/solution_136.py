a = input()
b = input()
n, m = len(a), len(b)
if n > m: b = '0' * (n - m) + b
else: a = '0' * (m - n) + a
i = 0
while i < max(n, m) and a[i] == b[i]:
    i += 1
print('=' if i == max(n, m) else '<' if int(a[i]) < int(b[i]) else '>')