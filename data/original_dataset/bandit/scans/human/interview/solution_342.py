a, b, c = list(map(int, input().split()))
x = 2 * (c + min(a, b))
if a != b:
    x += 1
print(x)