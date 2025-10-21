n = int(input())
a = 1
while a * a < n:
    a += 1

if a * (a - 1) >= n:
    print(2 * a + 2 * (a - 1))
else:
    print(4 * a)