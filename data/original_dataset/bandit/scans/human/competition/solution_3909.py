n = int(input())

a = 1

while n % a == 0:
    a *= 3

print((n - 1) // a + 1)