a, b = map(int, input().split())
if a == 9 and b == 1:
    print(9, 10)
elif a == b - 1:
    print(a, b)
elif a == b:
    print(a * 10, a * 10 + 1)
else:
    print(-1)