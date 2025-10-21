k, a, b, v = map(int, input().split())
for i in range(1, 1010):
    if a <= v * (i + min(b, (k - 1) * i)):
        print(i)
        break