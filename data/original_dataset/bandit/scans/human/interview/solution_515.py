k = int(input())

if k // 2 + k % 2 > 18:
    print(-1)
else:
    print('8' * (k // 2) + ('6' if k % 2 else ''))