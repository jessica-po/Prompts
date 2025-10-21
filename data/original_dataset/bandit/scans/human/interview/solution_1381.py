k, n, s, p = list(map(int, input().split()))

x = (n + s - 1) // s
y = k * x
z = (y + p - 1) // p

print(z)