n, a, b = input(), map(int, input().split()), map(int, input().split())
print(sum((y // 2) * (y - y // 2) if y > 1 and 2 * x >= y else -1 for x, y in zip(a, b)))