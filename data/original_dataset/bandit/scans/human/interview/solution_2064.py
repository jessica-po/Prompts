n = int(input());
if (n % 2 != 0):
        s = '7';
        n -= 3;
else:
    s = '1';
    n-=2;
for i in range(n // 2): s = s + '1';
print(s);