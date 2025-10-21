input()
a = [int(x) for x in input().split()]
b = min(a)
print(-1 if any(x % b for x in a) else b)