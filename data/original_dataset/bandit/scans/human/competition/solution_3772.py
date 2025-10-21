a, b = list(map(int, input().split()))
res = 0

while b != 0:
    res += a // b
    a %= b
    a, b = b, a
print(res)