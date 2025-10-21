# ABC127
# A Ferris Wheel
a, b = list(map(int, input().split()))
if a > 12:
    print(b)
    return
elif a < 6:
    print((0))
    return
else:
    print((b // 2))
    return